*****
MySQL
*****

DROP CONSTRAINTS
================

Exemple de syntaxe ::

  alter table ligne_preparation drop foreign key
  fk_ligne_preparation_colis1;


Index
=====

Voir les index d'une table ::

  SHOW INDEX FROM vetigend.tj_panier_pan;

Se connecter
============

En utilisant le client mysql ::

  mysql -u root -p
  mysql -h hostname -u root -p


Pour administrer une base de données il faut être connecté avec `root`.

Creation de base de données
===========================

Exemple de syntaxes ::

  create database test_aca;
  grant usage on test_aca.* to aca@localhost identified by 'aca';

Données les droits à un utilisateur ::

  grant all on t_aca.* to 'aca';

Données les droits d'usage d'une base de données ::

  grant usage on *.* to aca  identified by 'aca';


Chargement des fichiers
=======================

Utiliser l'ordre `load data infile` ::

  LOAD DATA INFILE 'filename.csv' REPLACE INTO TABLE TMP_QUANTITE FIELDS TERMINATED BY ';' ESCAPED BY '\\' LINES TERMINATED BY '\n' (ID_STOCK_SCT, ID_NATURE_STOCK,QUANTITE)

performance et mémoire

http://www.mysqlperformanceblog.com/2007/11/01/innodb-performance-optimization-basics/

Quelques recommandations extraites de cet article :

innodb_buffer_pool_size 70-80% of memory is a safe bet. I set it to 12G on 16GB box.
UPDATE: If you’re looking for more details, check out detailed guide on tuning innodb buffer pool
innodb_log_file_size – This depends on your recovery speed needs but 256M seems to be a good balance between reasonable recovery time and good performance
innodb_log_buffer_size=4M 4M is good for most cases unless you’re piping large blobs to Innodb in this case increase it a bit.
innodb_flush_log_at_trx_commit=2 If you’re not concern about ACID and can loose transactions for last second or two in case of full OS crash than set this value. It can dramatic effect especially on a lot of short write transactions.
innodb_thread_concurrency=8 Even with current Innodb Scalability Fixes having limited concurrency helps. The actual number may be higher or lower depending on your application and default which is 8 is decent start
innodb_flush_method=O_DIRECT Avoid double buffering and reduce swap pressure, in most cases this setting improves performance. Though be careful if you do not have battery backed up RAID cache as when write IO may suffer.
innodb_file_per_table – If you do not have too many tables use this option, so you will not have uncontrolled innodb main tablespace growth which you can’t reclaim. This option was added in MySQL 4.1 and now stable enough to use.
Also check if your application can run in READ-COMMITED isolation mode – if it does – set it to be default as transaction-isolation=READ-COMMITTED. This option has some performance benefits, especially in locking in 5.0 and even more to come with MySQL 5.1 and row level replication.


Performance sur LOAD INFILE
http://derwiki.tumblr.com/post/24490758395/loading-half-a-billion-rows-into-mysql

Resource globale
http://www.dj-j.net/waka/Linux:Administration_MySQL
