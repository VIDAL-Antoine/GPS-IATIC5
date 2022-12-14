# Mini-GPS
Projet individuel réalisé en IATIC5. 

À partir d'une carte de la France, l'objectif est de construire un GPS : à partir d'une position initiale, l'utilisateur souhaite se rendre à une ville. Toutefois, le principe consiste à choisir le trajet qui convient le mieux à l'utilisateur : ici cela sera le plus court chemin. Une autre option a été considérée : le nombre de villes parcourues.

La France sera représenté ici sous forme de graphe / tableau contenu dans un fichier csv qui représentera la matrice d'adjacence (préalablement remplie). L'entièreté de la France ne sera pas représenté pour des contraintes de stockage, nous nous limiterons donc à quelques dizaines de villes.

L'algorithme appliqué pour trouver le plus court chemin sera l'algorithme de Dijkstra.

À chaque ville atteinte (dans notre graphe un sommet), il sera possible de choisir la prochaine destination. Si celle-ci ne correspond pas à celle indiquée par le GPS, le GPS devra recalculer le plus court chemin.


## Informations d'utilisation

L'application utilise des fichiers externes, principalement une image et des fichiers csv. Les noms de ces fichiers ne peuvent pas être changés.

### Pré-requis

L'application a été testée sur Windows 10 et Linux (Ubuntu 22.04). 
L'application fonctionnnant sous Python 3, il est nécessaire de l'avoir installé pour que celle-ci se lance.

Liste des librairies Python à installer pour utiliser l'application (avec la commande permettant l'installation):
- tkinter : `pip3 install tk`
- pandas : `pip3 install pandas`
- Networkx : `pip3 install networkx`
- Matplotlib : `pip3 install matplotlib`
- Pillow : `pip3 install Pillow`

## Démarrage

Pour démarrer l'application, il suffit simplement de se rendre dans le dossier `src` puis de lancer la commande `python main.py` ou `pythonw main.py` (pour Windows).

## Outils utilisés lors de la conception de l'application
- Visual Studio Code et VIM pour l'édition de texte
- Microsoft Office Excel pour l'édition des fichiers csv
- Git et Github pour le versioning et l'hébergement des fichiers
- Paint pour l'édition des images permettant d'élaborer la carte de la France utilisée par l'application
- Overleaf (et donc LaTeX) pour la rédaction des documents (rapport et soutenance)

## Auteurs
- VIDAL Antoine
- MANOUSSAKIS George en tant que tuteur
- PILARD Laurence en tant que référent

