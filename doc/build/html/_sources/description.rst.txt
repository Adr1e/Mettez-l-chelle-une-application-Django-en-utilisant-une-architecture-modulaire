Description du projet
=====================

Orange County Lettings est une application web de gestion de locations immobilières.

Objectif
--------

L'application permet de :

* Gérer un catalogue de locations immobilières (Lettings)
* Gérer des profils utilisateurs (Profiles)
* Administrer les données via l'interface Django Admin

Architecture
------------

Le projet a été refactorisé pour adopter une architecture modulaire avec trois applications Django distinctes :

* **oc_lettings_site** : Application principale contenant la configuration, la page d'accueil et les pages d'erreur personnalisées (404, 500)
* **lettings** : Gestion des locations avec les modèles Address et Letting
* **profiles** : Gestion des profils utilisateurs avec le modèle Profile

Cette architecture modulaire améliore :

* La maintenabilité du code
* La séparation des responsabilités
* La réutilisabilité des composants
* La testabilité de l'application