*****************************
Divers astuces & notes utiles
*****************************


DLNA serveur
============

Lancer le minidlna serveur ::

  minidlna -f /home/acassaigne/.minidlna/minidlna.conf -P /home/acassaigne/.minidlna/minidlna.pid

La configuration est dans $HOME/.minidlna.


La commande pour reconstruire le cache est ::

 xxx

Freenas
=======


Voir la configuration réseau ::

  ssh root@partage.workgroup
  ifcongig -m (pour avoir les options media)

Sous linux pour voir le vitesse sur l'interface réseau ::

  ethtool eth0

En sortie nous obtenons::

  Settings for eth0:
	Supported ports: [ MII ]
	Supported link modes:   10baseT/Half 10baseT/Full
	                        100baseT/Half 100baseT/Full
	                        1000baseT/Full
	Supported pause frame use: No
	Supports auto-negotiation: Yes
	Advertised link modes:  10baseT/Half 10baseT/Full
	                        100baseT/Half 100baseT/Full
	                        1000baseT/Full
	Advertised pause frame use: No
	Advertised auto-negotiation: Yes
	Speed: 100Mb/s
	Duplex: Full
	Port: MII
	PHYAD: 1
	Transceiver: external
	Auto-negotiation: on
        Cannot get wake-on-lan settings: Operation not permitted
        Cannot get link status: Operation not permitted

Ici on est en 100Mb/s

Pour changer la vitesse ::

 sudo ethtool -s eth0 speed 1000 duplex full

Tester les performances réseaux via la commande iperf.
Sur le serveur lancer la commande ::

  iperf -s

sur le poste client lancer la commande ::

  iperf -c 192.168.1.100 (adresse du serveur)

si vous souhaitez avoir les débits en MegaBytes passez l'option ::

  iperf -c 192.168.1.100 -f MBytes


Calibre
=======

PDF et DRM
----------

Supprimer les drm des pdf, télécharger le pdf avec Adobe Digital
Editions. Ensuite installer le plugging ineptpdf_v01.4_plugin.zip au niveau de calibre.
Redémarrer Calibre et importer le fichier pdf qui sera decrypter et donc sans drm !

ebook et DRM
------------

Pour supprimer les DRM des kindle il faut installer le pluging DeDRM à
télécharge le zip contenant un certain nombre de pluging. Téléchargeable à cette adresse http://apprenticealf.wordpress.com/2012/09/10/drm-removal-tools-for-ebooks/
Le zip est tools_v6.0.1.zip

Les fichier de l'application Kindle se trouve pour windows sous My Documents folder\My Kindle Content

Copier et importer les fichiers AZW/AZW1/AZW2/AZW3 dans calibre et
ensute convertir ces fichiers avec calibre.
Le format de sorti doit être ebook.

http://www.the-digital-reader.com/2012/06/15/how-add-kindle-drm-removal-plugin-calibre/#.UVcIjnawekA


Eclipse
=======

Installer le plug-in Eclipse color theme
Allez dans le menu help et prendre l'option Eclipse Marketplace
Rechercher Eclipse Color Theme et lancer l'installation.

Importer un nouveau theme après l'avoir downloader à cette adresse :
http://eclipsecolorthemes.org/

Pour gérer les thèmes allez dans le mene Window-->preferences
Appareance->Color Theme (option installé via le plug-in)

Eclipse et Tomcat
-----------------

Télécharger le package tomcat, décompresser.

Dans eclipse en haut à droite cliquer sur Java EE, ensuite dans
l'onglet en bas cliquer sur server et ajouter un server Apach Tomcat.

Création d'une servlet
----------------------

Suivre cet excellent tutorial.

http://theopentutorials.com/examples/java-ee/servlet/how-to-create-a-servlet-with-eclipse-and-tomcat/

D'apport créer un projet web dynamique.
File menu -> New -> Dynamic Web Project

L'assistant doit proposer Apache Tomcat 6 et 2.5 pour dynamic web module version

Ensuite création de la servlet
Right click on src or Project -> New -> Servlet
Enter the Java package name as com.theopentutorials.servlets
Enter the Class name as HelloWorldServlet
Click on ‘Finish‘

Dans la méthode doGet ajouter ces lignes
PrintWriter out = response.getWriter();
out.println("Hello World");


Git
===

Pour voir les repo distants ::

  git remote -v

Pour ajouter un repo distant ::

  git remote add upstream https://github.com/otheruser/repo.git

Pour se synchroniser avec le repo distant utiliser la commande ::

  git fetch upstream

Voir les branches ::

  git branch -va

Pour réaliser un merge commencer par se positionner dans sa branche ::

  git checkout source

Ensuite réaliser le merge ::

  git merge upstream/source


Obtenir une version donnée d'un fichier
---------------------------------------

la commande ::

  git log

donne les commit réalisés

La commande ::

  git checkout 23ed5270d1d9b6210dea0316a39f69797d661697 mon_fichier

permet d'obtenir la version en question du fichier.

Ensuit un cp du fichier ::

  cp mon_fichier mon_fichier.23ed5270d

et retour à la version actuelle ::

  git checkout HEAD mon_fichier

Autre informations
https://help.github.com/articles/fork-a-repo

A lire sur le reset
http://git-scm.com/2011/07/11/reset.html


Réaliser un push
----------------

Utiliser la commande ::

  git push origin club_de_lecture

Groupe Unix
===========

Création d'un groupe
---------------------

Utiliser la commande ::

  sudo groupadd -g 1500 mynas

Ajouter un utilisateur existant à un groupe ::

  sudo usermod -a -G mynas acassaigne

pandoc
======

Commande convertir markdown to mediawiki ::

  pandoc -f markdown -t mediawiki test.md -o r.txt

Debian
======

Identifier les packages installés
---------------------------------

Utiliser la commande ::

 dpkg --get-selections

Programmes à connaitre
======================

Ocuppation espace disque
------------------------

Pour l'occuppation de l'espace disque : JDiskReport ou filelight.

Emacs
=====

bookmarks
---------

Ajouter ce fichier au bookmarks ::

  C-x r m

Aller à un bookmark ::

  C-x r b


bbdb email database
-------------------

Création d'une nouvelle entrée ::

  M-x bbdb-create

Installer wanderlust
--------------------

Il faut installer les packages suivants ::

    aptitude install flim apel

Utilisation de wanderlust
-------------------------


Utilisation de Mime

http://www.cs.vassar.edu/cgi-bin/info2www?%28emacs-w3m%29SEMI+MUAs

http://www.han.de/~racke/pard/emacs.html
key		feature
---		-------

u		Move to upper content
p or M-TAB	Move to previous content
n or TAB	Move to next content
SPC		Scroll up or move to next content
M-SPC or DEL	Scroll down or move to previous content
RET		Move to next line
M-RET		Move to previous line
v		Decode current content as `play mode'
e		Decode current content as `extract mode'
C-c C-p		Decode current content as `print mode'
a		Followup to current content.
q		Quit
button-2	Move to point under the mouse cursor
        	and decode current content as `play mode'


A tester

C-o pour auto refile ! http://www.gohome.org/wl/doc/wl_77.html#SEC77

Summary

Taper g pour aller dans un répertoire depuis la fenêtre summary.
f pour forward.
e ou y pour saved the message.

N et P pour aller au message suivant et précédent non lu.
H pour afficher le header en entier.
M pour ne pas afficher les mime type.
B extract multiple mime.
q quitter le folder actuel.
^ jump to parent ?
S sort
T disable thread => sequence
V move to virtual folder => filtre.

Pour appliquer sur un thread :
t d pour effacer le thread.
t o pour refile le thread.

Vider la poubelle
.................

Taper E dans la fenêtre des Folder pour supprimer tous les emails de
la poubelle.

Attacher un fichier dans wanderlust
...................................

Pour attacher un fichier il suffit d'utiliser cette commande.
It uses "MIME edit" mode; the specific command you're looking for is
C-c C-x TAB (mime-edit-insert-file).

FAQ
...

http://wiki.gohome.org/wl/?Behaviors

box/unbox
.........

http://www.emacswiki.org/emacs-jp/hgw-init-wl.el


Dans la fenêtre summary messages les marques temporaires sont ::

  * pour marquer on peut exécuter une commande, m key
  d pour dispose, d key
  D force delete, D key
  o to refile
  O to refile sans effacer les message
  i prefetch ?
  ~ resend
  x execute action sur les messages marqués par *

Les marques persistantes sont ::

  N, n nouveau message
  U, u unread
  ! déjà lu
  A, a déjà répondu
  F, f forwarded
  $ global flag

Pour lire un message tape ``espace`` pour synchroniser cette fenêtre
taper ``s``.
N ou n pour sauter au prochain message non lu.
Taper j pour entrer dans le buffer des messages.

You can pack the message numbers in Summary by M-x wl-summary-pack-number. ???

taper / pour ouvrir/fermer un thread.
taper [ pour ouvrir tous les threads.
taper ] pour fermer tous les threads

a pour répondre à un message.
A pour répondre à un message en reprennant le message.

Toute les raccourcis de la fenêtre summary : http://www.gohome.org/wl/doc/wl_82.html#SEC82

Dans le message buffer :
n pour passer de section en section.
p pour revenir sur la précédente section.
l pour supprimer l'afficher de la fenêtre summary.

Buffer d'édition C-c C-z pour quitter le buffer et le sauvegarder dans draft.
C-c C-c pour envoyer le message.

Intégration GPG & wanderlust
----------------------------

http://box.matto.nl/wanderlustgpg.html

intégration mu & wanderlust
---------------------------

http://permalink.gmane.org/gmane.mail.wanderlust.general.japanese/7071

Interaction yank, kill et le clipboard X11
------------------------------------------

Pour une interraction active entre Ctrl-k (kill), Alt-w et le
clipboard X11. Il faut positionner ceci dans votre .emacs ::

    (setq x-select-enable-clipboard t)

Info trouvé à cette page http://www.emacswiki.org/emacs/CopyAndPaste#toc2

Avec ces commentaires ::

   (setq mouse-drag-copy-region nil)  ; stops selection with a mouse being immediately injected to the kill ring
   (setq x-select-enable-primary nil)  ; stops killing/yanking interacting with primary X11 selection
   (setq x-select-enable-clipboard t)  ; makes killing/yanking interact with clipboard X11 selection


Configuration du mode ReST
--------------------------

Pour avoir des raccourcis sur F1, F4 et F5 il faut avoir ceci dans son
init.el ::

    (add-hook 'rst-mode-hook
           (lambda ()
            (local-set-key (quote [f1]) (quote rst-adjust-decoration))))

    (add-hook 'rst-mode-hook
           (lambda ()
            (local-set-key (quote [f4]) (quote rst-toc))))

    (add-hook 'rst-mode-hook
           (lambda ()
            (local-set-key (quote [f5]) (quote rst-display-decorations-hierarchy))))

mutt & notmuch
==============

A regarder pour indexer les emails.
http://upsilon.cc/~zack/blog/posts/2011/01/how_to_use_Notmuch_with_Mutt/
http://upsilon.cc/~zack/blog/posts/2011/01/how_to_use_Notmuch_with_Mutt/mutt-notmuch.1.html

java
====

Selectionner l'environnement java sous debian ::

    sudo update-alternatives --config java

exécuter un jar ::

    java -jar mon_fichier.jar

Red Hat
=======

Configuration interface réseau ::

   system-config-network (avec ou san X11)

ou alors utiliser les scripts dans ``/etc/sysconfig/network-scripts/``


Applications DVD, CD
====================

Formater un CDRW
----------------

La commande à utiliser est ::

   wodim -v -dev=/dev/cdrw blank=fast


Convertir mp3 au format cdr ::

    mpg123 --cdr ma_chanson.cdr ma_chanson.mp3
    wodim -v -dev=/dev/cdrw -dao -audio -pad track1.cdr track2.cdr track3.cdr [etc.]


Re-encodage pour ipad
---------------------

Utiliser cette commande pour passer de mkv de 2 Go (pour un épisode de 50mn = Qualité BlueRay) à 700Mo ::

   mencoder engrenages.s04e05.french.720p.bluray.x264-jmt.mkv -o o5_1500.mpeg -vf scale=720:576,harddup -of mpeg -mpegopts format=dvd:tsaf -oac lavc -ovc lavc -lavcopts acodec=ac3:abitrate=448:vcodec=mpeg2video:vrc_buf_size=1835:vrc_maxrate=9800:vbitrate=1500:keyint=15:vstrict=0:aspect=16/9 -lavdopts threads=2 -ofps 25 -srate 48000 -af lavcresample=48000

Utiliser ffmpeg
---------------

Pour Vincent, convertir un fichier avi en fichier mpeg ::

     ffmpeg -i bon.avi -target pal-dvd bon.mpeg

Encoder en qualité DVD avec ffmpeg ::

     ffmpeg -i mon_fichier.avi -target pal-dvd -aspect 16:9  -sameq fichier_resultat.mpeg


Pour encoder un avi en fichier mpeg totalement compatible avec le
format DVD ::

      mencoder 308.avi -o ~/308_true2.mpeg -utf8 -sub 308.srt -subpos 97 -fontconfig -font Arial -subfont-text-scale 2.5 -vf scale=720:576,harddup -of mpeg -mpegopts format=dvd:tsaf -oac lavc -ovc lavc -lavcopts acodec=ac3:abitrate=448:vcodec=mpeg2video:vrc_buf_size=1835:vrc_maxrate=9800:vbitrate=5000:keyint=15:vstrict=0:aspect=16/9 -ofps 25 -srate 48000 -af lavcresample=48000


Pour encoder un fichier avi ou mkv totalement compatible avec le format DVD
et en **haute qualité** ::

    mencoder 309.avi -o /virt/series/309_true2.mpeg -utf8 -sub 309.srt -subpos 97 -fontconfig -font Arial -subfont-text-scale 2.5 -vf scale=720:576,harddup -of mpeg -mpegopts format=dvd:tsaf -oac lavc -ovc lavc -lavcopts acodec=ac3:abitrate=448:vcodec=mpeg2video:vrc_buf_size=1835:vrc_maxrate=9800:vbitrate=5000:keyint=15:vstrict=0:aspect=16/9:trell:mbd=2:precmp=2:subcmp=2:cmp=2:dia=-10:predia=-10:cbp:mv0:vqmin=1:lmin=1:dc=10 -ofps 25 -srate 48000 -af lavcresample=48000

.. note:: Le fichier des sous-titre .srt doit être encodé en UTF8.
          Pour choisir une piste audio au sein d'un fichier mkv utiliser l'option -aid nr_track

Encoder un avi en mpeg2 (DVD) avec mencoder en **haute qualité** avec
sous-titres ::

     mencoder 303.avi -o tryXX.mpeg -utf8 -sub 303.srt -subpos 97 -fontconfig -font Arial -subfont-text-scale 2.5 -vf scale=720:576,harddup -of mpeg -mpegopts format=dvd:tsaf -oac lavc -ovc lavc -lavcopts acodec=ac3:abitrate=448:vcodec=mpeg2video:vrc_buf_size=1835:vrc_maxrate=9800:vbitrate=8000:keyint=15:trell:mbd=2:precmp=2:subcmp=2:cmp=2:dia=-10:predia=-10:cbp:mv0:vqmin=1:lmin=1:dc=10:vstrict=0:aspect=16/9

Pour encoder un avi en mpeg2 (DVD) avec mencoder en bonne qualité et
avec sous-titres ::

     mencoder 303.avi -o tryXX.mpeg -utf8 -sub 303.srt -subpos 97 -fontconfig -font Arial -subfont-text-scale 2.5 -vf scale=720:576,harddup -of mpeg -mpegopts format=dvd:tsaf -oac lavc -ovc lavc -lavcopts acodec=ac3:abitrate=448:vcodec=mpeg2video:vrc_buf_size=1835:vrc_maxrate=9800:vbitrate=5000:keyint=15:vstrict=0:aspect=16/9


Les options suivantes ont été supprimées ::

     trell:mbd=2:precmp=2:subcmp=2:cmp=2:dia=-10:predia=-10:cbp:mv0:vqmin=1:lmin=1:dc=10

Pour les sous-titres on peut mettre un bandeau ::

     -sub-bg-alpha 100 : ajoute un fond gris au sous-titrage; les valeurs possibles vont de 0 à 255 (0 désactive le fond; ensuite, plus le nombre augmente, plus la transparence augmente).

.. note:: une ressource utile sur mencoder http://www.mplayerhq.hu/DOCS/HTML/en/menc-feat-vcd-dvd.html

encoder un avi en mpeg2 avec ffmpeg ::

     ffmpeg -i mon_fichier.avi -target pal-dvd -aspect 16:9  -sameq mon_fichier.mpeg


Ajouter une piste de sous-titre à un fichier mkv
------------------------------------------------

La commande à utiliser est la suivante ::

  mkvmerge -o test.mkv "Sherlock.s01e02.The.Blind.Banker.480p.x264-MiNi.mkv" --language "0:fr" --track-name "0:francais" -s 0 -A "Sherlock - 1x02 - The Blind Banker.HDTV.Fov.fr.srt"

Créer un nouveau fichier mkv de zéro, ne possédant qu'un seul sous-titre ::

  mkvmerge -o new_file.mkv -S "Sherlock.s01e02.The.Blind.Banker.480p.x264-MiNi.mkv" "Sherlock - 1x02 - The Blind Banker.HDTV.Fov.fr.srt"

Ajouter sous-titre avec

Transformer fichier mkv en dvd avec sous-titre.
-----------------------------------------------

Le problème du mkv c'est le son voici les étapes à réaliser.

Première étape extraction de la piste 2 qui est le son ::

   mkvextract tracks  game01.mkv 2:test.ac3

deuxième étape encodage en haute qualité au format DVD.


En haute qualité avec sous-titre :
   mencoder game01.mkv -o h4_sound.mpeg     -utf8 -sub g1_u8.sub -subpos 97 -fontconfig -font Arial -subfont-text-scale 2.5     -vf scale=720:576,harddup -of mpeg -mpegopts format=dvd:tsaf     -audiofile test.ac3 -oac lavc -ovc lavc     -lavcopts vcodec=mpeg2video:vrc_buf_size=1835:vrc_maxrate=9800:vbitrate=5000:keyint=15:vstrict=0:aspect=16/9:trell:mbd=2:precmp=2:subcmp=2:cmp=2:dia=-10:predia=-10:cbp:mv0:vqmin=1:lmin=1:dc=10     -ofps 25 -srate 48000 -af lavcresample=48000

Encodage plus léger en terme de qualité.


extraction sous-titre depuis mkv
--------------------------------

utiliser la commande mkvinfo pour obtenir les informations ::

  mkvinfo fichier.mkv

Chercher ces informations ::

      + A track
     |  + Track number: 3 (track ID for mkvmerge & mkvextract: 2)
     |  + Track UID: 3270254256
     |  + Track type: subtitles
     |  + Lacing flag: 0
     |  + Codec ID: S_TEXT/UTF8
     |  + Language: und

Ensuite utiliser la commande suivante pour extraire ::

   mkvextract tracks Gravity.mkv 2:grv.srt


Blue-Ray et ré-encodage pour DVD
--------------------------------

mencoder permet cela avant tout il faut identifier l'identifiant de la
piste audio via la commande ::

    mplayer -identify -frames 0 -vc null -vo null -ao null 00001.m2ts | egrep -e "ID_AUDIO_ID|ID_AID"

Le résultat est ::

    ID_AUDIO_ID=4353
    ID_AID_4353_LANG=eng
    ID_AUDIO_ID=4352
    ID_AID_4352_LANG=fra

pour encode en haute qualité vers dvd ::

    mencoder 00001.m2ts -o /virt/series/cars2.mpeg -aid 4352 -vf scale=720:576,harddup -of mpeg -mpegopts format=dvd:tsaf -oac lavc -ovc lavc -lavcopts acodec=ac3:abitrate=448:vcodec=mpeg2video:vrc_buf_size=1835:vrc_maxrate=9800:vbitrate=5000:keyint=15:vstrict=0:aspect=16/9:trell:mbd=2:precmp=2:subcmp=2:cmp=2:dia=-10:predia=-10:cbp:mv0:vqmin=1:lmin=1:dc=10 -ofps 25 -srate 48000 -af lavcresample=48000

image magick
------------

Remplacer fond transparent par un fond blanc ::

  convert -flatten img1.png img1-white.png

Rotation d'une image ::

  convert -rotate 270 img1.png img1-rotate.png

convertir un fichier en utf8
----------------------------

Convertir un fichier texte en utf8 pour cela utiliser la commande ::

    iconv -f iso-8859-15 -t utf-8 g2.srt > g2_u8.srt

Image iso et DVD
----------------

Générer une image iso ::

     genisoimage -V "test" -o image.iso -udf -graft-points t03.mpeg

Divers commande DVD
-------------------

information sur le CD/DVD à graver ::

    dvd+rw-mediainfo /dev/dvd

effacer/formater rapide d'un DVD ::

    dvd+rw-format -force /dev/dvd

effacement/formater complet d'un DVD ::

    dvd+rw-format -force=full /dev/dvd

Graver un cd/dvd ::

    growisofs -dvd-compat -Z /dev/dvd=image.iso
    wodim -v dev=/dev/dvd -data g.iso

Utiliser l'option -dvd-compat permet de clore définitive la session.
Ce qui apporte une meilleure compatibilité.

A priori l'option -speed=2 permet de fixer une vitesse de gravage.


Comment copier un cdrom
-----------------------

La commande la plus simple est `dd` ::

  dd if=/dev/cdrom of=mon_fichier.iso


Comment copier un dvd
----------------------

Utiliser la commande ``vobcopy`` pour réaliser une copie exacte (raw
copie) ::

   mkdir mon_dvd_copy
   cd mon_dvd_copy
   vobcopy -m

Ensuite generer l'image iso ::

   genisoimage -dvd-video -o filename2.iso DIR_CONTENANT_VIDEO_TS

Graver l'image iso ::

   growisofs -dvd-compat -Z /dev/dvd=image.iso
   growisofs -dvd-video -Z /dev/dvd=image.iso


Ultiliser dvdauthor
-------------------


Comment réaliser un DVD vidéo ::

    mkdir mon_dvd
    dvdauthor -o mon_dvd/ -x mon_dvd.xml

l'option ``-n`` permet de simuler (dry) l'exécution de la commande
dvdauthor.

Le fichier mon_dvd.xml pour avoir une source avec deux chapitres est
le suivant ::

    <dvdauthor>
        <vmgm />
        <titleset>
            <titles>
                <pgc>
                    <vob file="aa_ff.mpeg" />
                    <vob file="ab_ff.mpeg" />
                </pgc>
            </titles>
        </titleset>
    </dvdauthor>


Attention si vous avez ce message d'erreur ::

    dvdauthor -x l6.xml -o dvd2
    DVDAuthor::dvdauthor, version 0.7.0.

    INFO: no default video format, must explicitly specify NTSC or PAL
    ...
    INFO: Scanning dvd2/VIDEO_TS/VTS_01_0.IFO
    ERR:  no video format specified for VMGM

Il faut exporter cette variable ``export VIDEO_FORMAT=PAL``.

effacer/formater rapide d'un DVD ::

    dvd+rw-format -force /dev/dvd

Ensuite reste à graver le dvd à partir du répertoire contenant TS_VIDEO::

    growisofs -Z /dev/dvd -dvd-video dvd/

.. note:: informations sur mencoder http://www.mplayerhq.hu/DOCS/HTML/fr/mencoder.html

Lire un répertoire de type dvd avec xine ::

    xine dvd://virt/series/mon_rep_dvd


.. note:: Un tutorial intéressant sur dvdauthor est http://www.tappin.me.uk/Linux/dvd.html

Ajout de bandes noires ::

    ffmpeg -i dans_la_brume.avi -sameq -vf pad=0:360:0:42:black t1.avi

Passage d'une vidéo avi au format 640x272 en 640x360.


RIP DVD
-------


Pour cela utiliser la commande suivante pour obtenir un encodage en une passe ::

  mencoder dvd://2 -alang en -slang fr -oac mp3lame -lameopts q=0:aq=0 -ovc xvid -xvidencopts fixed_quant=2:autoaspect -fontconfig -font Arial -o breaking_bad_e05.avi

Le //2 permet de selectionner le second chapitre.

Voir ici pour des informations complémentaires :
http://savvyadmin.com/dvd-to-xvid-encoding-with-mencoder/
http://en.gentoo-wiki.com/wiki/Mencoder
http://blog.pantokrator.net/2006/09/25/encoding-dvd-to-mpeg-4-avi-using-mencoder/
http://martin.ankerl.com/2008/12/25/ripping-multilanguage-dvds-with-subtitles-using-only-mencoder/
http://www.gentoo-wiki.info/MEncoder/Rip_DVD


Convertir ac3, aac en wav
-------------------------

La commande est ::

  mplayer -ao pcm a.ac3 -ao pcm:file="sound.wav"

Pad black color avec ffmpeg :

http://ubuntuforums.org/showthread.php?t=702188


Aspect ratio :
http://darkness.codefu.org/wordpress/tag/dvdauthor/

réaliser un dvd à creuser/todo
http://lists.mplayerhq.hu/pipermail/ffmpeg-user/2006-March/002564.html
http://kylecordes.com/2006/dvd-ffmpeg
http://tuxicity.wordpress.com/2006/12/01/avi-to-dvd-with-ffmpeg-and-dvdauthor/

faire vos propre DVD. dvdauthor
http://dvdauthor.sourceforge.net/
http://radagast.bglug.ca/linux/dvd_authoring/dvd_authoring.html

Encodage DV/ DVD etc...
http://www.tappin.me.uk/Linux/dvd.html

Pas mal d'option pour ffmpeg
http://rodrigopolo.com/ffmpeg/cheats.html

Padding option dans ffmpeg
http://www.mahalo.com/answers/please-explain-the-new-pad-syntax-in-ffmpeg
http://lists.mplayerhq.hu/pipermail/ffmpeg-user/2006-October/004648.html

Label de pochette de CD, DVD
----------------------------

L'application en ligne de commande est ``cdlabelgen`` ::

    cdlabelgen -c Test -s Title -f r.txt -o cover.ps


TO DO
=====

Macro emacs pour entourer le mot de `` et `` pratique en ReST.
http://xahlee.org/emacs/elisp_idioms.html

Documenter blue ray
http://kemovitra.blogspot.com/2010/04/using-mplayer-mencoder-to-rip-blu-ray.html
Identifier l'id de la piste audio
mplayer 00001.m2ts -vo direct3d -vc ffvc1 -vf cropdetect -ss 180 -identify


Matos
=====

Chaise
http://www.miximum.fr/tranche_vie/391-quelle-chaise-pour-developper%C2%A0

Radio
=====

Des papous dans la tête
-----------------------


Téléchargement possible des podcasts à cette adresse ::

  http://www.touslespodcasts.com/annuaire/culture/poesie/120-episode614579.html
  http://www.touslespodcasts.com/annuaire/culture/poesie/120.html





Subtitle outils
http://archive09.linux.com/feature/125978
