# 02 — Auth Login Tentatives

A command-line authentication system built in Python.  
The user has 3 attempts to enter the correct credentials. After 3 failures, the account is locked.  
Passwords are never stored in plain text — SHA-256 hashing is used via the `hashlib` module.

---

## Features

- Maximum 3 login attempts with attempt counter
- Password hashed with SHA-256 (no plain text storage)
- Exit option available at any prompt (`exit`)
- Account locked message after all attempts are exhausted

---

## Installation & Usage

**Requirements:** Python 3.x

```bash
git clone https://github.com/FromZeroToSec/02-auth-login-tentatives-.git
cd 02-auth-login-tentatives-
python main.py
```

**Demo credentials:**
- Username: `mehdi`
- Password: `MotDePasseTest123`

---

## What This Demonstrates

- Python control flow (loops, conditions, break)
- Secure password handling with `hashlib` SHA-256
- Input validation and user feedback
- Clean project structure with conventional commits

---

## Project Structure

```
02-auth-login-tentatives/
├── main.py        # Main application
└── .gitignore     # Python gitignore
```