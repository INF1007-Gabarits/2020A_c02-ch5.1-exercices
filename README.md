[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 4)

Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md)

À moins d'indication contraires, vous devez retourner les résultats des fonctions, pas les afficher directement.

## 1. Longueur paire

Vérifier si le nombre de caractères d’une chaîne de caractères est pair.

## 2. Fréquence d'une lettre

Calculer le nombre d’occurrences d’un caractère dans une chaîne de caractères, sans utiliser de fonctions avancées.

## 3. Prénoms composés

Soit un prénom composé (avec un trait d’union) passé en paramètre (exemple « jean-luc »). Il faut extraire le premier prénom (exemple « jean » pour « jean-luc ») puis le mettre dans la phrase « Bonjour *PremierPrénom* » (exemple « Bonjour Jean »). La première lettre du prénom doit être en majuscule (même si le paramètre est en minuscule). Indice : Les chaînes de caractères possède des fonctions de recherche et de séparation.

## 4. Texte à trous

Bâtir la phrase «Aujourd’hui, j’ai vu un \<animal\> s’emparer d’un panier \<adjectif\> plein de \<fruit\>.» en sélectionnant aléatoirement l’animal, l’adjectif et le fruit à partir de ceux donnés en paramètres. Les paramètres sont trois tuples de n'importe quelle taille.

Par exemples si on a les animaux `(chevreuil, chien, pigeon)`, les adjectifs `(rouge, officiel, lourd)` et les fruits `(pommes, kiwis, bananes)`, on pourrait obtenir la phrase :
```
Aujourd’hui, j’ai vu un pigeon s’emparer d’un panier rouge plein de kiwis.
```

Pour générer des nombres aléatoires en Python, référez-vous à https://docs.python.org/3/library/random.html, spécifiquement aux fonctions pour les entiers
