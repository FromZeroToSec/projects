from cryptography.fernet import Fernet #Module for encryption #secret.key gitignore


def generate_key():#Generate a key
    key = Fernet.generate_key()
    with open("secret.key","wb") as file:#Write the key, "wb" for binary
        file.write(key)#Write the key to the file

generate_key()#Call the function        
