***
Git
***

Création de dépôts
==================

Dépôt local
-----------

Pour créer un dépôt local ::

  git init .

Cette va créer un dossier .git dans le répertoire courant.
Ensuite à vous d'ajouter les fichiers que vous souhaiter versionner.


Dépôt distant
-------------

Création d'un répertoire ayant pour extension .git ::

  mkdir foo-project.git

Se positionner dans ce répertoire ::

  cd foo-project.git

Initialiser ce répertoire ::

  git --bare init

Si on veut s'amuser sur son propre PC tout en simulant un dépôt distant, on peut faire usage la synatxe file:/// ::

  git clone file:///full/pathname/foo-project.git
  cd foo-project

Info sur le dépôt distant
=========================

Pour obtenir des informations sur le/les dépôts distants utiliser cette commande ::

  git remote -v

Corriger l'url distante vous avez cloné un dépôt en http et vous voulez passer
au protocole git (ou ssh) ::

  git remote set-url origin git@github.com:username/repo.git

Fecth et voir les différences
-----------------------------

Identifier les différences du dépôt distant ::

  git fetch
  git diff origin/master

Ensuite merge si on le souhaite ::

  git merge origin/master


Supprimer un repo distant (remote)
----------------------------------

Utiliser la commande ::

  git remote rm origin


Identifier les fichiers d'un commit
-----------------------------------
La commande est ::

  git ls-tree --name-only -r SHA1


Gestion de l'index
==================

Ajouter tous les fichiers ayant .rst en suffix ::

   git add *.rst

Supprimer un fichier de l'index ::

   git rm --cached FILE

Ajouter tous les fichiers ::

   git add -all

Pour ajouter un fichier dans l'index ::

   git add filename.txt

Ajouter une partie de fichier ::

  git add -i
  ensuite patch
  selectionner le fichier
  et y pour ajouter un hunk

Pour retirer un fichier de l'index ::

   git reset HEAD test.txt

Quels sont les fichiers modifiés au sein répertoire de travail qui
ne sont pas dans l'index ::

   git diff
   git diff --stat

Annulation des modifications
============================

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

Historique & Recherches
=======================

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

Rechercher
----------

Chercher dans le log avec un regexp ::

  git log --grep "<PATTERN>"

l'option -E permet d'activer l'extend grep.

Chercher dans le code au niveau de toutes les révisions la STRING avec l'option -G ou -S::

  git log --stat -G'STRING'
  git log -p -S'STRING'

Chercher une chaine de caractère qui a été effacé au sein du code ::

  git log -p -S'STRING' --diff-filter=D

Chercher dans les fichiers du répertoire de travail mais uniquement pour les fichiers sous révision ::

  git grep -e 'STRING'

Chercher uniquement dans les fichiers ayant l'extension .c ::

  git grep -e 'STRING' -- '*.c'

Pour chercher une string uniquement dans les fichiers contenus dans l'index ::

  git grep --cached -e 'STRING' -- '*.c'

Pour chercher une string pour un commit donné ::

  git grep -e ';;' SHA1 -- '*.c'

Traiter les diffréneces
=======================

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


Utilisation de difftool
=======================

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

Comparer une version antérieur avec la version du working directory ::

  git difftool 9572205 test.txt

Pour comparaison avec la dernière version commité ::

  git difftool test.txt


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

Réaliser une archive
--------------------

la commande est de ce type ::

  git archive --format=zip --prefix=SQL_exo/ SQL: -o ../SQL_exo.zip

C'est la syntaxe `SQL:` qui donne le nom de la branche pour laquelle on souhaite réaliser une archive.
L'option `-o` indique le nom du fichier de sortie.

Ne pas oublier le `/` à la fin du SQL_exo car sinon ça devient un prefix pour tous les fichiers qui seront inclus dans le zip.


Travailler avec les branches
============================

Pour créer une branche ::

  git branch ma_branche

Pour créer et se positionner directement dans la branche utiliser la commande suivante ::

  git checkout -b ma_branche

Pour se placer dans la branche ::

  git checkout ma_branche

Pour créer une branche sur un ancien commit ::

  git branch ma_branche 96a31f2314c091121996
  git checkout -b ma_branche 96a31f2314c091121996

Voir les branches ::

  git branch -a

Copier/dupliquer une branche existante ::

  git branch copie_branche branche_existante


Pousser une nouvelle branche vers le dépôt d'origine ::

  git push --set-upstream origin ma_nouvelle_branche


Vérifier que la branche bien été poussée ::

  git remote show origin

Suivre une branche d'un dépôt distant ::

  git checkout -b ma_branche origin/ma_branche

Supprimer localement une branche ::

  git branch -d la_branche_a_supprimer

Supprimer la branche distante ::

  git push origin --delete la_branche_distante

résultat en sortie ::

  To https://github.com/dojo-toulouse/elixir-koans
  - [deleted]         anonymous_functions

Récupérer un fichier d'une branche sur une autre
------------------------------------------------

Pour cela checkout ::

  git checkout ma_branche
  git checkout master -- filename.txt


Réaliser les opérations de merge
================================

Lorsqu'il y a un conflit utiliser ::

  git ls-files -u

permet d'identifier les fichiers en conflits (qui sont à merger) ou alors utiliser ::

  git status

Ensuite lancer l'outil de résolution de merge via ::

  git mergetool

Pour cela il faut avoir configuré git pour qu'il utilise votre outil préféré.
Voir ma configuration, j'utilise meld mais il existe bon nombre de solutions à
commencer par le vénérable vimdiff ou kdiff3 ainsi que la solution commerciale
p4merge.


Rebase
======

Comment rebaser la branche bleue sur master ::

  git checkout bleue
  git rebase master

Une bonne idée est de dupliquer la branche que l'on rebase ici la branche bleue ::

  git branch copie_bleue bleue
  git checkout bleue
  git rebase master

Maintenant nous souhaitons amener master au niveau du dernier commmit de la branch bleue
afin d'avoir un historique linéaire ::

  git checkout master
  git rebase bleue

Voir exemple ici http://mettadore.com/analysis/a-simple-git-rebase-workflow-explained/


Resources également intéressant à étudier :

- http://randyfay.com/content/rebase-workflow-git
- http://gitready.com/intermediate/2009/01/31/intro-to-rebase.html
- http://labs.excilys.com/2012/02/28/preparez-vous-a-reecrire-lhistoire-avec-git-rebase/
- http://alx.github.io/gitbook/4_recombinaison_(rebase).html
- http://git-scm.com/book/fr/Les-branches-avec-Git-Rebaser

Pull, Push et Synchronisation
=============================

Synchronisation avec un dépôt forké
-----------------------------------

Vous avez cloné un dépôt depuis github et vous souhaitez le synchroniser pour cela il vous procéder ainsi.

Premièrement ajoute le dépôt à l'origine du fork, par exemple ::

  git remote add upstream https://github.com/dojo-toulouse/elixir-koans

On peut vérifier par un `git remote -v` que l'url d'accès a été ajoutée.

Maintenant réalisons un fetch pour récupérer les modifications ::

  git fetch upstream

Le résultat attendu est quelque chose de ce type ::

  remote: Counting objects: 19, done.
  remote: Compressing objects: 100% (11/11), done.
  remote: Total 13 (delta 6), reused 8 (delta 2)
  Unpacking objects: 100% (13/13), done.
  From https://github.com/dojo-toulouse/elixir-koans
   * [new branch]      master     -> upstream/master

Nous avons récupéré les données de la branch master en local,
ces données étant stockés dans la branche locale upstream/master.

Pour voir toutes les branches la commande suivante est pratique ::

  git branch -va

Il est maintenant temps de réaliser le merge avec notre branche master ::

  git checkout master
  git merge upstream/master

Le résultat attendu est quelque chose de ce type ::

  Updating 2a3fcc4..bf7f71f
  Fast-forward
   README.md                      |  2 +-
   about_anonymous_function.exs   | 39   +++++++++++++++++++++++++++++++
   about_lists.exs                |  4   ++++
   about_numbers_and_booleans.exs | 54   +++++++++++++++++++
   todo/about_regex.exs           |  4   ++++
   5 files changed, 102 insertions(+),   1 deletion(-)
   create mode 100644 about_anonymous_function.exs
   create mode 100644 todo/about_regex.exs

Il ne nous reste plus qu'a réaliser un `git push` ::

   git push

Voila c'est terminé.

La serie d'opération est inspirée de ce lien https://help.github.com/articles/syncing-a-fork

Identifier les commits de différence entre le local et le remote
================================================================

Verifier si tous les commits sont poussés, trois solutions

solution 1 ::

  git fetch
  git diff --stat origin/master..

solution 2 ::
  git fetch
  git diff origin/master..HEAD

solution 3 ::
  git push --dry-run

Voir les commits présents dans origin/master et non présent dans master (non tirés) ::
  
  git fetch
  git log master..origin/master

Voir les commmits présents dans master et non présent dans origin/master (non poussés)

  git fetch
  git log origin/master..master


Voir également ici
http://stackoverflow.com/questions/7057950/commit-differences-between-local-and-remote

commit vide
-----------

l'option à utiliser est --allow-empty
Pour commencer avec un dépôt vide, ayant un premier commit vide ::

   git commit --allow-empty -m "Message"


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

.. _eol_git: https://help.github.com/articles/dealing-with-line-endings

Voir à cette adresse _eol_git

Configurer meld
---------------

Pour configurer meld afin de l'utiliser lors de la résolution des merges, voici
ma configuration ::

   [merge]
   tool = mymeld
   [mergetool "mymeld"]
   cmd = meld --diff $BASE $LOCAL --diff $BASE $REMOTE --diff $LOCAL $MERGED $REMOTE

C'est inspiré de la configuration disponible à cette adresse http://lukas.zapletalovi.com/2012/09/three-way-git-merging-with-meld.html

Je n'ai pas encore testé cette configuration ::

  # Autre config à tester
  #[merge]
  #tool = mymeld
  #conflictstyle = diff3
  #[mergetool "mymeld"]
  #cmd = meld --diff $BASE $LOCAL --diff $BASE $REMOTE --diff $LOCAL $BASE $REMOTE $MERGED

  #Ou bien utiliser cette configuration
  #[mergetool "mymeld"]
  #cmd = meld $LOCAL $BASE $REMOTE -o $MERGED --diff $BASE $LOCAL --diff $BASE $REMOTE

Les outils à étudier pour réaliser des merges sont kdiff3 qui semble avoir des algorithme plus poussés.
Regarde également p4merge.
Voir à cet url http://stackoverflow.com/questions/572237/whats-the-best-three-way-merge-tool
On trouve au sein de cet url ces articles
article sur p4merge http://www.geekgumbo.com/2010/05/11/perforces-p4merge-file-comparison-editor-a-review/

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


Configuration github
====================
Pour configurer l'authentifcation github sur un débpôt local donné ::

  vi .git/config 
  modifier remote "origin"
  [remote "origin"]
        url = https://acassaigne:PASSWORD@github.com/acassaigne/doc.git

  [user]
        name = acassaigne
        email = anthony.cassaigne@gmail.com

les alias
---------

Quelques alias possibles à définir dans le fichier `.gitconfig` ::

  [alias]
      st = status
      df = diff
      co = checkout
      ci = commit
      br = branch
      amend = commit --amend # editer le dernier commit
      lol = log --graph --decorate --pretty=oneline --abbrev-commit
      lola = log --graph --decorate --pretty=oneline --abbrev-commit --all

Mes alias
+++++++++

Voir les commits non poussés et non tirés ::

  git config --global alias.notpush '!git fetch && git log origin/master..master' 
  git config --global alias.notpull '!git fetch && git log master..origin/master'

Voir à cette url pour les alias lol et lola http://blog.kfish.org/2010/04/git-lola.html

Les alias de log ::

    lol = log --graph --decorate --pretty=oneline --abbrev-commit
    lola = log --graph --decorate --pretty=oneline --abbrev-commit --all
    lp = log --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative
    lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit



Git sous windows
================

Installer msysgit.

Configurer
----------

Vérifier la valeur de la variable $HOME au sein d'un gitbash.

.. code-block:: bash

    echo $HOME

c'est à cet emplacement que vous placerez le fichier ``.gitconfig``

Configuration git difftool sous windows
---------------------------------------

Editeur
+++++++

Configurer l'appel à l'éditeur notepad++ ajouter dans le fichier .gitconfig ::

  [core]
    editor = npp.sh

Et placer ce script shell `npp.sh` dans le répertoire d'installation de
git/bin ::

  #!/bin/sh
  "C:\Program Files\Notepad++\notepad++.exe" -multiInst "$*" 

Winmerge
++++++++

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


p4merge
+++++++

[diff]
  tool = p4merge

[difftool]
  prompt = false

[difftool "p4merge"]
  cmd = "p4merge.exe \"$LOCAL\" \"$REMOTE\""

[merge]
  tool = p4merge

[mergetool "p4merge"]
  cmd =  "p4merge.exe  \"$BASE\" \"$REMOTE\" \"$LOCAL\" \"$MERGED\" "
  keepTemporaries = false
  keepBackup = false

Travailler avec github
======================

Vous avez forké un repo d'un projet ::

  git clone https://gitup/username/repo-forke

La version ssh ::

  git clone ssh://gituser@hostname/home/gituser/anthony_atelier

Autre version sans le prefix ssh mais on passe bien en ssh et en indiquant
un chemin relatif ::

  git clone gituser@little:anthony_atelier


Vous travaillez dans ce repo ::

  git branch new_feature
  git checkout new_feature
  .... working ....

Il faut configurer vers quelle branche vous réalisé le push ::

  git push --set-upstream origin new_feature

Pour les autres push çà sera une simple commande ::

  git push

Ensuite création de la pull request via la commande hub ::

  hub pull-request -m "Message de la pull request" -b user_origine_repo:master

ou ::

  hub pull-request -m "Message de la pull request" -b user_origine_repo:master -h my_username:new_feature

Résultat en sortie ::

  https://github.com/dojo-toulouse/elixir-koans/pull/6

Création de la pull request 6 pour le dépôt appartenant à user_origine_repo !

A regarder la commande hub écrite en ruby ::

  hub

url https://github.com/github/hub

Pour l'installer ::

   git clone https://github.com/github/hub
   cd hub
   sudo rake install

Consulter également cette url :   http://tck.io/posts/github_and_workflows.html
http://stackoverflow.com/questions/15302570/automatically-open-a-pull-request-on-github-by-command-line


Pull request et corrections
---------------------------

Pull request et branch, apporter des corrections à une PR.
Voir les informations ci-dessous.
http://stackoverflow.com/questions/7947322/preferred-github-workflow-for-updating-a-pull-request-after-code-review

Autre commandes git
===================

Compresser le repo git
----------------------

Quand git gui indique que la base doit être compressée,
il convient de lancer la commande ::

  git gc

A regarder
----------

A regarder : http://fr.slideshare.net/saharabeara/advanced-git-tutorial
Quelques éléments à reprendre.

A regarder http://osteele.com/archives/2008/05/my-git-workflow

Resource à creuser : https://github.com/github/teach.github.com/blob/gh-pages/courses/_posts/2001-02-25-git-advanced-course.md

Intro pas mal réalisée : https://www.kernel.org/pub/software/scm/git/docs/everyday.html

Quick resource : http://jonas.nitro.dk/git/quick-reference.html

A regarder ``Gerrit`` pour la revue de code.

Cheet-sheet http://www.git-tower.com/blog/git-cheat-sheet/

Sur la staging area :
http://gitolite.com/concepts/uses-of-index.html
http://programmers.stackexchange.com/questions/69178/what-is-the-benefit-of-gits-two-stage-commit-process-staging
http://betterexplained.com/articles/aha-moments-when-learning-git/
http://gitready.com/beginner/2009/01/18/the-staging-area.html

plein d'informations ici : http://sixrevisions.com/web-development/git-tips/
ici aussi http://gitready.com/


todo
git push
configurer git pour cela upstream

Les outils à regarder, ici un lien intéressant sur stackoverflow : http://stackoverflow.com/questions/3847740/list-of-useful-git-tools

Git number, numérote les fichier : https://github.com/holygeek/git-number

article sur le modèle de branche : http://nvie.com/posts/a-successful-git-branching-model/
Revue de code avec gerrit https://code.google.com/p/gerrit/

Explication sur le git diff
http://stackoverflow.com/questions/10950412/what-does-1-1-mean-in-gits-diff-output
http://stackoverflow.com/questions/2529441/how-to-work-with-diff-representation-in-git/2529633#2529633
http://en.wikipedia.org/wiki/Diff#Unified_format

@@ from-file-line-numbers to-file-line-numbers @@
 line-from-either-file
 line-from-either-file...
