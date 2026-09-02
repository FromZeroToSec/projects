import random
import string

# Define the character pool: letters, digits, and special characters
characters = string.ascii_letters + string.digits + string.punctuation

# Ask the user for the desired password length
length = int(input("How many characters do you want in your password? "))

# Build the password by picking random characters
password = ""
for i in range(length):
    password += random.choice(characters)

# Display the generated password
print(password)