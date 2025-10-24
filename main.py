import csv
import os


def view_task(database):
    task = []

    try:
        with open(database, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                task.append(row)
    except FileNotFoundError:
        print(f"--> FATAL ERROR: File Not Found!")
        print(f"--> The program is trying to find the file {database}")
        print(f"--> Pastikan path '{database}' sudah benar di main.py dan file-nya ada.")
        return []
    
    return task


def add_task(database: str, input_task):
    file_exists = os.path.exists(database)

    try:
        new_data = {'task' : input_task}

        with open(database, mode='a', newline='') as file:
            FIELDSNAME = ['task']
            writer = csv.DictWriter(file, fieldnames=FIELDSNAME)

            if not file_exists:
                writer.writeheader()

            writer.writerow(new_data)

        return True

    except IOError as e:
        print(f"Error: Failed to write to file {database}. Details: {e}")
        return False


def remove_task(database, id_task: int):
    all_tasks = view_task(database)
    tasks_to_keep = []

    if id_task >= len(all_tasks) or id_task <= 0:
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
        

def main():
    is_continue = True
    
    while is_continue:
        print('To-Do-List Menu:\n1. View Task\n2. Add a Task\n3. Remove Task\n4. Exit')

        try:
            user_input = int(input('Enter your choice: '))
        except ValueError:
            print('Error Input: Please input a number')
            continue
            
        if user_input == 1:
            all_tasks = view_task('database.csv')
            for i, task in enumerate(all_tasks, start=1):
                task_text = task['task']
                print(f'{i}. {task_text}')

        elif user_input == 2:
            task_name = input('Enter a new task: ')

            if add_task('database.csv', task_name):
                print(f'{task_name} is successfully added')
            else:
                print('Operation failed, please check again')

        elif user_input == 3:
            all_tasks = view_task('database.csv')
            for i, task in enumerate(all_tasks, start=1):
                task_text = task['task']
                print(f'{i}. {task_text}')

            while True:
                try:
                    remove_input = int(input('Select the number to be deleted: '))
                    break
                except ValueError:
                    print('Value Error: Please enter a number')
                    continue
            
            remove_task('database.csv', remove_input)
            
        elif user_input == 4:
            is_continue = False

        else:
            print('Invalid Input: Please input 1, 2, 3, or 4')


if __name__ == "__main__":
    main()