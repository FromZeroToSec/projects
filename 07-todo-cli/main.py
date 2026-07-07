import json

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

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file)
    print("The file has been saved.")

save_tasks(tasks)