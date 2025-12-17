Interfaces de programmation
===========================

URLs de l'application
---------------------

**Application principale (oc_lettings_site)**

.. list-table::
   :header-rows: 1

   * - URL
     - Nom
     - Vue
     - Description
   * - ``/``
     - index
     - index
     - Page d'accueil
   * - ``/admin/``
     - admin
     - Django Admin
     - Interface d'administration

**Application Lettings**

.. list-table::
   :header-rows: 1

   * - URL
     - Nom
     - Vue
     - Description
   * - ``/lettings/``
     - lettings:index
     - index
     - Liste des locations
   * - ``/lettings/<id>/``
     - lettings:letting
     - letting
     - Détail d'une location

**Application Profiles**

.. list-table::
   :header-rows: 1

   * - URL
     - Nom
     - Vue
     - Description
   * - ``/profiles/``
     - profiles:index
     - index
     - Liste des profils
   * - ``/profiles/<username>/``
     - profiles:profile
     - profile
     - Détail d'un profil

Pages d'erreur personnalisées
-----------------------------

* **404** : Page non trouvée (``templates/404.html``)
* **500** : Erreur serveur (``templates/500.html``)