def add(a,b):
    return a + b 
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    
# Boucle principale
while True:
    
    # Demande les entrées
    a = input("Enter the first number: ")
    operation = input("Enter your operation (+,-,÷,x): ").lower()
    b = input("Enter the second number: ")

    # Validation des entrées
    if not (a.isdigit() and b.isdigit()):
        print("Invalid number. Please enter valid numbers.")
    else:
        # Remplace les symboles alternatifs
        operation = operation.replace("÷", "/").replace("x", "*")

        # Effectue le calcul
        if operation == "+":
            result = add(int(a), int(b))

        elif operation == "-":
            result = subtract(int(a), int(b))

        elif operation == "/":
            result = divide(int(a), int(b))

        elif operation == "*":
            result = multiply(int(a) , int(b))
        else:
            result = None

    # Affiche le résultat
        if result is not None:
            print(f"Result: {a} {operation} {b} = {result}")
        else:
            print("Error: division by zero or invalid operation.")
    # Continuer ?
        again = input("Again? (y/n): ").lower()
        if again == "n":
            break
        print("-" * 50)