1. Activer l'environnement virtuel

* Windows
    ```
    .\venv\Scripts\activate
    ```

* MacOS/Linux
    ```
    source venv/bin/activate
    ```

2. Dans le répertoire du projet, installer les dépendances
    ```
    pip install -r requirements.txt
    ```

3. Créer les migrations pour la base de données et les appliquer
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
 
 4. Lancer le serveur
    ```
    python manage.py runserver
    ```