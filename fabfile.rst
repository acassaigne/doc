******
fabric
******

Si pratique ce fabric !

Créer un fichier `fabfile.py` dans lequel on va définir une tâche par exemple
synchro_file ::

  from fabric.api import local, lcd

  def synchro_file(filename, msg):
    svn_repo = '~/svn/doc/in_progress'
    local('cp -p {0} {1}'.format(filename, svn_repo))
    with lcd(svn_repo):
      local('svn commit -m "%s"' % msg)

Pour lancer cette tâche il suffit de lancer cette commande ::

   fab synchro_file:git.rst,"typo corrections"

ou ::

   fab nemo:filename=git.rst,msg="typo corrections"