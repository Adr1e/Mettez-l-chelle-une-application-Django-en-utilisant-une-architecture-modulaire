# Orange County Lettings

Site web d'Orange County Lettings - Application Django de gestion de locations immobilières.

## Description du projet

Orange County Lettings est une application web permettant de gérer des locations immobilières et des profils utilisateurs. Le projet a été refactorisé pour adopter une architecture modulaire avec trois applications Django distinctes :

- **oc_lettings_site** : Application principale (page d'accueil, configuration)
- **lettings** : Gestion des locations (modèles Address et Letting)
- **profiles** : Gestion des profils utilisateurs (modèle Profile)

## Technologies utilisées

- Python 3.11
- Django 4.2
- SQLite3
- Docker
- GitHub Actions (CI/CD)
- Render (hébergement)
- Sentry (monitoring)
- WhiteNoise (fichiers statiques)

## Installation locale

### Prérequis

- Python 3.11 ou supérieur
- Git
- Docker (optionnel)

### Cloner le repository
```bash
git clone https://github.com/Adr1e/Mettez-l-chelle-une-application-Django-en-utilisant-une-architecture-modulaire.git
cd Mettez-l-chelle-une-application-Django-en-utilisant-une-architecture-modulaire
```

### Créer l'environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
.\venv\Scripts\Activate.ps1  # Windows PowerShell
```

### Installer les dépendances
```bash
pip install -r requirements.txt
```

### Configurer les variables d'environnement

Créer un fichier `.env` à la racine du projet :
```
SECRET_KEY=votre-clé-secrète
DEBUG=True
SENTRY_DSN=votre-dsn-sentry
```

### Lancer le serveur
```bash
python manage.py runserver
```

Accéder au site : http://127.0.0.1:8000/

## Linting et Tests

### Exécuter flake8
```bash
flake8
```

### Exécuter les tests avec couverture
```bash
pytest --cov=. --cov-report=term-missing
```

La couverture de tests est actuellement de **89%** (supérieure aux 80% requis).

## Base de données

### Accéder à la base de données SQLite
```bash
sqlite3 oc-lettings-site.sqlite3
```

### Commandes utiles
```sql
.tables                           -- Afficher les tables
.schema lettings_address          -- Voir la structure d'une table
SELECT * FROM lettings_letting;   -- Requête exemple
.quit                             -- Quitter
```

## Panel d'administration

- URL : http://127.0.0.1:8000/admin/
- Utilisateur : `admin`
- Mot de passe : `Abc1234!`

## Déploiement

### Récapitulatif du fonctionnement

Le déploiement utilise un pipeline CI/CD avec GitHub Actions :

1. **Build & Test** : À chaque push, le code est testé (flake8 + pytest)
2. **Conteneurisation** : Si les tests passent et que c'est la branche `master`, une image Docker est construite et poussée sur Docker Hub
3. **Déploiement** : L'image est automatiquement déployée sur Render

### Configuration requise

#### Secrets GitHub (Settings → Secrets → Actions)

| Secret | Description |
|--------|-------------|
| `DOCKER_USERNAME` | Nom d'utilisateur Docker Hub |
| `DOCKER_PASSWORD` | Mot de passe Docker Hub |
| `RENDER_DEPLOY_HOOK` | URL du Deploy Hook Render |

#### Variables d'environnement Render

| Variable | Valeur |
|----------|--------|
| `SECRET_KEY` | Clé secrète Django |
| `DEBUG` | `False` |
| `SENTRY_DSN` | DSN Sentry |
| `ALLOWED_HOSTS` | `.onrender.com` |

### Étapes pour déployer

1. **Push sur master** :
```bash
   git add .
   git commit -m "Votre message"
   git push origin master
```

2. **Le pipeline CI/CD se déclenche automatiquement** :
   - Tests et linting
   - Construction de l'image Docker
   - Push sur Docker Hub
   - Déploiement sur Render

3. **Vérifier le déploiement** :
   - GitHub Actions : https://github.com/Adr1e/Mettez-l-chelle-une-application-Django-en-utilisant-une-architecture-modulaire/actions
   - Site en production : https://oc-lettings-h475.onrender.com

### Lancer le site avec Docker localement
```bash
docker pull adr1e/oc-lettings:latest
docker run -d -p 8000:8000 -e SECRET_KEY='your-secret-key' -e DEBUG='False' -e SENTRY_DSN='' adr1e/oc-lettings:latest
```

Accéder au site : http://127.0.0.1:8000/

## Monitoring avec Sentry

Les erreurs de l'application sont automatiquement capturées et envoyées à Sentry. Pour configurer Sentry :

1. Créer un compte sur https://sentry.io
2. Créer un projet Django
3. Récupérer le DSN
4. Ajouter le DSN dans les variables d'environnement

## Structure du projet
```
├── lettings/                 # Application des locations
│   ├── models.py            # Modèles Address et Letting
│   ├── views.py             # Vues des locations
│   ├── urls.py              # URLs avec namespace 'lettings'
│   └── templates/lettings/  # Templates des locations
├── profiles/                 # Application des profils
│   ├── models.py            # Modèle Profile
│   ├── views.py             # Vues des profils
│   ├── urls.py              # URLs avec namespace 'profiles'
│   └── templates/profiles/  # Templates des profils
├── oc_lettings_site/        # Application principale
│   ├── settings.py          # Configuration Django
│   ├── urls.py              # URLs racine
│   └── views.py             # Vue index + erreurs 404/500
├── templates/               # Templates globaux
│   ├── base.html
│   ├── index.html
│   ├── 404.html
│   └── 500.html
├── static/                  # Fichiers statiques
├── .github/workflows/       # Pipeline CI/CD
│   └── ci-cd.yml
├── Dockerfile               # Configuration Docker
├── requirements.txt         # Dépendances Python
└── .env                     # Variables d'environnement (non versionné)
```

## Liens utiles

- **Site en production** : https://oc-lettings-h475.onrender.com
- **Docker Hub** : https://hub.docker.com/r/adr1e/oc-lettings
- **GitHub Actions** : https://github.com/Adr1e/Mettez-l-chelle-une-application-Django-en-utilisant-une-architecture-modulaire/actions