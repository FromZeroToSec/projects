def encrypt(text,shift):
    result = ""
    for letter in text:
        if letter.isupper():
            result +=chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        elif letter.islower():
            result += chr((ord(letter) - ord('a') + shift) % 26 + ord('a')) 
        else:
            result += letter    
    return result      
print(encrypt("Hello World!", 3))