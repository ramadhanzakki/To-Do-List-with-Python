import csv

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