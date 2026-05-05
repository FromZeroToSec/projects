def check_length(password):
    return len(password) >= 8

def check_upper(password):
    return any(c.isupper() for c in password)

def check_digit(password):
    return any(c.isdigit() for c in password)

def check_special(password):
    return any(not c.isalnum() for c in password)

def get_score(password):
    return check_digit(password) + check_length(password) + check_special(password) + check_upper(password)

def get_strength(score): 
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

def main():
    while True:
        password = input("What is your password? ")
        while not check_length(password):
            print("Too short !")
            password = input("What is your password? ")
        score = get_score(password)
        print("Password strength: " + get_strength(score))
        print(get_feedback(password))
        again = input("Again? (y/n) ").lower()
        while again != "n" and again != "y":
            print("Invalid input")
            again = input("Again? (y/n) ").lower()
        if again == "n":
            print("Goodbye")
            break
        

def get_feedback(password):
    missing = []
    if not check_upper(password):
        missing.append("uppercase")
    if not check_digit(password):
        missing.append("digit")
    if not check_special(password):
        missing.append("special")   
    return "Missing: " + ", ".join(missing)
    
main()