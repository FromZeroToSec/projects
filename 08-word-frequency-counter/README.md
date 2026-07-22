# Word Frequency Counter

A command-line tool that reads a text file and displays the most frequently used words, filtering out common English and French stop words.

## Features

- Reads any `.txt` file provided by the user
- Cleans text (lowercase, punctuation removal)
- Filters out common stop words (English and French)
- Counts word occurrences
- Displays the top 10 most frequent words

## Usage

```bash
python3 main.py
```

You will be prompted to enter the name of the text file to analyze:

```
Enter the name of the file: test.txt
```

Example output:

```
security: 10
python: 6
automation: 6
data: 5
linux: 5
network: 4
git: 4
devsecops: 3
firewall: 3
encryption: 3
```

## What this demonstrates

- File reading with proper error handling (`try`/`except`)
- Text normalization (case handling, punctuation stripping)
- Dictionary-based frequency counting
- Sorting complex data structures with custom keys
- Separation of concerns across single-responsibility functions
- Basic multilingual text processing (stop word filtering)

## Requirements

- Python 3
- No external dependencies (standard library only)

## Project structure

```
08-word-frequency-counter/
├── main.py
├── test.txt
└── README.md
```
