import src.view_task
import src.add_task
import src.remove_task
import src.view_categorized_task

def main():
    is_continue = True
    
    while is_continue:
        print('\n==========================================')
        print('|            📋To-Do-List Menu:          |')
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
            
            categorized_data = src.view_categorized_task.view_categorized_task('database.csv')
            
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

            if src.add_task.add_task('database.csv', task_name, categories_input):
                print(f'{task_name} is successfully added🥳')
            else:
                print('⚠️WARNING⚠️: Operation failed, please check again')

        elif user_input == 3:
            print('\n==========================================')
            print('|              ❌Delete Task:            |')
            print('==========================================')
            print('\n📋Task List: ')
            all_tasks = src.view_task.view_task('database.csv')
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
            
            src.remove_task.remove_task('database.csv', remove_input)
            
        elif user_input == 4:
            print('\n==========================================')
            print('|              Thank You😍              |')
            print('==========================================')
            is_continue = False

        else:
            print('⚠️Invalid Input⚠️: Please input 1, 2, 3, or 4')


if __name__ == "__main__":
    main()