from cryptography.fernet import Fernet # Module for encryption


def generate_key():
    key = Fernet.generate_key()# Generate the key
    with open("secret.key","wb") as file:# Write the key, "wb" for binary
        file.write(key)#Write the key to the file

def encrypt_file(file_name):    
    try:
        with open("secret.key","rb") as key_file:  #Open the file, "rb" for binary
            key = key_file.read() #read the file
        with open(file_name,"rb") as file:#Open the file, "rb" for binary:
            fernet = Fernet(key)#Create the Fernet object
            encrypted = fernet.encrypt(file.read())#Encrypt the file
        with open(file_name,"wb") as file:#Open the file, "wb" for binary
            file.write(encrypted)#Write the encrypted file
    except FileNotFoundError:
        print("Error: file not found")


def decrypt_file(file_name):
    try:
        with open("secret.key","rb") as key_file:#Open the file, "rb" for binary
            key = key_file.read()#read the file
        with open(file_name,"rb") as file:#Open the file, "rb" for binary
            fernet = Fernet(key)#Create the Fernet object
            decrypted = fernet.decrypt(file.read())#Decrypt the file
        with open(file_name,"wb") as file:#Open the file, "wb" for binary
            file.write(decrypted)#Write the decrypted file
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
