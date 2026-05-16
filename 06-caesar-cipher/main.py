def encrypt(text, shift):
    """Encrypt a text using Caesar cipher with the given shift."""
    result = ""
    for letter in text:
        if letter.isupper():
            result +=chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        elif letter.islower():
            result += chr((ord(letter) - ord('a') + shift) % 26 + ord('a')) 
        else:
            result += letter    
    return result      


def decrypt(text, shift):
    """Decrypt a text using Caesar cipher with the given shift."""
    return encrypt(text, -shift)