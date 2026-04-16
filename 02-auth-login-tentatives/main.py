# Variable stored 
USERNAME = "mehdi"
PASSWORD = "MotDePasseTest123"
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
    if username == USERNAME and password == PASSWORD:
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