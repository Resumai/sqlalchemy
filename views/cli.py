from datetime import datetime as dt
from models.worker import Worker
from services.workers_service import get_all_workers, create_worker, update_worker




def print_workers_table(workers: list[Worker]):
    print("\n")
    print(f"{'ID':<4} {'Name':<12} {'Surname':<15} {'Birth Date':<12} {'Salary':<8} {'Works Since':<12}")
    print("-" * 67)

    for w in workers:
        print(f"{w.id:<4} {w.name:<12} {w.surname:<15} {str(w.birth_date.date()):<12} {w.salary:<8} {str(w.works_since.date()):<12}")
    print("\n")

def cli_create_worker():
    name_input = input("Please enter name of worker: ")
    surname_input = input("Please enter surname of worker: ")
    birth_date_input = input("Please enter birth date of worker, format YYYY-MM-DD: ")
    salary_input = input("Please enter salary of worker: ")
    create_worker(name_input, surname_input, birth_date_input, int(salary_input))



def cli_update_worker():
    workers = get_all_workers()
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
        


def cli_delete_worker():
    workers = get_all_workers()
    print_workers_table(workers)
    delete_input = input("Enter ID of worker to delete:")
    return int(delete_input)