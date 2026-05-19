
# 06 — Caesar Cipher

A command-line tool to encrypt and decrypt text using the Caesar cipher algorithm.

## What it does

- Encrypts any text by shifting each letter by a chosen value
- Decrypts any previously encrypted text
- Handles uppercase, lowercase, and special characters
- Validates user input (non-integer shift rejected)

## Usage

```bash
python3 main.py
```

```
1. Encrypt
2. Decrypt
3. Exit
--------------------------------------------------
Enter your choice: 1
Enter the text: Hello World
Enter the shift: 3
Encrypted text: Khoor Zruog
```

## What it demonstrates

- String manipulation and ASCII arithmetic
- Modular arithmetic for alphabet wrapping
- Clean function design: `decrypt` reuses `encrypt` with a negative shift
- Input validation with `try/except ValueError`
- CLI loop with graceful exit

## Project structure

```
06-caesar-cipher/
├── main.py
└── .gitignore
```

## Tech

Python 3 — standard library only
