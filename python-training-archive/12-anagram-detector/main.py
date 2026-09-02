def normalize(word):
    """Removes spaces and converts to lowercase"""
    return word.lower().replace(" ", "")


def is_anagram(word1, word2):
    """Returns True if the given words are anagrams, False otherwise"""
    return sorted(normalize(word1)) == sorted(normalize(word2))


def main():
    """takes two words as input and checks if they are anagrams"""
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    if is_anagram(word1, word2):
        print(f"{word1} and {word2} are anagrams.")
    else:
        print(f"{word1} and {word2} are not anagrams.")


if __name__ == "__main__":
    main()