************
Transact-SQL
************

Quelques notions du langage
===========================

Obtenir le nombre de lignes après un ordre ::

 SET @nb_lignes_inserées = @@ROWCOUNT

IDENTITY
--------

http://stackoverflow.com/questions/42648/best-way-to-get-identity-of-inserted-row

Plus sur comme méthode ::

    create table aca_test (id int identity , lib varchar(50));
    declare @IdentityOutput table ( ID int )
    insert into aca_test(lib) output inserted.id INTO @IdentityOutput values ('hel');

Comparer deux ensembles
-----------------------

Egalité de deux ensemble
++++++++++++++++++++++++

  select * from e1
  except
  select * from e2
union all
  select * from e2
  except
  select * from e1;

Fonction analytique
===================

Compter les lignes d'une table
------------------------------

DECLARE @Table1Count INT
SELECT @Table1Count = COUNT(*) FROM aca_partition WHERE id_partition=1;
SELECT @Table1Count;


Fonctions analytique
--------------------

http://sqlmag.com/t-sql/ranking-functions  explique rank dense_rank et row_number


create table aca_partition
(id_partition int,
 Qte int
 );

 insert into aca_partition(id_partition, Qte) values (1, 58);
 insert into aca_partition(id_partition, Qte) values (1, 2);
 insert into aca_partition(id_partition, Qte) values (1, 7);

 insert into aca_partition(id_partition, Qte) values (2, 5);
 insert into aca_partition(id_partition, Qte) values (2, 1);
 insert into aca_partition(id_partition, Qte) values (2, 87);
 insert into aca_partition(id_partition, Qte) values (2, 3);

select
   id_partition,
   Qte,
   RANK() OVER (partition by id_partition order by Qte) AS R,
   DENSE_RANK() OVER (partition by id_partition order by Qte) AS DR,
   ROW_NUMBER() OVER (partition by id_partition order by Qte) AS RN
FROM aca_partition;

Dictionnaire
============

Trouver les tables ayant telle colonne
--------------------------------------

Voici la requête ::

   SELECT table_name
   FROM INFORMATION_SCHEMA.COLUMNS
   WHERE COLUMN_NAME = 'Nom_de_colonne'


Index
=====

Drop Index
----------

La commande est ::

  drop index idx_tmp_current_cmd_StkEmp_01 on tmp_current_cmd_StkEmp;

Table variable versus temporary table
=====================================

- http://odetocode.com/articles/365.aspx

Table temporaire
================

Quand et comment les utiliser.

- http://www.sqlteam.com/article/temporary-tables

Comment identifier les tables temporaires existantes ?

Il suffit d'utiliser la requête suivante ::

	select TABLE_NAME from tempdb.information_schema.tables

Gestion des transactions et des erreurs
=======================================

http://baptiste-wicht.developpez.com/tutoriels/microsoft/sql-server/securiser/

TDD
===

http://tsqlt.org/146/database-test-driven-development/
http://sqlmag.com/t-sql/getting-started-test-driven-design-sql-server
http://msdn.microsoft.com/en-us/magazine/cc164243.aspx

Best practice
=============

- http://sqlmag.com/t-sql/t-sql-best-practices-part-1

shortcut management studio SQL sql-server
=========================================

http://technet.microsoft.com/fr-fr/library/ms174205.aspx

Selectionner texte
------------------

shift + fin selectionner jusque la fin de la ligne

Commenter
---------
ctrl + k, ctrl + c comment code
ctrl + k, ctrl + u uncomment code
ctrl + a tout selectionner

Executer SQL
------------
F5 executer tout le buffer ou seulement le texte selectionné.

Les signets
-----------
ctrl + k, ctrl + k definir un signet
ctrl + k, ctrl + n signet suivant
ctrl + k, ctrl + p signet précédent
ctrl + k, ctrl + l effacer les signets

Changer la valeur de l'identity
===============================

Pour cela utiliser la commande ::

  DBCC CHECKIDENT('Ma_table', RESEED, 500)

Python & Transact SQL
=====================

Télécharger le driver à cette adresse : https://code.google.com/p/pymssql/downloads/list
J'ai testé le pymssql-2.0.0b1-dev-20130111.win32-py2.7.exe sur un python 2.7.5

Pour se connecter il faut un utilisateur avec un mot de passe car l'authentification windows ne fonctionne pas ::

        conn = pymssql.connect(host='server\name', user='username', password='xxxx', database='database_name')
        cur = conn.cursor()
        cur.execute('select * from tmp_commande')
        print cur.fetchall()
        cur.execute('select * from tmp_Stock')
        print cur.fetchall()

