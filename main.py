import csv
import os

FIELDSNAME = ['task', 'categories']

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



def view_categorized_task(database):
    all_tasks = view_task(database)
    categorized_result = {}

    for row_dict in all_tasks:
        # Ambil kategori dari data, default 'Uncategorized' jika kosong
        category = row_dict.get('categories', 'Uncategorized').strip()
        if not category:
            category = 'Uncategorized' # Handle string kosong
            
        task_name = row_dict.get('task', 'Task Tanpa Nama')
        
        # Buat list jika kategori ini baru pertama kali ditemukan
        if category not in categorized_result:
            categorized_result[category] = []
            
        # Tambahkan nama task ke list kategori yang sesuai
        categorized_result[category].append(task_name)
        
    return categorized_result



def add_task(database: str, input_task: str, categories_task: str):
    file_exists = os.path.exists(database)

    try:
        new_data = {'task' : input_task, 'categories' : categories_task}

        with open(database, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDSNAME)

            if not file_exists:
                writer.writeheader()

            writer.writerow(new_data)

        return True

    except IOError as e:
        print(f"Error: Failed to write to file {database}. Details: {e}")
        return False


def remove_task(database, id_task: int):
    try:
        all_tasks = view_task(database)
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
        

def main():
    is_continue = True
    
    while is_continue:
        print('\n==========================================')
        print('|             📋To-Do-List Menu:          |')
        print('==========================================')
        print('1. View Task\n2. Add a Task\n3. Remove Task\n4. Exit\n')

        try:
            user_input = int(input('Enter your choice: '))
        except ValueError:
            print('⚠️Error Input⚠️: Please input a number')
            continue
            
        if user_input == 1:
            print('\n==========================================')
            print('|           📂Tasks by Category:         |')
            print('==========================================')
            
            categorized_data = view_categorized_task('database.csv')
            
            if not categorized_data:
                print('Tidak ada task untuk dikelompokkan.')
            else:
                for category, task_list in categorized_data.items():
                    print(f'\n--- 🗂️  Kategori: {category} ---')
                    for i, task_name in enumerate(task_list, start=1):
                        print(f"  {i}. {task_name}")
        elif user_input == 2:
            print('\n==========================================')
            print('|                🆕New Task:             |')
            print('==========================================')
            task_name = input('Enter a new task: ')
            categories_input = input('Enter the categories: ')

            if add_task('database.csv', task_name, categories_input):
                print(f'{task_name} is successfully added🥳')
            else:
                print('⚠️WARNING⚠️: Operation failed, please check again')

        elif user_input == 3:
            print('\n==========================================')
            print('|              ❌Delete Task:            |')
            print('==========================================')
            print('\n📋Task List: ')
            all_tasks = view_task('database.csv')
            for i, task in enumerate(all_tasks, start=1):
                task_text = task['task']
                print(f'{i}. {task_text}')

            while True:
                try:
                    remove_input = int(input('Select the number to be deleted: '))
                    break
                except ValueError:
                    print('⚠️Value Error⚠️: Please enter a number')
                    continue
            
            remove_task('database.csv', remove_input)
            
        elif user_input == 4:
            print('\n==========================================')
            print('|              Thank You😍              |')
            print('==========================================')
            is_continue = False

        else:
            print('⚠️Invalid Input⚠️: Please input 1, 2, 3, or 4')


if __name__ == "__main__":
    main()