# 05 — File Encryptor

A CLI tool to encrypt and decrypt files using symmetric encryption (Fernet / AES-128).

---

## What it does

- Generates a secure encryption key and saves it locally
- Encrypts any file in place using the generated key
- Decrypts any previously encrypted file
- Handles missing file errors gracefully

---

## Tech stack

- Python 3
- [`cryptography`](https://pypi.org/project/cryptography/) — Fernet symmetric encryption

---

## Installation

```bash
git clone https://github.com/FromZeroToSec/05-file-encryptor.git
cd 05-file-encryptor
pip install cryptography
```

---

## Usage

```bash
python main.py
```

```
What do you want to do?
1. Generate key
2. Encrypt file
3. Decrypt file
4. Quit
Choice:
```

### Workflow

```bash
# Step 1 — generate the key (do this once)
Choice: 1

# Step 2 — encrypt a file
Choice: 2
Enter the file path: /path/to/file.txt

# Step 3 — decrypt the file
Choice: 3
Enter the file path: /path/to/file.txt
```

> ⚠️ Keep `secret.key` safe. Without it, encrypted files cannot be recovered.  
> ⚠️ Never commit `secret.key` to Git.

---

## What this demonstrates

- Symmetric encryption with Fernet (AES-128-CBC + HMAC)
- Binary file I/O (`rb` / `wb` modes)
- CLI menu loop with input validation
- Error handling with `try/except`
- Python best practices: docstrings, `if __name__ == "__main__"`, `.gitignore`

---

## Project structure

```
05-file-encryptor/
├── main.py        # Main script
├── .gitignore     # Excludes secret.key and test files
└── README.md
```

