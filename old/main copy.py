from sqlalchemy import create_engine, select, Column, Integer, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from datetime import datetime as dt
 
engine = create_engine("mysql://root:slapta@localhost:3306/task_schema")

class Base(DeclarativeBase):
    pass

class Workers(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    birth_date : dt = Column(DateTime)
    salary = Column(Integer)
    works_since : dt = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"<Worker(id={self.id}, name='{self.name}', surname='{self.surname}', birth_date={self.birth_date.date()}, salary={self.salary}, works_since={self.works_since.date()})>"

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)



# input_birth_date: Must be YYYY-MM-DD str format or datetime object.
def create_worker(name_choice : str, surname_choice : str, birth_date_choice : str | dt, salary_choice : int):

    if isinstance(birth_date_choice, str):
        try:
            birth_date_choice = dt.strptime(birth_date_choice, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD (e.g., '1990-05-11')")

    with Session() as s:
        user = Workers(name = name_choice, 
                       surname = surname_choice, 
                       birth_date = birth_date_choice,
                       salary = salary_choice) 
        s.add(user)
        s.commit()


# create_worker("John", "Johniest", 2000, "1993-10-02")
# create_worker("Alice", "Smith", 3000, dt(1990, 5, 11))


def get_all_info():
    with Session() as s:
        select_all = select(Workers)
        results = s.execute(select_all).scalars().all()
        return results
    

# workers = get_all_info()
# for worker in workers:
#     print(worker.id, worker.name, worker.surname, worker.salary, worker.works_since)

def delete_worker_by_id(worker_id: int):
    with Session() as s:
        worker = s.get(Workers, worker_id)
        if worker:
            s.delete(worker)
            s.commit()


def update_worker(worker_id: int, **kwargs):
    with Session() as s:
        worker = s.get(Workers, worker_id)
        if worker:
            for key, value in kwargs.items():
                if hasattr(worker, key):
                    setattr(worker, key, value)
            s.commit()

# update_worker(1, name="Jonas", salary=4500)
# update_worker(2, surname="Petrauskas", birth_date=dt(1985, 4, 9))




# UI STUFF starting here

# def print_all_info():
#     workers = get_all_info()
#     for worker in workers:
#         print(worker)


def print_workers_table(workers: list[Workers]):
    print("\n")
    print(f"{'ID':<4} {'Name':<12} {'Surname':<15} {'Birth Date':<12} {'Salary':<8} {'Works Since':<12}")
    print("-" * 67)

    for w in workers:
        print(f"{w.id:<4} {w.name:<12} {w.surname:<15} {str(w.birth_date.date()):<12} {w.salary:<8} {str(w.works_since.date()):<12}")
    print("\n")

def ui_create_worker():
    name_input = input("Please enter name of worker: ")
    surname_input = input("Please enter surname of worker: ")
    birth_date_input = input("Please enter birth date of worker, format YYYY-MM-DD: ")
    salary_input = input("Please enter salary of worker: ")
    create_worker(name_input, surname_input, birth_date_input, int(salary_input))



def ui_update_worker():
    workers = get_all_info()
    print_workers_table(workers)
    id_input = int(input("Enter ID of worker you want to update information: "))
    choice_input = input(f"What would you like to update?\n"
                       f"1.Name\n"
                       f"2.Surname\n"
                       f"3.Birth date\n"
                       f"4.Salary\n"
                       f"0.Exit\n"
                       f"What would you like to to do : ")
    match int(choice_input):
        case 1:
            name_new = input("Enter new name:")
            update_worker(id_input, name=name_new)
        case 2:
            surname_new = input("Enter new surname:")
            update_worker(id_input, surname=surname_new)
        case 3:
            birth_date_new = input("Enter new birth day, format YYYY-MM-DD: ")
            date_obj = dt.strptime(birth_date_new, "%Y-%m-%d")
            update_worker(id_input, birth_date=date_obj)
        case 4:
            salary_new = input("Enter new salary:")
            update_worker(id_input, salary=int(salary_new))
        case 0:
            return


def ui_delete_worker_choice():
    workers = get_all_info()
    print_workers_table(workers)
    delete_input = input("Enter ID of worker to delete:")
    return int(delete_input)



while True:
    print(f'1. View workers\n'
          f'2. Create worker\n'
          f'3. Update worker\n'
          f'4. Delete worker\n'
          f'0. Exit prgoram')
    user_input = input("What would you like to do? Type number: \n")


    match int(user_input):
        case 1:
            workers = get_all_info()
            print_workers_table(workers)
        case 2:
            ui_create_worker()
        case 3:
            ui_update_worker()
        case 4:
            delete_choice = ui_delete_worker_choice()
            delete_worker_by_id(delete_choice)
            print("Worker data deleted.")
        case 0:
            break