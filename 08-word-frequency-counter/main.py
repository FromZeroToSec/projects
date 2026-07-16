def open_file (filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("Error: file not found")
        return ""









#Feuille de route — 08-word-frequency-counter Lecture fichier (en cours) : fonction qui lit un fichier texte et retourne le contenu (gestion FileNotFoundError)
#Nettoyage + split : découper le texte en mots (lowercase, ponctuation retirée)
#Comptage fréquence : dictionnaire {mot: nombre d'occurrences}
#Tri + affichage top N : afficher les mots les plus fréquents
#Main + interface CLI : demander le nom du fichier, afficher résultat, if __name__ == "__main__":