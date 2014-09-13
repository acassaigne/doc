:Title: Macbook & Linux
:Category: Macbook
:Date: 2014-08-24
:Modified: 2014-08-24
:tags: linux, macbook v5.5


********************
Linux & MacBook v5,5
********************

.. contents:: Table des matières

1ère partie sous MacOS X
========================
Une commande utile pour déterminer la version hardware de votre mac ::

    dmidecode -s system-product-name

Une des ressources les plus complète pour installer linux sur mac book
5,5 est cette adresse : http://allurgroceries.com/mbp55/


Reduire la taille de la partition MacOS X
-----------------------------------------

Pour nous utiliserons la commande ``diskutil``. 
Nous commencerons par lister les partitions existantes ::

    diskutil list
    /dev/disk0
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:      GUID_partition_scheme                        *160.0 GB   disk0
       1:                        EFI                         209.7 MB   disk0s1
       2:                  Apple_HFS Macintosh HD            159.7 GB   disk0s2

.. note:: si nous souhaitons avoir plus d'informations sur le disque
          (marque, capacité etc...) il est possible d'utiliser la commande
          suivante ``diskutil info /dev/disk0``

.. note:: identifier le système de boot se réalise à l'aide la
          commande ``bless --info``, ces commandes doivent être lancées en
          étant connecté avec l'utilisateur ``root``

Exemple d'informations retournées par la commande ``bless --info`` ::

    bless --info
    finderinfo[0]: 1306219 => Blessed System Folder is /System/Library/CoreServices
    finderinfo[1]: 1677004 => Blessed System File is /System/Library/CoreServices/boot.efi
    finderinfo[2]:      0 => Open-folder linked list empty
    finderinfo[3]:      0 => No OS 9 + X blessed 9 folder
    finderinfo[4]:      0 => Unused field unset
    finderinfo[5]: 1306219 => OS X blessed folder is /System/Library/CoreServices
    64-bit VSDB volume id:  0x711146C481134A9F

Pour diminuer la taille de la partition il faut utiliser la commande
``diskutil resizeVolume xxx`` où xxx représente la partition ::

    diskutil resizeVolume disk0s2 140G   

Le résultat de la commande est celui-ci (cela prends quelques minutes
pour dimuner la taille de la partition) ::

     Started partitioning on disk0s2 Macintosh HD
     Verifying disk
     Resizing
     Finished partitioning on disk0s2 Macintosh HD
     /dev/disk0
        #:                       TYPE NAME                    SIZE       IDENTIFIER
        0:      GUID_partition_scheme                        *160.0 GB   disk0
        1:                        EFI                         209.7 MB   disk0s1
        2:                  Apple_HFS Macintosh HD            139.9 GB   disk0s2

Une fois la taille de la partition diminuée il est maintenant possible
d'installer Linux sur la place libérée.

.. note:: Pour créer des partition sous linux en faisant usage de la
          table de type GPT. Il faut utiliser la commande ``gdisk`` et
          non pas ``fdisk``. Cette commande est disponible sur le
          livecd de ``system rescue``.


Installer le boot loader rEFIt
------------------------------

Vous pouvez le télécharger à cette adresse
http://refit.sourceforge.net/.  

Prendre la version ``Mac disk image``, lancer l'installation et
rebooter.  Si lors du reboot aucun menu ``rEFIt`` n'est visible c'est
qu'il faut relancer l'installation via le script ``enable.sh``.  Pour
cela vous devez disposer d'un répertoire ``/efi`` à la racine du
disque dur.

Pour activer ``rEFIt`` manuellement voici les commandes à utiliser en
étant l'utilisateur ``root`` ::

    sudo su - root
    cd /efi/refit
    ./enable.sh

Ensuite rebooter le Mac et vous devez avoir le menu suivant.

.. image:: ../../images/screen_refit.png

Boot & rEFIt
------------

Le mac gére ses partitions via une table de type GPT et non pas
MBR. Le mac est donc prêt pour les disque dont la capacité est >2To.
Le bios de type EFI utilise donc ce format de table mais grub ne sait
pas lire ce type de table des partitions.
Il lui faut donc à la fois émuler le bon vieux bios du PC et une table de type MBR.
Cela est réalisé par le boot loader rEFIt pour les deux points.

Par conséquent il faut absolument que la partition contenant les
kernel Linux soit dans les **quatres première partition** et de type
**partition principale**. Et également de **taille raisonnable (petite
1Go par exemple)** sinon grub ne peut pas accéder à la partition.

2ème Partie installer Debian
============================

Installation
------------

Introduire le ``CD-ROM`` d'installation de la Debian et rebooter le
mac tout en appuyant sur la touche ``C`` pour démarrer sur le
``CD-ROM``.
  
Pour le compte root prendre un mot de passe simple pour commencer car
il est probable que vous ayez des problèmes de clavier.


.. note:: Vous trouverez à cette adresse une liste des touches utiles
          pour les Mac http://www.jacsoft.co.nz/Tech_Notes/Mac_Keys.shtml.

.. tip:: Comment passer d'une console à l'autre ?  Pour passer d'une
    console à l'autre lors de l'installation de la Debian il convient
    d'utiliser les touches Fn+control+option+F2

Installer Grub
--------------

Installer ``grub`` sur la partition et non pas en tant que ``Master
Boot Record (MBR)``. Pour identifier le numéro de la partition changer
de console.


Une fois l'installation terminé au niveau du boot loader ``rEFIt``
vous devez lancer le *shell refit* pour demander la synchronisation du
``boot EFI``. Une fois la synchronisation terminée il est conseillé
d'arrêter et de redémarrer le Mac.  Il vous est maintenant possible de
booter sous Debian.

Configurer Linux
----------------

Clavier en mode console
.......................

Une fois arrivé au ``login`` se connecter sous ``root``. Un rapide
contrôle pour vérifier le bon/mauvais fonctionnement des touches
"éèçà@#<>-" va nous conduire à selectionner une autre configuration
pour le clavier.  Pour la Debian l'ensemble des claviers se trouvent
dans le répertoire ``/usr/share/keymaps/mac``, le clavier fonctionnant
correctement sous mac book pro version 5,5 est
``mac-macbook-fr.kmap.gz``.

Pour reconfigurer durablement le clavier il faut utiliser la commande suivante ::
     dpkg-reconfigure -plow console-data

Prendre l'option ``select all architecture`` ensuite selectionner ``macbook``

Voila votre clavier est correctement configuré en mode console.

Configuration clavier sous KDE.
...............................

Sur ``debian/squeeze`` toute configuration clavier se joue dans le
fichier ``/etc/default/keyboard`` il vous faut cette configuration ::

    XKBMODEL="pc105"
    XKBLAYOUT="fr"
    XKBVARIANT="mac"
    XKBOPTIONS="lv3:rwin_switch"



Voici la configuration clavier retenue pour ``KDE 4.4``.

.. image:: ../../images/config_keyboard_macbook_kde.png

Mais comment accéder au touches F1, F2 et/ou luminosité +/- ?
La aussi c'est une option bien caché sous KDE cela se passe ici. 

.. image:: ../../images/configure_clavier_macbook_kde_third_party.png

Il est maintenant possible de passer du mode graphique au mode console
via la combinaison de touche ctrl+alt+F1.  Une fois en mode console
par contre c'est la touche ``cmd`` qui remplace la touche ``alt``,
faudra creuser ce petit problème. Voila on commence à avoir un clavier
opérationnel sous KDE.

Mais où sont les caractères \|[]{}. Voici une liste des raccourcis
clavier :

* [ taper cmd + shift + (
* ] taper cmd + shift + )
* | taper cmd + shift + L
* \ taper cmd + shift + /
* ~ taper cmd + shift + n

Gestion de la luminosité de l'écran.
....................................

Avec kernel 2.6.35
,,,,,,,,,,,,,,,,,,

Avec le kernel ``2.6.35`` la luminosité de l'écran LCD se géré par
défaut via cette clé ``/sys/class/backlight/nv_backlight/brightness``

En soirée un niveau de luminosité acceptable est 70.
Pour la journée c'est à déterminer.


Gestion de la luminosité de l'écran sous X11
............................................

Installation à partir des sources
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Dernière étape installer les driver ``nvidia-bl-dkms`` qu'il est
possible de télécharger à cette adresse :
https://launchpad.net/~mactel-support/+archive/ppa/+packages

chercher avec ce formulaire nvidia-bl, télécharger les sources de la
dernière version.
Ne pas télécharger la version mbp mais la version nvidia-bl-dkms

Par exemple télécharger ``nvidia-bl-dkms_0.16.10~lucid.tar.gz`` pour
l'installer suivre ces étapes ::

    dkms remove -m nvidia_bl -v 0.16.10 --all
    dkms ldtarball --archive=nvidia-bl-dkms_0.16.10~lucid.tar.gz 
    dkms add build install -m nvidia_bl -v 0.16.10 --kernelsourcedir=/usr/src/linux-headers-2.6.35.5-aca2
    rmmod mbp_nvidia_bl
    modprobe nvidia_bl
    echo "blacklist mbp_nvidia_bl" >> /etc/modprobe.d/blacklist.conf
    echo "nvidia_bl" >> /etc/modules



installation à partir des modules dkms
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Télécharger le package Debian suivant : ``nvidia-bl-dkms_0.14_all.deb``
Et lancer son installation par les commandes ::

   wget https://launchpad.net/~mactel-support/+archive/ppa/+build/1044380/+files/nvidia-bl-dkms_0.14_all.deb
   dpkg -i nvidia-bl-dkms_0.14_all.deb
   echo "blacklist mbp_nvidia_bl" >> /etc/modprobe.d/blacklist.conf
   echo "nvidia_bl" >> /etc/modules

Vérifier la présence du module pour votre noyau ::
  
   ls -lrt /lib/modules/2.6.30-2-686/kernel/drivers/video/backlight/

Charger le module ::

   modprobe nvidia_bl

Pour vérifier la prise en charge par le noyau de la fonctionnalité
blacklight utilisez les commandes ::

  dmesg | grep nvidia_bl
  nvidia_bl: Supported Nvidia graphics adapter 10de:0863:106b:00b9 detected

Il vous est alors possible de modifier la luminosité par les
paramètres système suivants ::

   echo 100 > /sys/class/backlight/nvidia_backlight/brightness
   echo 200 > /sys/class/backlight/nvidia_backlight/brightness
   cat /sys/class/backlight/nvidia_backlight/max_brightness


Avec les driver nvidia-bl-dkms
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

En mode console le noyau linux gère correctement la carte graphique à
partir de la version ``2.6.30`` possiblement pour une version
légèrement inférieur du noyau. Cela se configure à l'aide de l'entrée
système suivante ``/sys/class/backlight/nvidia_backlight/brightness``.

Une luminosité acceptable en journée est 400 et en soirée 100. La
valeur maximal est de 1023 et est accesible via cette commande ::

    cat /sys/class/backlight/nvidia_backlight/max_brightness

Pour changer la luminosité il suffit d'utiliser une commande de ce type ::

    echo 100 > /sys/class/backlight/nvidia_backlight/brightness
    echo 400 > /sys/class/backlight/nvidia_backlight/brightness

.. note:: Par contre la gestion sous X11 n'est pas assurée avec les
    drivers par défaut pour cela il faut installer les driver nvidia
    et installer le driver ``nvidia_bl`` (nvidia blackligth)




Installer les driver nvidia
...........................

Il faut télécharger la dernière version des drivers nvidia à cette adresse http://www.nvidia.com/
Ensuite il faut installer la version de ``GCC`` qui a été utilisé pour compiler le noyau linux.

.. note:: 
   Les drivers utilisés au cours de cette installation sont les drivers ``NVIDIA-Linux-x86-190.42-pkg1.run``

Par exemple si votre kernel a été compilé avec ``GCC 4.1`` lancer la commande suivante ::

    apt-get install make gcc gcc-4.1 linux-headers* -y

Ensuite il faut stopper X11 et lancer l'installation des drivers avec les commandes suivantes ::

    /etc/init.d/kdm stop
    cd /home/repetoire_drivers_nvidia/
    export CC=/usr/bin/gcc-4.1
    sh NVIDIA-Linux-xxxxxxx-pkgx.run

Pour terminer relancer X11 ::

    /etc/init.d/kdm start

Votre résolution doit maintenant être celle de l'écran ``1280x800`` pour un ``Mac Book 13pouces v5,5``.



Changer le comportement des touche fn+F1
........................................

Si vous souhaitez avoir directement accès aux touches F1, F2... et non
plus directement accès aux touches luminosité +/-, volume du son +/-.
Il vous faut alors modifier ce paramètre système
``/sys/module/hid_apple/parameters/fnmode`` de la façon suivante ::

     echo 2 > /sys/module/hid_apple/parameters/fnmode

Gestion de la luminosité du clavier
...................................

Il faut pour cela modifier la valeur du paramètre système
``/sys/devices/platform/applesmc.768/leds/smc::kbd_backlight/brightness``.

Voici quelques valeurs à titre d'exemple ::

   echo 100 > /sys/devices/platform/applesmc.768/leds/smc::kbd_backlight/brightness
   # valeur faible
   echo 20 > /sys/devices/platform/applesmc.768/leds/smc::kbd_backlight/brightness
   # Pour éteindre le clavier 
   echo 1 > /sys/devices/platform/applesmc.768/leds/smc::kbd_backlight/brightness

La valeur maximal est connu via ce paramètre ::

   cat /sys/class/backlight/nvidia_backlight/max_brightness
   1023

.. note:: 
     Si vous ne disposez pas de paramètres système ``/sys/devices/platform/applesmc.768`` 
     cela signifie que votre noyau linux n'est pas assez récent et qu'il ne sait donc pas prendre 
     en charge le matériel spécifique aux MacBook. Il vous faut monter la version de votre noyau.

Installer le logiciel pommed
............................

Ce logiciel permet la gestion des touches d'ejection du cd, du volume
sonore +/- etc... Il est récupérable à cette adresse
http://alioth.debian.org/projects/pommed/

pommed requires:
,,,,,,,,,,,,,,,,

 - pciutils / libpci (on Intel machines only)
 - libofapi aka oflib (PowerMac machines only, see below)
 - zlib
 - libconfuse
 - libdbus
 - libasound
 - libaudiofile
 - eject

Lancer les commandes ::

     apt-get install zlib
     apt-get install libpci-devlibpci1 pciutils
     apt-get install libpci-dev libpci1 pciutils
     apt-get install libconfuse-dev libconfuse0
     apt-get install libdbus-1-dev
     apt-get install libasound2 libasound2-dev libasound2-doc
     apt-get install libaudiofile0 libaudiofile-dev
     
Compiler pommed
,,,,,,,,,,,,,,,

Cela se réalise simplement en éxécutant la commande ``make pomme`` ::

   cd source_pommed
   make pommed

Installation de pommed
,,,,,,,,,,,,,,,,,,,,,,

Installer pommed (voir fichier ``INSTALL`` dans le répertoire des sources) ::

      cd /home/aca/download/pommed-1.30
      cp pommed/pommed /usr/bin/
      ls pommed/data/
      cp -pr pommed/data/* /usr/share/pommed
      mkdir /usr/share/pommed
      cp -pr pommed/data/* /usr/share/pommed
      cp pommed.conf.mactel /etc/pommed.conf
      cp pommed.init /etc/init.d/pommed
      chmod u+x /etc/init.d/pommed
      cp dbus-policy.conf /etc/dbus-1/system.d/pommed.conf


Configurer l'audio
..................
TODO

Configurer le wifi
..................

Installation du driver BCM4322
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


La carte wifi du macbook 5,5 est la suivante ``Broadcom BCM432b
802.11`` ou ``bcm4322``.

Télécharger le driver à cette adresse http://www.broadcom.com/support/802.11/linux_sta.php

Une adresse a regarder : http://wireless.kernel.org/en/users/Drivers/b43

La commande suivante permet d'identifier le modèle de chipset wifi ::

   lspci -vnn | grep 14e4
   03:00.0 Network controller [0280]: Broadcom Corporation BCM4322 802.11a/b/g/n Wireless LAN Controller [14e4:432b] (rev 01)

A l'adresse suivante
http://wireless.kernel.org/en/users/Drivers/b43#Supported_chip_types
nous constatons que le chipset 4322 n'est actuellement pas supporté
par le driver b43 de Linux.

Il faut donc supprimer le chargement de driver/module ::

  modprobe -r b43


.. note:: pour vérifier que le module est réellement déchargé, il convient d'utiliser la commande suivante ::
          lsmod | grep b43

Pour interdire le chargement de ce module lors du prochain reboot ::

  echo "blacklist b43" >> /etc/modprobe.d/blacklist
  echo "blacklist ssb" >> /etc/modprobe.d/blacklist


Installer les outils de gestion wifi ::

  apt-get install wireless-tools

Après avoir télécharger les drivers chez broadcom, il faut les
compiler ::

   cd /usr/src
   mkdir wl
   cd wl
   tar xvf hybrid-portsrc-x86_32-v5.10.91.9.3.tar.gz
   cd src/wl
   KBUILD_NOPEDANTIC=1 make -C /lib/modules/`uname -r`/build M=`pwd`
   install -D -m 755 wl.ko /lib/modules/`uname -r`/kernel/drivers/net/wireless/wl.ko
   depmod -r
   modprobe wl
   echo wl >> /etc/modules

.. note:: pour recompiler ce driver il vous faut les header de votre noyau linux.
          ``apt-get install linux-headers-2.6.30-2-common``

Quelques commandes utiles pour configurer la partie wifi.

Si la compilation ne se termine pas correctement dû à des changement
dans le noyau par exemple. Il faut alors soit trouver un patch soit
trouver un package déjà compiler, par exemple pour ubuntu.
Comme celui-ci qui permet d'installer les driver pour le noyau 2.6.35 ::

    bcmwl-kernel-source_5.60.48.36+bdcom-0ubuntu5_i386.deb

Configuration du wifi
---------------------

Regarder si votre carte wifi est accessible (driver chargé) ::

  iwconfig

Si le résultat ressemble à ceci ::

   eth2 IEEE 802.11g ESSID:"WORKSTATION" Nickname:"pslk"

C'est que la carte wifi est reconnue.

Afficher la liste des réseau wifi disponible ::

   iwlist eth2 scan

.. note:: les autres commandes possibles sont :
           
           - iwlist eth2 freq
           - iwlist eth2 bitrate
           - iwlist eth2 ap

Selectionner le réseau ``WORSTATION`` ::

  iwconfig eth2 essid WORKSTATION

Passer en mode ``managed`` ou ``ad hoc`` ::

  iwconfig eth2 mode Managed
  iwconfig eth2 mode Ad-Hoc

Entrer une clé WEP ::

  iwconfig eth2 key restricted 0123H4567B89

.. note:: ces informations sont accessible à cette adresse http://www.trustonme.net/didactels/304.html


Divers ressources à explorer
----------------------------

quelques touches de caractères sous mac
http://infopythonfr.wordpress.com/tag/pipe/

ne pas booter sous X/ supprimer démarrage kdm ou gdm
http://linuxdistrochoices.com/blog/review/distro-choice-based-on-using-runlevels/

autres sources pour le clavier.
http://blog.lmartin.fr/dc2/index.php/post/2008/05/11/Configurer-le-clavier-Apple-extra-fin-sous-Ubuntu

Autres touches du clavier.
http://forum.ubuntu-fr.org/viewtopic.php?pid=650837

Installer les drivers Linux nvidia sous mac book .
http://www.commentcamarche.net/faq/sujet-3456-debian-howto-xorg7-installer-drivers-nvidia
http://wiki.debian.org/NvidiaGraphicsDrivers

Un info trouvé sur un forum http://ubuntuforums.org/showthread.php?t=198453 ::

     Keyboard Backlight works with F8 and F10. To turn it off use
     F8. To increase F10. At the moment F9 does nothi ng.  The
     keyboard in general is a work in progress for me. You can select
     a Macbook Pro(Intl) keyboard bu t I am not sure what it does. I
     am playing with xev. It displays X11 events, like keycodes. With
     xmo dmap you can update your keyboard map, but only for the
     session. Check out the man pages for more in fo. As I said a work
     in progress for me.
     
Autre info trouvé pour le clavier ::

    Keyboard layout
    
    I have set my system to UTF-8, using a en_US.utf8 locale and I am
    using a UTF-8 keymap (not a Latin-1 one!): I have modified the
    keymap a little. The more keys you get right in the keymap file
    the less work you have in X, as it inherits these settings! I
    started off with a keymap file created with dumpkeys, tweaked it
    and put it to /etc/default.kmap. This file is then referenced from
    /etc/conf.d/keymaps in the KEYMAP variable. For X see below!
    
    The Apple keys work as Alt-Gr. So it provides access to the 'at'
    sign as Apple-2, the # sign as Apple-3, square brackets [] as
    Apple-ü and Apple-", braces {} as Apple-ä and Apple-$, pipe | as
    Apple-1 (or Apple-7), backslash \ as Apple-<. Additionally the
    Apple-E is the Euro  and Apple-G the 'at' like on a Mac. I have
    made the keypad Enter key (between Right Apple and Cursor Left) a
    'Delete' key. With Shift it's 'Insert'. You also get 'Delete' with
    Fn-Backspace (Kernel does that).
    
    By default the Kernel sets the Fn key to always enabled (OS-X
    behaviour). If you don't like that turn it off with the kernel
    parameter usbhid.pb_fnmode=2 in Grub or change it at runtime
    through /sys/module/usbhid/parameters/pb_fnmode.

Autres commandes utiles pour identifier le code d'une touche ::

   showkey -t 5
   dumpkeys 
   xev
