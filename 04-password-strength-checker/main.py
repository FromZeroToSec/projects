



def check_length(password):
    return len(password) >= 8

def check_upper(password):
    return any(c.isupper() for c in password)

def check_digit(password):
    return any(c.isdigit() for c in password)

def check_special(password):
    return any(not c.isalnum() for c in password)

def get_score(password):
    return check_digit(password)+check_length(password)+check_special(password)+check_upper(password)

def get_strength(score): 
    if score >= 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    elif score == 2:
        return "Weak"
    elif score == 1:
        return "Very Weak"
    else: return "Too Weak"

def main ():
    password = input("What is your password? ")
    score = get_score(password)
    print("Password strength: " + get_strength(score))

main()