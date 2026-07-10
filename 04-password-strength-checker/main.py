def check_length(password):
    return len(password) >= 8  # Password must be at least 8 characters

def check_upper(password):
    return any(c.isupper() for c in password)  # True if at least one uppercase letter found

def check_digit(password):
    return any(c.isdigit() for c in password)  # True if at least one digit found

def check_special(password):
    return any(not c.isalnum() for c in password)  # True if at least one special character found

def get_score(password):
    # Each criterion adds 1 point to the total score (max 4)
    return check_digit(password) + check_length(password) + check_special(password) + check_upper(password)

def get_strength(score):
    # Map score to strength label
    if score >= 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    elif score == 2:
        return "Weak"
    elif score == 1:
        return "Very Weak"
    else:
        return "Too Weak"

def get_feedback(password):
    missing = []
    # Check each criterion and collect missing ones
    if not check_upper(password):
        missing.append("uppercase")
    if not check_digit(password):
        missing.append("digit")
    if not check_special(password):
        missing.append("special")
    if not missing:
        return "None"
    return "Missing: " + ", ".join(missing)

def main():
    while True:  # Main loop — allows replay
        password = input("What is your password? ")
        while not check_length(password):  # Reject passwords under 8 characters
            print("Too short !")
            password = input("What is your password? ")
        score = get_score(password)
        print("Password strength: " + get_strength(score))
        print(get_feedback(password))
        again = input("Again? (y/n) ").lower()
        while again != "n" and again != "y":  # Validate user input for replay choice
            print("Invalid input")
            again = input("Again? (y/n) ").lower()
        if again == "n":
            print("Goodbye")
            break

main()