# Palindrome Checker — detects if a word or phrase reads the same forwards and backwards

def is_palindrome(word):
    """Returns True if the given word is a palindrome, False otherwise"""
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def main():
    """Main function"""
    print("Palindrome Checker")
    while True: 
        word = input("Enter a word: ")
        if is_palindrome(word):
            print(f"{word} is a palindrome.")
        else:
            print(f"{word} is not a palindrome.")
        play_again = input("Play again? (y/n): ").lower()
        print("-" * 50)# Separator
        if play_again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()