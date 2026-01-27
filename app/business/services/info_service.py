from app.data.repositories.data_repository import fetch_data_from_db, get_all_tasks, add_task_to_db

def get_welcome_message():
    db_info = fetch_data_from_db()
    return f"Business Layer säger: {db_info}"

def get_processed_tasks():
    # Vi hämtar listan och sorterar den i bokstavsordning
    return sorted(get_all_tasks())

def add_new_task(task_text):
    # Logik: Se till att texten inte är tom och rensa mellanslag
    if task_text:
        clean_task = task_text.strip()
        if len(clean_task) > 0:
            add_task_to_db(clean_task)