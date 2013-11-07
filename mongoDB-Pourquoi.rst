2 Pourquoi utiliser MongoDBi
MongoDB est un système de base de données conçu pour les applications web et les infrastructures de type internet. Le model de données et les stratégies de persistances ont été construire pour obtenir d’important débit en lecture et écriture. MongoDB a été conçu également dans l’objectif de s’adapter au niveau de charge souhaité tout en intégrant les contraintes de haute disponibilité. MongoDB peut fournir de surprenante bonne performances que ce soit en configuration mono-nœud ou multi-nœuds.
2.1 MongoDB une base document-centrique 
Au contraire du mode relationnel où les entités métiers sont stockées dans plusieurs tables, MongoDB stocke l’ensemble des informations au sein du document. Prenons l’exemple d’un CV qui composé d’un nom et prénoms ainsi que d’une série d’expériences dans un modèle relationnel nous aurions au moins deux entités l’une pour le CV et une autre pour les expériences alors qu’avec MongoDB une seul entité est créé. Le document CV pouvant contenir plusieurs « sections » expériences. Un document MongoDB  propose donc une vision hiérarchique venant remplacer la mécanique des jointures proposé au sein d’un SGBDR traditionnel.  Ce design de stockage est particulièrement bien adapté à la persistance d’une modélisation objet. Avec MongoDB  il n’est plus utile d’avoir un ORM. 
2.2 Historique
MongoDB est né en 2007 et part d’un constat que la plupart des développeurs n’étaient pas satisfait du modèle relationnel.  La startup 10gen partant de ce fait décide de concentrer ses efforts sur le développement d’un nouveau paradigme dans le domaine des bases de données. L’objectif étant   de combiner le meilleur du modèle relationnel (en termes de fonctionnalités) en s’inspirant du modèle clé-valeur en environnement distribué. Le modèle de développement est open source, le code de MongoDB est donc librement accessible sous licence GNU Affero General Public License. MongoDB a été développé en vu d’atteindre ces deux objectifs : 
- avoir une montée en charge optimal en mode cluster (scalabilité horizontale)
- avoir un format de stockage parfaitement adapté aux applications web
MongoDB est donc conçu pour obtenir une scalabilité horizontale c'est-à-dire faire face au besoin de montée en charge par l’ajout de serveurs à contrario des SGBDR traditionnels où la scalabilité est verticale et est assuré par l’augmentation de puissance du serveur hébergeant la base de données.
2.3 Réplication
MongoDB offre un mode (est-ce le seul ?) de réplication de type une base primaire (écriture/lecture) et des bases secondaires en lecture uniquement. En cas de perte de la base primaire c’est une base secondaire qui est promue automatiquement en base primaire. Lorsque l’ancienne base primaire est réactivée, elle est automatique reconfigurée en tant que base secondaire. 
2.4 Performance et persistance des données
Il s’agit toujours d’un compromis entre performance et persistance par exemple une base de données de type Memcache n’assure aucune persistance car l’intégralité des données sont stockées en RAM et propose donc d’excellentes performances. A contrario les SGBDR garantissent la persistance des données sur commit par une journalisation se réalisant sur un support de type disque dur au détriment des performances. Avec MongoDB c’est le client (l’application) qui choisi entre performance et garantie de la persistance. Si le client souhaite de la performance, il demande l’insertion de donnée en mode fire-and-forget, c'est-à-dire que l’ordre d’écriture est transmis à MongoDB sans accusé de réception. Par contre si le client souhaite une garantie de persistance il optera pour le mode safe-mode imposant un accusé de réception. L’option safe-mode est configurable,  il est ainsi possible d’imposer un nombre minimum de réplication avant qu’un accusé de réception ne soit retourné. 
2.5 Scabilité horizontale et haute disponibilité
MongoDB propose un modèle de scalabilité horizontale par partitionnement des données, c'est-à-dire que chaque nœud reçoit une partie des données (un fragment). Ce partitionnement ou fragmentation des données (auto-sharding dans la terminologie de MongoDB) est réalisé automatiquement. Pour des raisons de haute disponibilité un nœud assure également la réplication d’un autre fragment (plus exactement de deux autres fragments éliminant ainsi tout SPOF). 
3 Cas d’utilisation
Pour quels types de besoins est-il pertinent de mettre en œuvre MongoDB ? C’est ce que nous développons dans ce paragraphe.
3.1 Application web
Bien entendu il est tout à fait pertinent d’utiliser MongoDB pour un développement d’applications web. MongoDB permet le stockage de collections de documents complexes en se passant de mapping. MongoDB permettant le stockage de documents complexes, il est fort probable qu’il y aura nettement moins de collections que de tables au sein d’un SGBDR. De plus le langage d’interrogation est plus simple que le SQL et MongoDB permet l’indexation de données au même titre que les SGBDR. MongoDB propose un modèle évident de scabalité horizontale permettant aux applications web de supporter une forte charge.
3.2 Logging et analyse
MongoDB est bien adapté aux besoins de logging et dans l’analyse de ceux-ci. Quelques grandes compagnies de l’internet telles que Disqus, GitHub, Justin.tv, Electronic Arts… l’utilisent à cette fin. MongoDB répond bien à ces besoins via deux fonctionnalités clés qui sont une mise à jour atomic au niveau du document et les collections plafonnées. Les collections plafonnées permettent de définir des règles de gestion temporelle au niveau sur ces dernières. Stocker des données de type logging au sein d’une base de données comparativement au stockage sur fichiers  offre une bien meilleure organisation et plus de facilités d’interrogations.
3.3 Cache de données
MongoDB peut remplacer le classique couple MySQL/Memcache. Il est possible d’utiliser MongoDB en tant que cache de pages. 
3.4 Schémas variables
Si votre ou vos schémas de données sont fortement évolutifs alors vous pouvez tirer partie de MongoDB qui a été conçu dans cette optique. 
3.5 Prototypage
MongoDB est souple au niveau des schémas de données et facile à mettre en œuvre c’est donc un candidat idéal dans le cadre de prototypage d’applications.
4 MongoDB n’est pas adapté pour...
Si vous avez besoin de garantie transactionnelle, par exemple si vous devez développer une application bancaire. 
Si vous avez une base de code existant faisant usage du SQL ou si vous avez des opérations complexes de regroupement de collections de données. 
Si vous avez des besoins en versionning de données alors MongoDB ne sera pas adapté. 
MongoDB n’a pas de réel fonctionnalités de type recherche fulltext, les expressions régulières étant assez peu performantes. 
5 Installation et prise en main de MongoDB
5.1 Récupérer MongoDB
Télécharger la version souhaitée à cette adresse http://www.mongodb.org/downloads. 
La version 32 bits que se soit pour Linux ou Windows ne permet de gérer que 2 giga de ram, ce qui est trop peu pour une utilisation en environnement de production.
5.2 Comment installer mongoDB
Une fois le téléchargement terminé, il faut décompresser l'archive zip dans un répertoire par exemple c:\mongodb. Ensuite vous devez créer les répertoires c:\data\db qui vont stocker les données.
Pour lancer MongoDB, il faut lancer un terminal en ligne de commande (cmd.exe pour windows en tant qu'administrateur du système et un shell pour Unix) ensuite exécuter les commandes suivantes 
	cd c:\mongodb\mongodb-win32-i386-[version]
	cd bin
	mongod.exe
MongoDB est installé et opérationnel.
6 Comment utiliser MongoDB
6.1 Le client standard de MongoDB
Le shell javascript (client mongodb) fourni lors de l'installationpeut être lancé via la commande mongo. Cette commande se trouve dans le répertoire c:\mongodb\mongodb-win32-i386-[version]\bin
En lançant cette commande mongo vous devriez obtenir :
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
6.2 Quelques commandes
Pour changer de collection (base de données) utiliser la commande use :
	use ma_collection
Quel est le format de stockage des données ? Les données stockées le sont au format JSON et plus exactement BSON qui une extension du JSON.
Par exemple nous souhaitons stocker cette donnée :
		une_personne = {nom: "Cassaigne", prenom: "Anthony"}
		db.test.save(une_personne)
La commande db.test.save(une_personne) sauvegardera les données dans la collection test.
ll n'est pas nécessaire de créer de collection avant de sauvegarder une donnée.
Exemple de création de plusieurs enregistrements :
  for(i = 1; i < 21; i++) db.test.save({ nom: 'utilisateur_nr_' + i, age: i });
Comment recherche des données ?
Pour cela utiliser la commande find par exemple :
	db.test.find()
Retournera tous les enregistrements :
    { "_id" : ObjectId("51d3e9d6b9ded04db517d2f9"), "nom" : "Cassaigne", "prenom" :
      "Anthony" }
    { "_id" : ObjectId("51d3f215b9ded04db517d30e"), "nom" : "utilisateur_nr_1", "age" : 1 }
    { "_id" : ObjectId("51d3f215b9ded04db517d30f"), "nom" : "utilisateur_nr_2", "age" : 2 }
    { "_id" : ObjectId("51d3f215b9ded04db517d310"), "nom" : "utilisateur_nr_3", "age" : 3 }
    { "_id" : ObjectId("51d3f215b9ded04db517d311"), "nom" : "utilisateur_nr_4", "age" : 4 }
    { "_id" : ObjectId("51d3f215b9ded04db517d312"), "nom" : "utilisateur_nr_5", "age" : 5 }
    { "_id" : ObjectId("51d3f215b9ded04db517d313"), "nom" : "utilisateur_nr_6", "age" : 6 }
7 Quelques ressources web utiles
Pour aller plus loin en particulier sur le domaine hadoop et MongoDB :
http://fr.slideshare.net/spf13/mongodb-and-hadoop
Un tutorial correctement réalisé, de l’installation à la prise en main :
http://tuts.syrinxoon.net/tuts/installation-et-bases-de-mongodb
Les cas d’utilisation et retour d’expérience :
http://blog.xebia.fr/2010/12/15/mongodb-en-pratique/
http://blog.xebia.fr/2010/04/30/nosql-europe-bases-de-donnees-orientees-documents-et-mongodb/
Terminologie comparative avec le modèle relationnel 
http://docs.mongodb.org/manual/reference/sql-comparison/
