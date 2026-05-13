from cryptography.fernet import Fernet 


def generate_key():
    """Generates a key and saves it to a file."""
    key = Fernet.generate_key()
    with open("secret.key","wb") as file:# wb = write binary
        file.write(key)

def encrypt_file(file_name):    
    """Encrypts a file in place using Fernet."""    
    try:
        with open("secret.key","rb") as key_file:  # rb = read binary
            key = key_file.read() 
        with open(file_name,"rb") as file:
            fernet = Fernet(key)
            encrypted = fernet.encrypt(file.read())
        with open(file_name,"wb") as file:# wb = write binary
            file.write(encrypted)
    except FileNotFoundError:
        print("Error: file not found")


def decrypt_file(file_name):
    """Decrypts a file in place using Fernet."""
    try:
        with open("secret.key","rb") as key_file:# rb = read binary
            key = key_file.read()
        with open(file_name,"rb") as file:
            fernet = Fernet(key)
            decrypted = fernet.decrypt(file.read())
        with open(file_name,"wb") as file:# wb = write binary
            file.write(decrypted)
    except FileNotFoundError:
        print("Error: file not found")

def main():
    while True:
        answer = input("What do you want to do?\n1. Generate key\n2. Encrypt file\n3. Decrypt file\n4. Quit\nChoice: ")
        if answer == "1":
            generate_key()
        elif answer == "2":
            user_file = input("Enter the file path: ")
            encrypt_file(user_file)
        elif answer == "3":
            user_file = input("Enter the file path: ")
            decrypt_file(user_file)
        elif answer == "4":
            break 
        else:
            print("Invalid option")

if __name__ == "__main__": main() 
