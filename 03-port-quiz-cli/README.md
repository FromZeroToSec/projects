# 03-port-quiz-cli

A CLI quiz game to test your knowledge of network ports and their associated services.

## Usage

```bash
python main.py
```

## How it works

- A random port is selected from 25 common network ports
- You have 5 attempts to guess the correct service
- After 2 wrong answers, a hint reveals the first letter of the service
- The game loops until you choose to quit

## What it demonstrates

- Python dictionaries and random selection
- Input validation and loop control
- Win/lose conditions with attempt tracking
- Hints system based on attempt count

## Ports covered

FTP, SSH, Telnet, SMTP, DNS, HTTP, HTTPS, RDP, MySQL, PostgreSQL, MongoDB, Redis, Docker, and more.

## Project structure

```
03-port-quiz-cli/
├── main.py
└── .gitignore
```