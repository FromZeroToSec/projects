import string

def open_file (filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("Error: file not found")
        return ""

def clean_text(raw_text):
    words = raw_text.lower().split()
    clean_words = []
    for word in words:
        word = word.strip(string.punctuation)
        clean_words.append(word)
    return clean_words