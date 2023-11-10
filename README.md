# ue19_labo09-10

BUT : app.py interroge le service PunAPI pour afficher des jeux de mots. Il utilise la bibliothèque `requests` pour effectuer des requêtes HTTP

1. Clonage du depot sur le pc :

    ```bash
    git clone https://github.com/VotreNom/ue19_labo09-10.git
    cd ue19_labo09-10
    ```

2. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Comment Exécuter

- Exécutez le programme Python :

    ```bash
    python app.py
    ```

- Suivez les instructions pour entrer le nombre de jeux de mots et la catégorie souhaités.

## Docker

- Vous pouvez également exécuter l'application dans un conteneur Docker :

    ```bash
    docker build -t punapi-app .
    docker run punapi-app
    ```

## Configuration

- Ajustez le fichier `app.py` pour personnaliser le comportement de l'application selon vos besoins.

## Contribuer

Si vous souhaitez contribuer à ce projet, n'hésitez pas à ouvrir une demande de tirage (pull request) !

