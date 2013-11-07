******
Python
******

Installation pip sous win32
===========================

Commencer par installer setup-tools ::

   http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows

 récupérer le exe (setuptools-0.7.7.win32-py2.7.‌exe) à cette adresse http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools
ensuite récuperer le exe d'installation de pip (pip-1.3.1.win32-py2.7.‌exe) à cette adresse
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip

Lancer un simple serveur http
-----------------------------

Voici la commande ::

    cd mon_repertoire_wwww
    python -m SimpleHTTPServer

Changer le port, pour le positionner sur le port 80 (par exemaple) ::

    cd mon_repertoire_wwww
    python -m SimpleHTTPServer 80
