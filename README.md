1. Cloner ce projet

1. Se déplacer dans le répertoire du projet
    ```
    cd e5-demo
    ```

1. Créer un environnement virtuel dans le répertoire parent du projet
    * Windows
    ```
    python -m venv ..\venv
    ```
    * Linux/macOS
    ```
    python -m venv ../venv
    ```

1. Activer l'environnement virtuel

    * Windows
    ```
    ..\venv\Scripts\activate
    ```
    * Linux/macOS
    ```
    source ../venv/bin/activate
    ```

1. Installer les dépendances
    ```
    pip install -r requirements.txt
    ```

1. Appliquer les migrations existantes
    ```
    python manage.py migrate
    ```
 
 1. Lancer le serveur
    ```
    python manage.py runserver
    ```