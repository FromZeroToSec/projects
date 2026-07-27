# Contact Book CLI

A command-line contact manager built in Python. Add, view, search, update, and delete contacts, with data persisted to a local JSON file between runs.

## Features

- **Add contact** — store a new contact (name, phone, email)
- **View contacts** — list all saved contacts
- **Search contact** — find a contact by name
- **Update contact** — edit one or more fields of an existing contact, leaving a field blank to keep its current value
- **Delete contact** — remove a contact by name
- **Persistent storage** — contacts are saved to `contacts.json` after every change, and reloaded automatically on startup

## Usage

```bash
python main.py
```

Follow the on-screen menu to choose an action (1–6).

## What this demonstrates

- CRUD operations on a structured in-memory data set (list of dictionaries)
- Separation of concerns: input handling, data manipulation, and display are kept in distinct functions
- Error handling for invalid menu input and missing data files
- Data persistence using the `json` module
- DRY principle applied via a shared `print_contact` helper
