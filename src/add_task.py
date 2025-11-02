import csv
import os

FIELDSNAME = ['task', 'categories']

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