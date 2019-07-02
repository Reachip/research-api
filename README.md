Ce dépôt contient la base de code de l'API REST du projet Research.

# Installation des dépendances 

**Nota bene:** PostgreSQL doit être installé sur la machine hôte !

Créer la base de données du projet : 

```sql
CREATE DATABASE research;
```

Installer les dépendances de Python :

```bash
pip3 install --user peewee flask jwt flask_cors flask_restful psycopg
```

# Lancement

```bash
export FLASK_APP=__main__.py
flask run
```
