************
Transact-SQL
************

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
