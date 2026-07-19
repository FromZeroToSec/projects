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


def remove_stopwords(words):
    stop_words_en = ["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "was", "were", "will", "with"]
    stop_words_fr = ["le", "la", "les", "un", "une", "des", "et", "ou", "de", "du", "à", "en", "est", "que", "qui", "pour", "dans", "sur", "avec", "ce", "cette", "ces", "il", "elle", "je", "tu", "nous", "vous", "se"]
    stop_words = stop_words_en + stop_words_fr
    filtered_words = []
    for word in words:
        if word not in stop_words:
            filtered_words.append(word)
    return filtered_words


def main():
    filename = input("Enter the name of the file: ")
    raw_text = open_file(filename)
    words = clean_text(raw_text)
    words = remove_stopwords(words)
    word_count = count_words(words)
    display_top_words(word_count, 10)


if __name__ == "__main__":
    main()