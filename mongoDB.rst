*******
mongoDB
*******


Installation
============

Télécharger la version souhaité à cette adresse http://www.mongodb.org/downloads.

.. note:: la version 32 bits que se soit pour Linux ou Windows ne permet de gérer que 2 giga de ram, ce qui est trop peu pour une utilisation en environnement de production.

Comment installer mongoDB
-------------------------

Une fois le téléchargement terminé, il faut décompresser l'archive zip dans ``c:\mongodb``.
Ensuite vous devez créer les répertoires ``c:\data\db`` ::

	mkdir c:\data
	mkdir c:\data\db

Pour lancer mongodb, il faut lancer un terminal en ligne de commande (cmd.exe pour windows en tant qu'administrateur du système et un shell pour Unix) ensuite exécuter les commmandes suivantes ::

	cd c:\mongodb\mongodb-win32-i386-[version]
	cd bin
	mongod.exe

Voila vous avez un environnement prêt à être utilisé.

.. note:: mondodb sauvegarde ses données dans c:\data\db ou /data/db (sous unix)
          si vous souhaitez sauvegarder vos données ailleurs c'est possible :hidden:
          utilisant le paramètre --dbpath

Démarrer mongodb en précisant un répertoire de stocake spécifique ::

    mongod --dbpath /home/user/mongodb_data

Comment utiliser mongoDB
========================

Le shell javascript (client mongodb) fourni lors de l'installation de mongoDB peut être lancé via la commande ``mongo``
Cette commande se trouve dans le répertoire ``c:\mongodb\mongodb-win32-i386-[version]\bin``

En lançant cette commande ``mongo`` vous devriez obtenir ::
MongoDB shell version: 2.4.4
connecting to: test
Server has startup warnings:
Wed Jul 03 10:01:12.115 [initandlisten]
Wed Jul 03 10:01:12.116 [initandlisten] ** NOTE: This is a 32 bit MongoDB binary.
Wed Jul 03 10:01:12.116 [initandlisten] **       32 bit builds are limited to less than 2GB of data (or less with --journal).
Wed Jul 03 10:01:12.117 [initandlisten] **       Note that journaling defaults to off for 32 bit and is currently off.
Wed Jul 03 10:01:12.117 [initandlisten] **       See http://dochub.mongodb.org/core/32bit
Wed Jul 03 10:01:12.118 [initandlisten]

Ce client utilise javascript, les commandes sont donc constitués d'instructions javascript.

Quelques commandes
==================

Pour changer de collection (base de données) utiliser la commande ``use`` ::

	use ma_collection

Comment sauvegarder une donnée ?
Les données stockées le sont au format JSON et plus exactement BSON qui une extension du JSON.
Par exemple nous souhaitons stocker cette donnée ::

		une_personne = {nom: "Cassaigne", prenom: "Anthony"}
		db.test.save(une_personne)

La commande ``db.test.save(une_personne)`` sauvegardera les données dans la collection ``test``.

.. note:: il n'est pas nécessaire de creer de collection avant de sauvegarder une donnée.

Exemple de création de plusieurs enregistrements ::

  for(i = 1; i < 21; i++) db.test.save({ nom: 'utilisateur_nr_' + i, age: i });

Comment recherche des données ?

pour cela utiliser la commande ``find`` par exemple ::

	db.test.find()

retournera tous les enregistrements ::

	{ "_id" : ObjectId("51d3e9d6b9ded04db517d2f9"), "nom" : "Cassaigne", "prenom" : "Anthony" }
    { "_id" : ObjectId("51d3f215b9ded04db517d30e"), "nom" : "utilisateur_nr_1", "age" : 1 }
    { "_id" : ObjectId("51d3f215b9ded04db517d30f"), "nom" : "utilisateur_nr_2", "age" : 2 }
    { "_id" : ObjectId("51d3f215b9ded04db517d310"), "nom" : "utilisateur_nr_3", "age" : 3 }
    { "_id" : ObjectId("51d3f215b9ded04db517d311"), "nom" : "utilisateur_nr_4", "age" : 4 }
    { "_id" : ObjectId("51d3f215b9ded04db517d312"), "nom" : "utilisateur_nr_5", "age" : 5 }
    { "_id" : ObjectId("51d3f215b9ded04db517d313"), "nom" : "utilisateur_nr_6", "age" : 6 }

Utiliser la recherche de type full text
=======================================

C'est une nouveauté de la version 2.4. Pour cela il faut commmencer par activer
l'option sur la ligne de commande de mongod ::

   mongod --setParameter textSearchEnabled=true

Ensuite il faut créer un index spécifique de cette façon ::

   db.tech_skill.ensureIndex({ label: "text"}, {default_language: "french"})

Avec cette commande nous créons un index de type full text sur l'attribut label
de la collection tech_skill en précisant qu'il s'agit d'un contenu en langue
française.

Pour lancer une recherche il faut lancer ce type de commande ::

  db.tech_skill.runCommand("text", { search:"java"})

Ici nous recherchons tout document ayant le mot java dans l'attribut label de
la collection tech_skill. La recherche est indiférente aux minuscules et
majuscules (case insensitive).

Le résultat est quelque chose de ce type ::

          {
                  "score" : 1,
                  "obj" : {
                          "_id" : ObjectId("51e4fc71b9ec6027e20fb435"),
                          "level" : 3,
                          "id_people" : ObjectId("51e4fc71b9ec6027e20fb434"),
                          "label" : "Java"
                  }
          },
          {
                  "score" : 0.625,
                  "obj" : {
                          "_id" : ObjectId("51e4fb56b9ec6027224a52ce"),
                          "level" : 2,
                          "id_people" : ObjectId("51e4fb56b9ec6027224a52cb"),
                          "label" : "Java,    SQL, scripts Shell"
                  }
          }
  ],
  "stats" : {
          "nscanned" : 4,
          "nscannedObjects" : 0,
          "n" : 4,
          "nfound" : 4,
          "timeMicros" : 11434
  },
  "ok" : 1

Exporter et import des données
==============================

Pour exporter
-------------

La commande permettant d'exporter en JSON ou CSV est mongoexport ::

  mongoexport --db test --collection people -out export_people.json

Cette commande va produire un fichier export_people.json contenant les données
de la collection people au format JSON depuis la base locale test. Le résultat
attendu est un message de ce type ::

  connected to: 127.0.0.1
  exported 86 records

Pour importer
-------------

La commande permettant d'importer la collection people du fichier
export_people.json dans la base test est ::

  mongoimport --drop --db test --collection people --file export_people.json

L'option --drop permet de supprimer la collection people pré-existante.

Python et mongodb
=================

Full text search
----------------

Pour utiliser la recherche full text avec pymongo c'est simple, il suffit
d'utiliser cette API ::

   import pymongo

   client = pymongo.MongoClient()
   db = client.test
   res = db.command("text", "tech_skill", search="java")
   print res

Url utiles
==========

Informations utiles :

Drivers
-------

L'url a connaitre est http://api.mongodb.org/ 

Installation sous windows
-------------------------

voir http://docs.mongodb.org/manual/tutorial/install-mongodb-on-windows/

Cas d'utilisation
-----------------

- http://blog.xebia.fr/2010/12/15/mongodb-en-pratique/
- http://blog.xebia.fr/2010/04/30/nosql-europe-bases-de-donnees-orientees-documents-et-mongodb/

Tutorial & Installation
-----------------------

- http://tuts.syrinxoon.net/tuts/installation-et-bases-de-mongodb
-

A trier
http://www.cloudbees.com/platform/pricing/ecosystem.cb
http://blogs.forrester.com/james_staten/13-06-14-forrester_wave_public_cloud_platforms_the_winner_is
https://mongolab.com/products/pricing/

SOLR et mongodb
http://derickrethans.nl/mongodb-and-solr.html
http://blog.knuthaugen.no/2010/04/cooking-with-mongodb-and-solr.html


hébergement
===========

Hébergement
https://mongolab.com/products/pricing/
https://www.mongohq.com/pricing
http://blogs.forrester.com/james_staten/13-06-14-forrester_wave_public_cloud_platforms_the_winner_is
 infrastructure-as-a-service (IaaS) or platform-as-a-service (PaaS)
http://www.cloudbees.com/platform-service-mongohq.cb
Tutorial :
http://tuts.syrinxoon.net/tuts/installation-et-bases-de-mongodb
Livres
http://stackoverflow.com/questions/5148994/best-mongodb-book
I'd recommend only ebooks, that give free updates at this stage, since the API etc is changing very fast.
The web is your best bet imho:
http://www.mongodb.org/display/DOCS/Home
http://mongotips.com/


Quelques comparaisons
http://sgbd.arbinada.com/node/69
Introduction intéressante
http://blog.xebia.fr/2010/12/15/mongodb-en-pratique/

MongoDB et SOLR
http://loutilities.wordpress.com/2012/11/26/complementing-mongodb-with-real-time-solr-search/
http://blog.knuthaugen.no/2010/04/cooking-with-mongodb-and-solr.html


Data modeling en MongoDB
http://docs.mongodb.org/manual/core/data-modeling/
ici voir section Data Modeling Patterns and Examples
http://docs.mongodb.org/manual/core/data-modeling/#data-modeling-examples


Définition de Collection
collection
Collections are groupings of BSON documents. Collections do not enforce a schema, but they are otherwise mostly analogous to RDBMS tables.

The documents within a collection may not need the exact same set of fields, but typically all documents in a collection have a similar or related purpose for an application.

All collections exist within a single database. The namespace within a database for collections are flat.

See What is a namespace in MongoDB? and BSON Documents for more information.

Référence
=========
http://docs.mongodb.org/manual/reference/database-references/
http://www.mongodb.org/about/production-deployments/

Avis contraires
===============
http://www.tuicool.com/articles/RjAZra
http://www.borntosegfault.com/2013/03/is-mongodb-still-on-course.html
http://nosql.mypopescu.com/post/42524689600/mongodb-is-still-broken-by-design-5-0

Retour expérience
=================
http://www.ze-technology.com/2010/07/23/retour-dexperience-sur-mongodb/

Autre Cassandra et twitter
==========================
https://blog.twitter.com/2010/cassandra-twitter-today


Introduction NoSQL
==================
http://dev.af83.com/2010/04/12/nosql-et-aprs.html
