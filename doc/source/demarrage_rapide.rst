Guide de démarrage rapide
=========================

Lancer le serveur de développement
----------------------------------

.. code-block:: bash

   source venv/bin/activate
   python manage.py runserver

Accéder au site : http://127.0.0.1:8000/

Panel d'administration
----------------------

* URL : http://127.0.0.1:8000/admin/
* Utilisateur : ``admin``
* Mot de passe : ``Abc1234!``

Exécuter les tests
------------------

.. code-block:: bash

   pytest --cov=. --cov-report=term-missing

Exécuter le linting
-------------------

.. code-block:: bash

   flake8