#Variable Identifiant et mot de passe
USERNAME = "mehdi"
PASSWORD = "MotDePasseTest123"

# Initialisation du compteur et du maximum de tentatives
attempts = 0
max_attempts = 3

# Boucle qui autorise 3 essais maximum
while attempts < max_attempts:
    username = input("Enter your username: ").lower()
    password = input("Enter your password: ")

# Vérification des identifiants (toujours en clair pour l'instant)
    if username == USERNAME and password == PASSWORD:
        print("Access Authorized")
        break
    else:
        print("Access denied")
        attempts += 1

# Affichage du décompte des tentatives restantes  
        remaining = max_attempts - attempts
        print(f"Remaining attempts: {remaining}")

# Message affiché si les 3 tentatives sont épuisées
else:
    print("ACCOUNT LOCKED")