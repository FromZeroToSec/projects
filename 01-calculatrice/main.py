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
            result = int(a) + int(b)
        elif operation == "-":
            result = int(a) - int(b)
        elif operation == "/":
            if int(b) == 0:
                result = None
                print("Error: division by zero.")
            else:
                result = int(a) / int(b)
        elif operation == "*":
            result = int(a) * int(b)
        else:
            result = None

        # Affiche le résultat
        if result is not None:
            print(f"Result: {a} {operation} {b} = {result}")
        else:
            print("Error: invalid operation.")

        # Continuer ?
        again = input("Again? (y/n): ").lower()
        if again == "n":
            break