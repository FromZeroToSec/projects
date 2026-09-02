def is_even(n):   
    return n % 2 == 0 


while True:   
    try:
        n = int(input("Entrez un nombre : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue
    

    if is_even(n):
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")

    answer = input("Voulez-vous continuer ? (o/n) ").lower() 
    if answer != "o":
        break

print("Merci d'avoir joué !") 