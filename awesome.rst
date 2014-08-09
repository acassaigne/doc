awesome
#######


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

Gestionaire de fichier :

sous gnome le programme se nomme  ::

    nautilus


changer de clavier :

utiliser les commandes ::

    setxkbmap fr
    setxkbmap dvorak




setxkbmap fr mac

avec un mac pour gérer la luminosité de l'écran 
sudo su - root
cd /sys/class/backlight/apple_backlight
echo 1 > brightness 
 
sudo "echo 3 >/sys/class/backlight/apple_backlight/brightness"

echo 1 | sudo tee /sys/class/backlight/apple_backlight/brightness 

https://github.com/travisjeffery/awesome-wm


disable sound
amixer -D pulse set Master 1+ toggle

enable sound
amixer -D pulse set Master 1+ toggle

http://askubuntu.com/questions/97936/terminal-command-to-set-audio-volume
Augmenter de 5%
amixer -D pulse sset Master 5%+

Diminuer de 5%
amixer -D pulse sset Master 5%-

Positionner à 50%
amixer -D pulse sset Master 50%



focuse after minimize
http://www.mail-archive.com/awesome@naquadah.org/msg04610.html

autre ressource pour la configuration
http://blog.wolf.am/archives/2011/04/25/awesome_wm/

Pour configurer finement avec calendrier etc...
http://urukrama.wordpress.com/2008/07/10/first-steps-with-awesome-window-manager/

des resources
http://ubuntuforums.org/showthread.php?t=675292
http://urukrama.wordpress.com/2008/07/10/first-steps-with-awesome-window-manager/
http://awesome.naquadah.org/wiki/My_first_awesome
http://awesome.naquadah.org/wiki/Awesome_3.x

http://awesome.naquadah.org/wiki/My_first_awesome
http://vincent.bernat.im/en/blog/2012-awesome-wm.html#awesome-configuration
