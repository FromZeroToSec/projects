import json

def load_tasks():
    """Load tasks from the JSON file, or return an empty list if missing/corrupted."""
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
        print("The file has been loaded.")
    except FileNotFoundError:
        tasks = []
        print("The file does not exist. It will be created.")
    except json.JSONDecodeError:
        tasks = []
        print("The file is empty or corrupted. It will be created.")
    return tasks

def add_task(task, tasks):
    """Add a task to the list."""
    tasks.append(task)
    print("The task has been added.")

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file)
    print("The file has been saved.")



