# APIavocadoBACK

## Description

Cette partie du projet contient l'API Flask utilisée pour prédire le prix des avocats et fournir les données nécessaires au front-end. Le back-end gère également une route pour afficher les données d'un fichier CSV au format JSON.

---

## Prérequis

Assurez-vous que les outils suivants sont installés sur votre système :

- [Python 3.8+](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [Pandas](https://pandas.pydata.org/)

---

## Installation

1. Clonez le projet :
   ```bash
   git clone https://github.com/<votre-utilisateur-github>/APIavocado.git
   ```
   
   ```bash
   cd APIavocado/APIavocadoBACK
   ```
   
Installez les dépendances Python :

```bash
pip install -r requirements.txt
```
Placez le fichier avocado.csv à la racine du répertoire APIavocadoBACK.

Utilisation
Démarrez le serveur Flask :

```bash
python app.py
```

Par défaut, l'API est accessible à l'adresse suivante :

```bash
http://127.0.0.1:5000/
```

Routes disponibles :

```bash
GET /: Affiche une page d'accueil avec un lien vers les données CSV.
```

```bash
GET /csv: Renvoie les données du fichier avocado.csv au format JSON.
```