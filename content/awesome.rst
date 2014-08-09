:Title: Awesome
:Category: Linux
:Date: 2014-08-09
:Modified: 2014-08-09
:tags: linux, awesome, windows manager

Racourcis
---------

- change de mode mod + space
- agrandir/diminuer la taille de la fenêtre mode +  h,l
- changer de fenetre active mod +  j,k
- changer l'emplacement des fenetres mod + shift + j,j
- passer en full screen mod  + f
- relancer awesome mod + shit + r
- lancer une application mod + r
- fermer une fenetre mod + shift + c

Envoyer un application vers un tag mod + shift + tag
exemple mod + shift + 2 envoit l'application active vers le tag 2

Quelques astuces 
----------------

Gestionaire de fichier :

sous gnome le programme se nomme  ::

    nautilus


changer de clavier :

utiliser les commandes ::

    setxkbmap fr
    setxkbmap dvorak
    setxkbmap fr mac

avec un mac pour gérer la luminosité de l'écran  ::
 
    echo 1 | sudo tee /sys/class/backlight/apple_backlight/brightness 

https://github.com/travisjeffery/awesome-wm

Pour la gestion du son les commandes linux sont ::

    disable sound
    amixer -D pulse set Master 1+ toggle
    
    enable sound
    amixer -D pulse set Master 1+ toggle

Source http://askubuntu.com/questions/97936/terminal-command-to-set-audio-volume

Pour augmenter ou diminuer le son sous linux les commandes sont :
Augmenter de 5% 

.. code:: bash

    amixer -D pulse sset Master 5%+
    ls terminal-command-to-set-audio-volume
    cd truc
    export HHH='toto'

Diminuer de 5% ::

    amixer -D pulse sset Master 5%-

Positionner le niveau sonore à 50% ::

    amixer -D pulse sset Master 50%


Autre resources à regarder 
--------------------------

focuse after minimize

- http://www.mail-archive.com/awesome@naquadah.org/msg04610.html

autre ressource pour la configuration

- http://blog.wolf.am/archives/2011/04/25/awesome_wm/

Pour configurer finement avec calendrier etc...

- http://urukrama.wordpress.com/2008/07/10/first-steps-with-awesome-window-manager/

resources

- http://ubuntuforums.org/showthread.php?t=675292
- http://urukrama.wordpress.com/2008/07/10/first-steps-with-awesome-window-manager/
- http://awesome.naquadah.org/wiki/My_first_awesome
- http://awesome.naquadah.org/wiki/Awesome_3.x
- http://awesome.naquadah.org/wiki/My_first_awesome
- http://vincent.bernat.im/en/blog/2012-awesome-wm.html#awesome-configuration
