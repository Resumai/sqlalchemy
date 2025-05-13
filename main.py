from services.workers_service import get_all_workers, delete_worker_by_id
from views.cli import print_workers_table, cli_create_worker, cli_update_worker, cli_delete_worker

# alembic revision --autogenerate -m "Comment"
# alembic upgrade head
# alembic stamp head


while True:
    print(f'1. View workers\n'
          f'2. Create worker\n'
          f'3. Update worker\n'
          f'4. Delete worker\n'
          f'0. Exit prgoram')
    user_input = input("What would you like to do? Type number: \n")


    match int(user_input):
        case 1:
            workers = get_all_workers()
            print_workers_table(workers)
        case 2:
            cli_create_worker()
        case 3:
            cli_update_worker()
        case 4:
            delete_choice = cli_delete_worker()
            delete_worker_by_id(delete_choice)
            print("Worker data deleted.")
        case 0:
            break
