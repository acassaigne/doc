********
Markdown
********

Quelques syntaxes
=================

Inspiré par cette url http://progmod.org/tutoriel/3/utilisez-markdown/

Les titres ::

  # Titre niveau 1
  ## Titre niveau 2
  ### Titre niveau 3
  ...
  ###### Titre niveau 6 (le maximum)

Url
---

Les liens ::

  [Exemple](http://example.com)
  [Exemple](http://example.com "Un super site que vous devriez visiter")
  <http://example.com>


Les liens par référence ::

Pour le site [Zatras][1] et son [Share Blog][2], vous pouvez me contacter via la [page contact][3].

Et je place le texte suivant n'importe où dans ma page:

[1]: http://www.zatras.com/ "Page d'accueil de Zatras.com"
[2]: http://www.zatras.com/~share "Accueil du Zatras Share Blog"
[3]: http://www.zatras.com/~share/info/contact "Page de contact"


Images
------

exemple de syntaxe ::

     ![Texte alternatif si l'image ne s'affiche pas](/chemin/image.jpg "Titre optionnel")

Images par référence ::

    ![Texte alternatif][identifiant]

    [identifiant]: /mon/long/tres/long/chemin/vers/mon/image-qui-est-belle-et-jolie.jpg "Titre optionnel"

Gras et italique
----------------

Gras et italique ::

texte en italique ``_exemple italique_`` ou ``*texte en italique*`` pour du
texte en gras ``**exemple de texte en gras**``
Pour protéger un caractère * positionner un ::

   \*

Pour introduire du code dans une phrase ::

   `cat mon_fichier.txt`

Programmes
==========

Pévisualiser les markdown node et module gfms