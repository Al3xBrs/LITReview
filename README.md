# LITReview

LITReview est un site de revue de livres et articles.
Un utilisateur peut demander un avis sur un ouvrage et un autre peut lui répondre en donnant une note. 
Des revues de livres/articles peuvent également être postées seule.

## Requirements

    Avant de passer à l'étape 1, vous devez avoir installer Python et Git sur votre machine. Pour savoir comment faire, dirigez vous vers leur site.

        * Python : https://www.python.org/
        * Git : https://git-scm.com/
  

# 1 - Initialiser le serveur

    * Préparer un dossier sur votre machine qui recevra le code du site.
  
    * Cloner le repository sur ce dossier en utilisant la commande 
  
        $ git clone urldurepository
  
    * Créer un environnement virtuel où est installé le fichier requirements.txt
  
        $ python -m venv env

    * Installer les modules du fichier requirements.txt
  
        $ pip install -r requirements.txt

    * Lancer le serveur en vous rendant dans le second dossier LITReview
  
        $ cd LITReview/
        $ python manage.py runserver

# 2 - Se connecter sur le site

    Une fois le serveur lancé avec l'étape 1, rendez-vous sur le site en tapant localhost:8000 (http://localhost:8000) dans la barre de recherche de votre navigateur web.

    Il existe 3 comptes disponibles comme exemple pour vous connecter :

        * pierre@gmail.com      pwd : Pierre
        * Paul@gmail.com        pwd : Paul
        * jack@gmail.com        pwd : Jack
  
# 3 - Naviguer sur le site

    En haut du site vous trouverez 5 boutons principaux.
    
        * Accueil               - Retourner sur l'accueil
        * Ticket                - Publier un ticket
        * Review                - Publier une review
        * Abonnements           - File d'abonnement
        * Photo de profil       - Profil + Se déconnecter

    Chaque utilisateur peut naviguer librement sur ces pages et peut répondre à un ticket seulement si aucune review n'a été postée sur celui-ci en cliquant sur "Publier une review" directement sur le ticket.

    Les mentions "Modifier le post" et "Supprimer le post" sont seulement accessibles pour les utilisateurs dont le post appartient.

    Une mention "Modifier mon mot de passe" est accessible sur le profil de l'utilisateur connecté seulement.