import sys
import json

try:
    file = open("tasks.json", "r")#ouverture du fichier
    tasks = json.load(file)#chargement du fichier
    file.close()
    print("The file has been loaded.")
except FileNotFoundError:#fichier n'existe pas
    tasks = []#creation du fichier
    print("The file does not exist. It will be created.")
except json.JSONDecodeError:  # fichier existe mais vide/corrompu
    tasks = []#creation du fichier
    print("The file is empty or corrupted. It will be created.")