# 03-port-quiz-cli

A CLI quiz game to test your knowledge of network ports and their associated services.

## Usage

```bash
python main.py
```

## Modes

**Mode 1 — Find the service**: A random port is displayed, you must identify the associated service.

**Mode 2 — Find the port**: A random service is displayed, you must identify the associated port number.

## How it works

- 25 common network ports covered (FTP, SSH, HTTP, RDP, MySQL, MongoDB, Docker, and more)
- 5 attempts per question
- Hint revealed after 2 wrong answers (first letter for mode 1, first digit for mode 2)
- Input validation on mode selection and port answers
- Replay option after each round

## What it demonstrates

- Python dictionaries and random selection
- Dual-mode CLI logic with input validation
- try/except for type conversion errors
- Hints system based on attempt count
- Clean loop control with break and continue

## Project structure

```
03-port-quiz-cli/
├── main.py
└── .gitignore
```
```