from sqlalchemy import select
from db import Session
from models.worker import Worker
from datetime import datetime as dt


# input_birth_date: Must be YYYY-MM-DD str format or datetime object.
def create_worker(name_choice : str, surname_choice : str, birth_date_choice : str | dt, salary_choice : int):

    if isinstance(birth_date_choice, str):
        try:
            birth_date_choice = dt.strptime(birth_date_choice, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD (e.g., '1990-05-11')")

    with Session() as s:
        user = Worker(name = name_choice, 
                       surname = surname_choice, 
                       birth_date = birth_date_choice,
                       salary = salary_choice) 
        s.add(user)
        s.commit()


# create_worker("John", "Johniest", 2000, "1993-10-02")
# create_worker("Alice", "Smith", 3000, dt(1990, 5, 11))


def get_all_workers():
    with Session() as s:
        select_all = select(Worker)
        results = s.execute(select_all).scalars().all()
        return results
    

# workers = get_all_info()
# for worker in workers:
#     print(worker.id, worker.name, worker.surname, worker.salary, worker.works_since)

def delete_worker_by_id(worker_id: int):
    with Session() as s:
        worker = s.get(Worker, worker_id)
        if worker:
            s.delete(worker)
            s.commit()


def update_worker(worker_id: int, **kwargs):
    with Session() as s:
        worker = s.get(Worker, worker_id)
        if worker:
            for key, value in kwargs.items():
                if hasattr(worker, key):
                    setattr(worker, key, value)
            s.commit()

# update_worker(1, name="Jonas", salary=4500)
# update_worker(2, surname="Petrauskas", birth_date=dt(1985, 4, 9))
