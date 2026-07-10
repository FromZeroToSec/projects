# 07 - Todo CLI

A command-line task manager that lets users add, list, and persist tasks to a JSON file. Built as part of the FromZeroToSec DevSecOps portfolio.

## What it does

- Add new tasks through an interactive menu
- List all saved tasks with numbering
- Save tasks to a local JSON file (tasks.json)
- Reload existing tasks automatically on startup
- Handles missing or corrupted data files gracefully

## Usage

python main.py

You'll see an interactive menu:

1. Add a task
2. List tasks
3. Save tasks
4. Exit

Enter the number corresponding to your choice. Tasks are automatically saved when you exit (option 4).

## Technical highlights

- **File I/O with error handling**: uses try/except to catch FileNotFoundError and json.JSONDecodeError, so the program never crashes on a missing or corrupted file — it simply starts with an empty task list.
- **Single-responsibility functions**: load_tasks(), add_task(), and save_tasks() each handle exactly one concern, with no reliance on global state — all data is passed explicitly through parameters.
- **Input validation**: empty or whitespace-only tasks are rejected before being added.
- **Data persistence**: tasks are stored in JSON format, human-readable and easy to inspect or extend.

## Requirements

- Python 3.x (standard library only, no external dependencies)

## Project structure

07-todo-cli/
├── main.py
├── .gitignore
└── README.md
