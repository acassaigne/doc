Sublime Text 2
**************

Les pluging que j'utilise
=========================

Faisant un usage régulier de pyhton, restructured Text :

- Packages/Perv - Color Scheme/Perv Orange.tmTheme
- MarkdownEditing
- SublimeRope python
- Sublime Text Restructured Text Code Completion (rst)
- Theme utilisé Thomorow Color Schema (Tomorrow Night Eighties)
- EncodingHelper https://github.com/SublimeText/EncodingHelper#readme

A regarder !! http://sametmax.com/liste-des-plugins-sublime-text-que-jutilise/
http://outofmemoryblog.blogspot.fr/2012/08/python-development-with-sublime-text-2.html

Snippet
=======

Pour déterminer le scope à positionner lors de la définition d'une snippet ::

   <scope>text.html.markdown</scope>

Pour identifier le scope il y a le raccourci ctrl+shift+alt+p à taper dans le
fichier source, apparait alors en bas dans la bar de status le scope pour ce
firchier.

On peut également trouver l'information sur cette page :
- https://gist.github.com/iambibhas/4705378

snippets que j'utilise
----------------------

Pour le markdown ::

    <snippet>
      <content><![CDATA[
    ```shell
    ${1:code}
    ```
    ]]></content>
      <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
      <tabTrigger>cc</tabTrigger>
      <!-- Optional: Set a scope to limit where the snippet will trigger -->
      <scope>text.html.markdown</scope>
    </snippet>



Ma configuration
================


Windows
=======

Sous windows les packages installés sont stockées sous %APPDATA% ::

  echo %APPDATA%


Gestionnaire des packages
=========================

à installer en suivant ces instructions : https://sublime.wbond.net/installation#st2

Blog
====
http://shoogledesigns.com/blog/blog/tag/sublime-text-2/

Url
===

- https://gist.github.com/eteanga/1736542
- https://github.com/dbousamra/sublime-rst-completion  (restructured text)

Popularité des packages

- https://sublime.wbond.net/

Pour Markdown
-------------

- http://www.macstories.net/roundups/sublime-text-2-and-markdown-tips-tricks-and-links/
- https://github.com/demon386/SmartMarkdown
- https://github.com/ttscoff/MarkdownEditing


# Sublime Text & Markdown

Installer le package MardownEditing, [voir cette url](https://github.com/SublimeText-Markdown/MarkdownEditing/tree/master) 

## Configuration

Ouvrir le fichier *Markdown.sublime-settings* qui se trouve dans le répertoire des packages. Pour obtenir le répertoire des packages utiliser le *menu preferences->Browse Packages...* ensuite ouvrir le répertoire *MarkdownEditing*

Changer ces valeurs 
```init
"color_scheme": "Packages/MarkdownEditing/MarkdownEditor.tmTheme",
...
"draw_centered": false,
...
"line_numbers": true,
```

Test 
```sql
SELECT * FROM TOTO;
```

Url pluging
-----------

- http://blog.goetter.fr/post/24671859680/sublime-text-2-raccourcis-et-plugins
