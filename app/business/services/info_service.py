from app.data.repositories.data_repository import fetch_data_from_db, get_all_tasks

def get_welcome_message():
    db_info = fetch_data_from_db()
    return f"Business Layer säger: {db_info}"

# Ny funktion!
def get_processed_tasks():
    tasks = get_all_tasks()
    # Här kan vi t.ex. sortera dem eller ändra dem om vi vill
    return tasks