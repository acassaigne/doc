******
Play 2
******

Installation
============

Télécharger play et décompresser le zip. Ensuite suivre les instructions de
cette page http://www.playframework.com/documentation/2.1.x/Installing

Sous windows mettre à jour la variable d'environnement PATH.
Cette variable doit contenir C:\play-2.1.3

Tester l'installation
=====================

Lancer la commande ::

    play.bat help

Nous devons obtenir ::

    C:\>play.bat help
           _            _
     _ __ | | __ _ _  _| |
    | '_ \| |/ _' | || |_|
    |  __/|_|\____|\__ (_)
    |_|            |__/

    play! 2.1.3 (using Java 1.7.0_25 and Scala 2.10.0), http://www.playframework.org
    Welcome to Play 2.1.3!

    These commands are available:
    -----------------------------
    license            Display licensing informations.
    new [directory]    Create a new Play application in the specified directory.

    You can also browse the complete documentation at http://www.playframework.org.

Création d'une application
==========================

Utiliser la commande ::

    play new

création du répertoire todolist contenant les répertoires suivants :
- app
- conf
- logs
- project
- public
- target
- test

- Le répertoire app contient les fichier source java (.java) avec une
  modélisation MVC
- conf contient les fichiers de configuration application.conf, routes, messages
le fichier messages est là pour i18n.
- project contient les scripts de contruction (build) basés sur sbt.
- public contient toutes les ressources publics (CSS, images...)
- test contient tous les tests qui peuvent être écrits en JUnit.

note: tous les fichiers doivent être encodés en UTF8

Lancer l'application
====================

lancer la console en utilisant la commande ::

    cd todolist
    play
    run

maintenant vous pouvez tester l'application sur le port 9000.
http://localhost:9000


Si on ouvre le fichier todolist/app/controllers/Application.java on trouve
la définition de cette méthode ::


    public class Application extends Controller {

      public static Result index() {
        return ok(index.render("Your new application is ready."));
      }

    }

Toute méthode qui doit retourner un résultat HTTP soit retouner un type Result.

Pour retourner un résultat en mode texte uniquement il suffit d'utiliser ok(String)
comme ceci ::

    public class Application extends Controller {

        public static Result index() {
            return ok("Bonjour Anthony.");
        }

    }

Ajouter des routes
==================

Exemple de routes avec un paramètre ::

    # Home page
    GET     /                       controllers.Application.index()

    # Tasks
    GET     /tasks                  controllers.Application.tasks()
    POST    /tasks                  controllers.Application.newTask()
    POST    /tasks/:id/delete       controllers.Application.deleteTask(id: Long)


Si nous demandons l'url http://localhost:9000/tasks nous obtenons une erreur de
compilation car nous n'avons pas codé les méthodes suivantes :

- controllers.Application.tasks()
- controllers.Application.newTask()
- controllers.Application.deleteTask(id: Long)

Nous pouvons utilier l'objet TODO de type Result permettant d'indiquer qu'une
implémentation future doit être réalisée.

Exemple d'utilisation ::

    public static Result tasks() {
        return TODO;
      }

Play et Eclipse
===============

Pour obtenir un projet Eclipse il faut utiliser la commande Eclispe ainsi ::

    cd todolist
    play
    eclipse

Résultat attendu ::

    [info] About to create Eclipse project files for your project(s).
    [info] Successfully created Eclipse project files for project(s):
    [info] todolist
    [todolist] $ exit
