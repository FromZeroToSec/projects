# Demande les entrées à l'utilisateur
number_1 = float(input("Enter the first number: "))
operation = input("Enter your operation (+,-,÷,x) ").lower()
number_2 = float(input("Enter the second number: "))

# Remplace les symboles alternatifs
operation = operation.replace("÷","/").replace("x","*")

# Effectue le calcul selon l'opération choisie
if operation == "+":
   result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "/":
    result = number_1 / number_2
elif operation == "*":
    result = number_1 * number_2
else:
    result = None

# Affiche le résultat ou un message d'erreur
if result is not None:
    print(f"Result: {number_1} {operation} {number_2} = {result}")
else:
    print("Error: invalid operation.")
   