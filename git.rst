***
Git
***

Pour Windows
============

Installer msysgit.

Configurer
----------

Vérifier la valeur de la variable $HOME au sein d'un gitbash.

.. code-block:: shell

    echo $HOME

c'est à cet emplacement que vous trouverez le fichier ``.gitconfig``

Identifier les fichiers d'un commit
-----------------------------------
La commande est ::

  git ls-tree --name-only -r SHA1


Gestion de l'index
------------------

Pour ajouter un fichier dans l'index ::

   git add filename.txt

Pour retirer un fichier de l'index ::

   git reset HEAD test.txt

Est-ce des fichier dans la Working Directory qui ne sont pas dans l'index ::

  git diff

Annuler toutes les modifications
--------------------------------

Pour retourner au dernier commit en ANNULANT TOUTES LES MODIFICATIONS,
il y a DONC PERTE POTENTIELLE DE DONNEES ::

  git reset --hard HEAD

Annuler les modifications
-------------------------

.. note:: ATTENTION la commande revert ne sert pas du tout à cela.

Récupérer une version d'un fichier via checkout ::

  git checkout 5b3bbf4 test.txt

Récupérer une version d'un fichier via show ::

  git show SHA1:./filename.txt > old_file.revision.SHA1.txt
  cat old_file.revision.SHA1.txt

Il faut utiliser le chemin complet ::

  git show 27cf8e84bb88e24ae4b4b3df2b77aab91a3735d8:full/repo/path/to/my_file.txt

Pour revenir sur une version ::

  git checkout SHA1 filename_to_restore
  git checkout -- mon_fichier.txt

Suivre les modifications d'un fichier
-------------------------------------

la commande log permet de voir l'historique ::

  git log
  git shortlog

elle peut s'appliquer à un fichier ::

  git log filename.txt

l'option --stat permet d'obtenir le nombre de modifications ::

  git log --stat filename.txt

résultat ::

  Author: Anthony Cassaigne <anthony.cassaigne@gmail.com>
  Date:   Thu Nov 7 09:44:49 2013 +0100

      remove salut, replace by bonjour

   test.txt | 2 +-
   1 file changed, 1 insertion(+), 1 deletion(-)

ou si on veut les différences au format patch ::

  git log -p filename.txt
  git log --follow --all -p filename.txt

l'option follow permet de suivre les renames.

Voir les différences DIFF
-------------------------
Vous pouvez également utiliser l'option --stat pour obtenir
les différences en nombre de lignes.

la commande ::

   git diff

donne la différence entre WORKING DIRECTORY et l'INDEX (staging zone).

La commande ::

  git diff --cached

donne la différence entre l'INDEX et HEAD

La commande ::

  git diff HEAD

Donne la différence entre la HEAD et WORKING DIRECTORY.
(possiblement incluant les modif de l'index, à valider.)

voir url http://www.gitguys.com/topics/git-diff/


Voyage dans le temps
====================

Utiliser la zone de staging pour récupérer une version.
Poser un tag sur votre version actuelle car nous allons jouer avec le reset ::

    git tag my_head_tag

on part vers le commit souhaité ::

   git reset SHA1

message retourné ::

  Unstaged changes after reset:
  M       test.txt

On a donc bien la zone de staging qui a changé.
On revient sur notre version en préservant la zone de staging ::

   git reset --soft my_head_tag

On a maintenant la possibilité d'utiliser git diff ou git difftool pour voir les
différences entre la working directory et la zone de staging.

On peut récupérer un fichier de la zone de staging via ces commandes ::

  git ls-files -s

résultat c'est un ls de la zone de staging ::
  $ git ls-files -s
  100644 7811ebf7ac44c1c2972ea1e11662d8cf6be2757e 0       test.txt

On réaliser un cat du blob via cette commande ::

  git cat-file blob 7811ebf

Pour le récupérer on peut faire un ::

  git cat-file blob 7811ebf > ma_old_version.txt


Utiliser les tags
=================

positionner un tag sur le commit courant ::

  git tag mon_tag

Voir les tags ::

  git tag -n

le -n donne le message associé.

la liste des tags avec le SHA1 ::

  git show --summary --oneline --decorate


utilisation de git difftool
---------------------------

Une difftool configuré voici ce qu'il est possible de réaliser.


utiliser ainsi ::

  git difftool filename.txt

donne la différence entre la WORKING DIRECTORY et L'INDEX.

Si on fait un `git add filename.txt` la commande git difftool filename.txt ne donne plus de différence.

Pour voir la différence entre la WORKING DIR et le HEAD du dépot ::

  git difftool HEAD filename.txt

Pour voir la différence entre l'INDEX et le HEAD du dépot ::

  git difftool --cached filename.txt

Voir la différence entre deux commits (prenant en compte toutes les modification entre ces commits) ::

   git difftool 5b3bbf4..00911bd filename.txt

Comparer deux versions d'un fichier ::

  git difftool 5b3bbf4 00911bd test.txt

Générer un patch et appliquer
=============================

Générer un patch ::

  git diff 0da94be  59ff30c > my.patch

Appliquer un patch ::

  git apply my.patch


La commande reset
=================

Permet se balader dans les commits ! Attention on peut perdre des COMMIT !!!
A explorer prudemment.

Identifier les commit orphelin ::

  git fsck --lost-found

On devrait pouvoir le retrouver à condition que le garbage collector ne soit pas passé.

Voir ce lien http://gitready.com/advanced/2009/01/17/restoring-lost-commits.html


Récupérer un fichier d'une branche sur une autre
-------------- ---------------------------------

Pour cela checkout ::

  git checkout ma_branche
  git checkout master -- filename.txt

Autre commandes utiles
======================

lister les fichiers qui ne sont pas sous la gestion de version ::

  git ls-files --others

Liste également les fichiers qui sont en .gitignore
Pour ne pas avoir ces fichiers ajouter l'option --exclude-standard

Supprimer les fichiers non suivi par git,
ATTENTION il y a potentiellement perte de données.

La commande doit être utilisé avec -i pour le mode intéractif
-n pour simuler (c'est bien pour commencer car pas de perte de données)
-f pour lancer réllement la commande ::

  git clean -n

Pour lancer réllement la commande avec donc l'effacement des fichiers ::

  git clean -f

Pour ajouter les fichiers ignorés ::

  git clean -x -f

Pour ajouter les répertoires vides utiliser -d ::

  git clean -x -d

Export son projet dans une archive
----------------------------------

la commande est de ce type ::

  git archive --format=zip --prefix=chemin_prefix_pour_le_zip/ HEAD > filename.zip

Ne pas oublier le / à la fin du chemin_prefix_pour_le_zip car sinon ca devient un prefix pour tous les fichiers
qui seront inclus dans le zip.



Reflog
======

La commande reflog permet de voir TOUTES les commandes passées, dont les amend sur commit.

Configuration
=============

Ne pas convertir le CRLF et LF
------------------------------

Nous souhaitons que tous les fichiers respectent le LF (Unix).
Les commandes sont ::

    git config --global core.autocrlf input
    git config --global core.eol lf

Faut-il tout de même avoir un fichier .gitattributes contenant ceci ::

    * text=lf

Voir à cette adresse _eol_git

.. _eol_git: https://help.github.com/articles/dealing-with-line-endings



Configuration git difftool
--------------------------

Sous Windows
++++++++++++

Configurer git afin d'utiliser winmerge.
Pour cela il faut créer un shell à placer dans un endroit où le PATH windows pointe ::

    #!/bin/sh
    echo Launching WinMergeU.exe: $1 $2
    echo "run win merge $1 $2" > t.log
    "C:/Program Files (x86)/WinMerge/WinMergeU.exe" -e -ub "$1" "$2"

Ensuite configurer le .gitconfig comme ceci ::

   [diff]
       tool = winmerge

   [difftool "winmerge"]
       cmd = "winmerge.sh \"$LOCAL\" \"$REMOTE\""

   [difftool]
     prompt = false

Et c'est tout !

Travailler avec deux ou plus de configuration
---------------------------------------------

Git a deux niveaux de configuration, un niveau global et un niveau par dépôt.

La configuration global se fait avec l'option --global ::

    git config --global user.name "user_at_work"
    git config --global user.email "email_at_work@blah.com"

exemple pour participer au projets apside ::

    git config --global user.name "apsidetoulouse"
    git config --global user.email "cassaigne.0595@apside.net"

Configuration pour un dépôt déterminé ::

    git config user.name "my_personnal_user"
    git config user.email "email_perso@perso.org"

Ces informations spécifiques au dépôt sont stockés dans le fichier .git/config ::

    [remote "origin"]
        url = https://acassaigne@bitbucket.org/acassaigne/doc.git
        fetch = +refs/heads/*:refs/remotes/origin/*
    [user]
        name = acassaigne
        email = anthony.cassaigne@gmail.com

les alias
---------

Dans le fichier .gitconfig ::

  [alias]
      st = status
      df = diff
      co = checkout
      ci = commit
      br = branch
      amend = commit --amend # editer le dernier commit
      lol = log --graph --decorate --pretty=oneline --abbrev-commit
      lola = log --graph --decorate --pretty=oneline --abbrev-commit --all

Voir à cette url pour les alias lol et lola http://blog.kfish.org/2010/04/git-lola.html

Les alias de log :

    lol = log --graph --decorate --pretty=oneline --abbrev-commit
    lola = log --graph --decorate --pretty=oneline --abbrev-commit --all
    lp = log --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative
    lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit

Supprimer un repo distant (remote)
----------------------------------

Pour voir les repos distants configurés utiliser la commande ::

   git remote -v

Utiliser la commande ::

  git remote rm origin

A regarder
----------

A regarder ``Gerrit`` pour la revue de code.

Cheet-sheet http://www.git-tower.com/blog/git-cheat-sheet/

Sur la staging area :
http://gitolite.com/concepts/uses-of-index.html
http://programmers.stackexchange.com/questions/69178/what-is-the-benefit-of-gits-two-stage-commit-process-staging
http://betterexplained.com/articles/aha-moments-when-learning-git/
http://gitready.com/beginner/2009/01/18/the-staging-area.html

plein d'informations ici : http://sixrevisions.com/web-development/git-tips/
ici aussi http://gitready.com/
