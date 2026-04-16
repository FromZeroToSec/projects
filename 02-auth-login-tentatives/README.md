# Auth Login Tentatives

Système d'authentification en ligne de commande avec tentatives limitées — Python débutant.

## Fonctionnalités
- **3 tentatives maximum** : L'utilisateur a trois chances pour se connecter.
- **Décompte en temps réel** : Affiche le nombre d'essais restants après chaque erreur.
- **Compte bloqué** : Accès verrouillé après 3 échecs consécutifs.
- **Identifiant flexible** : Insensible à la casse (majuscules/minuscules).
- **Option de sortie** : Taper `exit` au username ou password quitte le programme proprement.

## Installation & Usage
```bash
git clone https://github.com/FromZeroToSec/02-auth-login-tentatives
cd 02-auth-login-tentatives
python main.py
```

## Concepts utilisés
- **Boucle while/else** : Gestion des essais et blocage final.
- **Conditions if/else** : Vérification des identifiants.
- **Constantes** : Credentials stockés en haut du fichier, séparés de la logique.
- **F-strings** : Affichage dynamique des tentatives restantes.
- **Input utilisateur** : Récupération et nettoyage des données (`.lower()`).