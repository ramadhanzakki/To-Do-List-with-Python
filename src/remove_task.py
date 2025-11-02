import csv
import src.view_task

def remove_task(database, id_task: int):
    try:
        all_tasks = src.view_task.view_task(database)
        if not all_tasks:
            print('No tasks, Nothing can be deleted')
            return
    except FileNotFoundError:
        print('Error 101: Database not Found')
        return

    tasks_to_keep = []

    if id_task > len(all_tasks) or id_task <= 0:
        print('Task Not Found')
    else:
        for i, task_name in enumerate(all_tasks, start=1):
            if i != id_task:
                tasks_to_keep.append(task_name)

        try:
            FIELDSNAME = tasks_to_keep[0].keys() if tasks_to_keep else all_tasks[0].keys()
            
            with open(database, mode='w') as file:
                writer = csv.DictWriter(file, fieldnames=FIELDSNAME)
                writer.writeheader()
                writer.writerows(tasks_to_keep)
            
            print(f'Data with id {id_task} has been successfully deleted')

        except Exception as e:
            print(f'An error occurred while deleting the file ith id {id_task}')