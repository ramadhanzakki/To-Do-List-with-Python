import src.view_task

def view_categorized_task(database):
    all_tasks = src.view_task.view_task(database)
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