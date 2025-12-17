Procédures de déploiement
=========================

Architecture de déploiement
---------------------------

Le déploiement utilise un pipeline CI/CD avec GitHub Actions :

1. **Build & Test** : À chaque push, le code est testé (flake8 + pytest)
2. **Conteneurisation** : Si les tests passent et que c'est la branche ``master``, une image Docker est construite et poussée sur Docker Hub
3. **Déploiement** : L'image est automatiquement déployée sur Render

Configuration requise
---------------------

Secrets GitHub
^^^^^^^^^^^^^^

Configurer dans : Settings → Secrets → Actions

.. list-table::
   :header-rows: 1

   * - Secret
     - Description
   * - DOCKER_USERNAME
     - Nom d'utilisateur Docker Hub
   * - DOCKER_PASSWORD
     - Mot de passe Docker Hub
   * - RENDER_DEPLOY_HOOK
     - URL du Deploy Hook Render

Variables d'environnement Render
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Variable
     - Valeur
   * - SECRET_KEY
     - Clé secrète Django
   * - DEBUG
     - False
   * - SENTRY_DSN
     - DSN Sentry
   * - ALLOWED_HOSTS
     - .onrender.com

Étapes de déploiement
---------------------

Déploiement automatique
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   git add .
   git commit -m "Votre message"
   git push origin master

Le pipeline CI/CD se déclenche automatiquement.

Lancer avec Docker localement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker pull adr1e/oc-lettings:latest
   docker run -d -p 8000:8000 -e SECRET_KEY='your-key' -e DEBUG='True' -e SENTRY_DSN='' adr1e/oc-lettings:latest

Accéder au site : http://127.0.0.1:8000/

Monitoring avec Sentry
----------------------

Les erreurs sont automatiquement capturées et envoyées à Sentry.

Configuration :

1. Créer un compte sur https://sentry.io
2. Créer un projet Django
3. Récupérer le DSN
4. Ajouter le DSN dans les variables d'environnement

Liens utiles
------------

* Site en production : https://oc-lettings-h475.onrender.com
* Docker Hub : https://hub.docker.com/r/adr1e/oc-lettings
* GitHub Actions : https://github.com/Adr1e/Mettez-l-chelle-une-application-Django-en-utilisant-une-architecture-modulaire/actions