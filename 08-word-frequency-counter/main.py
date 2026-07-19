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

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
        

def get_top_words (word_count, n):
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_count[:n]

def display_top_words (word_count, n):
    top_words = get_top_words(word_count, n)
    for word, count in top_words:
        print(f"{word}: {count}")

def main():
    filename = input("Enter the name of the file: ")
    raw_text = open_file(filename)
    words = clean_text(raw_text)
    word_count = count_words(words)
    display_top_words(word_count, 10)


if __name__ == "__main__":
    main()