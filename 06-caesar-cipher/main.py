"""
A simple Caesar cipher CLI tool.
Encrypt and decrypt text using the ancient rotation method.
"""
def encrypt(text, shift):
    """Encrypt a text using Caesar cipher with the given shift."""
    result = ""
    for letter in text:
        if letter.isupper():
            result += chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        elif letter.islower():
            result += chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += letter 
    return result


def decrypt(text, shift):
    """Decrypt a text using Caesar cipher with the given shift."""
    return encrypt(text, -shift)


def main():
    """
    Main function of the program
    that allows the user to encrypt and decrypt text using the Caesar cipher.
    """
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        print(50*"-")
        choice = input("Enter your choice: ")
        if choice == "1":
            text = input("Enter the text: ")
            try:
                shift = int(input("Enter the shift: "))
                print("Encrypted text: " + encrypt(text, shift))
            except ValueError:
                print("Invalid shift. Please try again.")
        elif choice == "2":
            text = input("Enter the text: ")
            try:
                shift = int(input("Enter the shift: "))
                print("Decrypted text: " + decrypt(text, shift))
            except ValueError:
                print("Invalid shift. Please try again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ =="__main__":
    main()