Installation du projet
======================

Prérequis
---------

* Python 3.11 ou supérieur
* Git
* SQLite3
* Docker (optionnel, pour le déploiement)

Cloner le repository
--------------------

.. code-block:: bash

   git clone https://github.com/Adr1e/Mettez-l-chelle-une-application-Django-en-utilisant-une-architecture-modulaire.git
   cd Mettez-l-chelle-une-application-Django-en-utilisant-une-architecture-modulaire

Créer l'environnement virtuel
-----------------------------

**macOS / Linux :**

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate

**Windows (PowerShell) :**

.. code-block:: powershell

   python -m venv venv
   .\venv\Scripts\Activate.ps1

Installer les dépendances
-------------------------

.. code-block:: bash

   pip install -r requirements.txt

Configurer les variables d'environnement
----------------------------------------

Créer un fichier ``.env`` à la racine du projet :

.. code-block:: text

   SECRET_KEY=votre-clé-secrète
   DEBUG=True
   SENTRY_DSN=votre-dsn-sentry

Appliquer les migrations
------------------------

.. code-block:: bash

   python manage.py migrate