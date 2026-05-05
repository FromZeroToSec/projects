04 — Password Strength Checker

A terminal-based tool that evaluates password strength based on security criteria.

## Features

- Validates minimum password length (8 characters)
- Scores password on 4 criteria: length, uppercase, digit, special character
- Returns strength label: Too Weak / Very Weak / Weak / Medium / Strong
- Provides detailed feedback on missing criteria
- Replay option after each check

## Usage

```bash
python main.py
```
What is your password? hello
Too short!
What is your password? Hello123!
Password strength: Strong
Missing: None
Again? (y/n) n
Goodbye

## What it demonstrates

- Pure functions with single responsibility
- String validation with built-in methods (`isupper`, `isdigit`, `isalnum`)
- Input validation with `while` loops
- Score-based logic and conditional strength mapping
- Clean CLI structure with replay loop

