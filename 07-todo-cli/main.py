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

def main():
    """Main function of the program."""
    tasks = load_tasks()
    while True:
        print("1. Add a task")
        print("2. List tasks")
        print("3. Save tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            task = task.strip()
            if not task:
                print("The task cannot be empty. Please try again.")
                continue
            add_task(task, tasks)
        elif choice == "2":
            print("Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
        elif choice == "3":
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()