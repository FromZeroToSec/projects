import hashlib

# Variable stored 
USERNAME = "mehdi"
PASSWORD_HASH = "6b45bad95dcfac6d300d431f153be6e7fe6286b3ae0484bd374b6f300214b0d8"
EXIT = "exit"

# Attempt counter and maximum attempts
attempts = 0
max_attempts = 3

# Loop allowing 3 attempts maximum
while attempts < max_attempts:
    username = input("Exit to quit. \nEnter your username : ").lower()
    
    # Check if user wants to exit
    if username == EXIT:
        print("Exiting...")
        break

    password = input("Exit to quit. \nEnter your password :")
    
    # Check if user wants to exit
    if password == EXIT:
        print("Exiting...")
        break

    # Verify 
    if username == USERNAME and hashlib.sha256(password.encode()).hexdigest() == PASSWORD_HASH:
        print("Access Authorized")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print("Access denied")
        print(f"Remaining attempts: {remaining}")

# Message displayed if all attempts are exhausted
else:
    print("ACCOUNT LOCKED")