**********
Cours Java
**********

Semaine 1
=========


Url pour configurer et approfondir eclipse.
https://class.coursera.org/intro-java-fr-001/wiki/view?page=install#conf_eclipse

Méthode de travail 
https://class.coursera.org/intro-java-fr-001/wiki/view?page=courselogistics


Les types simple
----------------

int c'est entier et double pour des nombres décimaux.

int toto = 0;
Toujours initialiser car on peut avoir une exception sur un system.output

déclaration de plusieurs variables sur une même ligne

int p = 1, q = 0;
char monChar = 'a';
Ne pas abuser car moins lisible.
Exemple de nom respectant les conventions ::

 int nCarreTotal = 0;
 int sousTotal98 = 0;

 Les noms commences par une minuscule et les mots suivants par une majuscule.

Les constantes
++++++++++++++

Il faut utiliserr ``final`` 
final double PI = 3.1416;