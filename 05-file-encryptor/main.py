from cryptography.fernet import Fernet #Module for encryption


def generate_key():
    key = Fernet.generate_key()#Generate the key
    with open("secret.key","wb") as file:#Write the key, "wb" for binary
        file.write(key)#Write the key to the file

def encrypt_file(file_name):    
    with open("secret.key","rb") as key_file:  #Open the file, "rb" for binary
        key = key_file.read() #read the file
    with open(file_name,"rb") as file:#Open the file, "rb" for binary:
        fernet = Fernet(key)#Create the Fernet object
        encrypted = fernet.encrypt(file.read())#Encrypt the file
    with open (file_name,"wb") as file:#Open the file, "wb" for binary
        file.write(encrypted)#Write the encrypted file

generate_key()#Call the function  

def decrypt_file(file_name):
    with open("secret.key","rb") as key_file:#Open the file, "rb" for binary
        key = key_file.read()#read the file
    with open(file_name,"rb") as file:#Open the file, "rb" for binary
        fernet = Fernet(key)#Create the Fernet object
        decrypted = fernet.decrypt(file.read())#Decrypt the file
    with open(file_name,"wb") as file:#Open the file, "wb" for binary
        file.write(decrypted)#Write the decrypted file