Base de données et modèles
==========================

Le projet utilise SQLite3 comme base de données.

Schéma de la base de données
----------------------------

L'application contient trois modèles principaux répartis dans deux applications.

Application Lettings
--------------------

**Modèle Address**

Représente une adresse postale.

.. list-table::
   :header-rows: 1

   * - Champ
     - Type
     - Description
   * - id
     - Integer (PK)
     - Identifiant unique
   * - number
     - Integer
     - Numéro de rue
   * - street
     - CharField(64)
     - Nom de la rue
   * - city
     - CharField(64)
     - Ville
   * - state
     - CharField(2)
     - État (code 2 lettres)
   * - zip_code
     - Integer
     - Code postal
   * - country_iso_code
     - CharField(3)
     - Code ISO du pays

**Modèle Letting**

Représente une location immobilière.

.. list-table::
   :header-rows: 1

   * - Champ
     - Type
     - Description
   * - id
     - Integer (PK)
     - Identifiant unique
   * - title
     - CharField(256)
     - Titre de la location
   * - address
     - OneToOneField
     - Relation vers Address

Application Profiles
--------------------

**Modèle Profile**

Représente un profil utilisateur.

.. list-table::
   :header-rows: 1

   * - Champ
     - Type
     - Description
   * - id
     - Integer (PK)
     - Identifiant unique
   * - user
     - OneToOneField
     - Relation vers User (Django)
   * - favorite_city
     - CharField(64)
     - Ville favorite

Accéder à la base de données
----------------------------

.. code-block:: bash

   sqlite3 oc-lettings-site.sqlite3

Commandes utiles :

.. code-block:: sql

   .tables                           -- Lister les tables
   .schema lettings_address          -- Voir la structure
   SELECT * FROM lettings_letting;   -- Requête exemple
   .quit                             -- Quitter