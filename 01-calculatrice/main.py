# Demande les entrées à l'utilisateur
a = float(input("Enter the first number: "))
operation = input("Enter your operation (+,-,÷,x) ").lower()
b = float(input("Enter the second number: "))

# Remplace les symboles alternatifs
operation = operation.replace("÷","/").replace("x","*")

# Effectue le calcul selon l'opération choisie
if operation == "+":
   result = a + b
   
elif operation == "-":
    result = a - b

elif operation == "/":
    if b == 0:
        result = None
    else:
        result = a / b
   
elif operation == "*":
    result = a * b
else:
    result = None

# Affiche le résultat ou un message d'erreur
if result is not None:
    print(f"Result: {a} {operation} {b} = {result}")
else:
    print("Error: invalid operation or division by zero.")

   