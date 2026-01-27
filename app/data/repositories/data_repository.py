# En lista som sparas i minnet (nollställs om du startar om servern)
_tasks = ["Köp kaffe", "Bygg en app", "Fira framgången", "Lär dig Three-Tier"]

def fetch_data_from_db():
    return "Data hämtad från Databasen (Data Layer)"

def get_all_tasks():
    return _tasks

def add_task_to_db(task):
    if task:
        _tasks.append(task)