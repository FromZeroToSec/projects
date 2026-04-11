tentatives = 0
while tentatives < 3:
    utilisateur = input("Entrez votre identifiant ").lower()
    password = input("Entrez votre mot de passe ")

    if utilisateur == "mehdi" and password == "MotDePasseTest123": # TODO : ne jamais stocker un mot de passe en clair — à hasher en production
        print("Accès autorisé")
        break
    else:
        print("Accès refusé")
        tentatives += 1

else:
    print("COMPTE BLOQUÉ")