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

La bonne méthode est d'utiliser ::

  SCOPE_IDENTITY()

Méthode avec OUTPUT ::

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

Procedures
==========

Définir une procédure avec des paramètres externes (output) ::

    IF OBJECT_ID('dbo.get_info_rejets_nb_colis_doublon') IS NOT NULL
      DROP PROCEDURE dbo.get_info_rejets_nb_colis_doublon;
    GO

    CREATE PROCEDURE [dbo].[get_info_rejets_nb_colis_doublon]
     @pl_id_job_deal BIGINT,
     @pl_count_colis_prives INT OUTPUT,
     @pl_count_rejets INT OUTPUT,
     @pl_count_doublon INT OUTPUT
    AS
    BEGIN
    SELECT
       @pl_count_colis_prives = colis_prives.count_prives,
       @pl_count_rejets = r.count_rejets,
       @pl_count_doublon = doublon.count_doublons
    FROM (SELECT value as count_rejets FROM result_load_commands
          WHERE id_job_deal = @pl_id_job_deal
             AND  name = 'QTE_COLIS_REJETS' ) r,
          (SELECT value as count_prives FROM result_load_commands
           WHERE id_job_deal = @pl_id_job_deal
             AND  name = 'QTE_COLIS_PRIVES' ) colis_prives,
          (SELECT value as count_doublons FROM result_load_commands
           WHERE id_job_deal = @pl_id_job_deal
             AND name = 'DOUBLON' ) doublon;
    END;
    GO

Appeler cette procédure ::

  DECLARE @r INT
  DECLARE @c INT
  DECLARE @D int

  exec get_info_rejets_nb_colis_doublon  @pl_id_job_deal =39 , @pl_count_colis_prives=@r OUTPUT, @pl_count_rejets=@c OUTPUT, @pl_count_doublon=@d OUTPUT
  SELECT @r,@c,@d

Table temporaire
================

Quand et comment les utiliser.

- http://www.sqlteam.com/article/temporary-tables

Comment identifier les tables temporaires existantes ?

Il suffit d'utiliser la requête suivante ::

	select TABLE_NAME from tempdb.information_schema.tables

Contraintes
===========

Clé primaire composite ::

  CREATE TABLE param_job_deal
    ( id_param_job_deal BIGINT IDENTITY(1,1) PRIMARY KEY,
      id_job_deal BIGINT NOT NULL,
      step_name VARCHAR(50),
      param_name VARCHAR(50),
      str_value VARCHAR(50),
      bigint_value bigint,
      PRIMARY KEY (id_param_job_deal, id_job_deal)
      );

Clé étrangère ::

  CREATE TABLE param_job_deal
    ( id_param_job_deal BIGINT IDENTITY(1,1) PRIMARY KEY,
      id_job_deal BIGINT NOT NULL,
      step_name VARCHAR(50),
      param_name VARCHAR(50),
      str_value VARCHAR(50),
      bigint_value bigint,
      FOREIGN KEY (id_job_deal) REFERENCES job_deal(id_job_deal)
      );



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

