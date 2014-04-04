
Quelques éléments d'information sur python

# Classe abstraite & interface : Abstract Class module abc
http://stackoverflow.com/questions/2124190/how-do-i-implement-interfaces-in-python
http://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python
http://dbader.org/blog/abstract-base-classes-in-python

# Environnement de développement

## Virtualenv

### création d'un environnement 

utilise la commande 


```shell
mkvirtualenv -a devel/blog blog
```
### activer/désactiver un environnement 

```shell
workon env_name
deactivate
```

## Plugin JEDI

Sublime text avec ce plugin https://github.com/srusskih/SublimeJEDI
Pour activer l'autocomplétion utiliser cette configuration :

    # User/Preferences.sublime-settings or User/Python.sublime-settings
    {
        // ...
        "auto_complete_triggers": [{"selector": "source.python", "characters": "."}],
    }

Pour sauter à la définition d'une méthode ctrl+shift+G

# Installation pip sous win32

Commencer par installer setup-tools :

   http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows

Récupérer le exe (setuptools-0.7.7.win32-py2.7.‌exe) à cette adresse http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools
ensuite récuperer le exe d'installation de pip (pip-1.3.1.win32-py2.7.‌exe) à cette adresse
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip

# Quelques commandes utiles

## Lancer un simple serveur http

Voici la commande :

    cd mon_repertoire_wwww
    python -m SimpleHTTPServer

Changer le port, pour le positionner sur le port 80 (par exemaple) :

    cd mon_repertoire_wwww
    python -m SimpleHTTPServer 80
