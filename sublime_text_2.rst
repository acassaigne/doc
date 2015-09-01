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

Shortcut
========

## file manager
ctrl+n new file
ctrl+shift+s save as

## interface
ctrl+k ctrl+b side bar show/hide
ctrl+0 focus side bar

F11 fullscreen
shift+F11 full full screen

ctrl+pagedown next tab 
ctrl+tab next tab
ctrl+pageup previous tab
ctrl+shift+tab previous tab 
alt+& panel 1
alt+é panel 2
...

ctrl+p show file panel
ctrl+shift+p command panel 
ctrl+alt+p change project / select workspace

### bookmark 
ctrl+f2 define bookmark 

F2 next bookmark
shift+F2 previous bookmark

ctrl+shift+f2 clear bookmark

alt+f2 select all bookmark

### layout
alt+shift+1 
alt+shift+2 , 3, 4 , 5, 6,7,8

ctrl+& focus group 1
ctrl+é focus group 2
...
ctrl+shift+& move file to group 1
...

ctrl+@ focus side bar 

ctrl+k ctrl+up create new panel 
ctrl+k ctrl+down close panel

## delete word, transpose caracters 

ctrl+backspace delete word backward
ctrl+shift+backspace delete the begining of row

ctrl+t transpose character 
alt+q wrap lines 
ctrl+k ctrl+u upper case word
ctrl+k ctrl+l lower case word 

## mark

ctrl+k ctrl+space set mark 
ctrl+k ctrl+a select to mark 
ctrl+k ctrl+w delete to mark
ctrl+k ctrl+x swap with mark 
ctrl+k ctrl+y yank 
ctrl+k ctrl+g clear bookmarks



## undo, redo, repeat
ctrl+z undo
shift+ctrl+z redo
ctrl+y redo_or_repeat

ctrl+u soft redo what is the difference with redo ?
ctrl+shift+u soft_redo ????

## copy/paste
ctrl+k ctrl+v paste from history !!!

## move 

ctrl+left move to next word
ctrl+right move to backward word
alt+left move to subword 
alt+right move to subword, subword1_subword2 the underscore is separator of subword

shift+home begin of line (remap to ctrl+a)
shift+end end of line (remap to ctrl+e)

ctrl+home begin of file
ctrl+end end of file

ctrl+k ctrl+c move/show to center 

## snippet 

alt+shift+w insert snippet 

## fold/unfold code

ctrl+shift+[ fold code
ctrl+shift+] unfold code

## increase/decrease font
ctrl++ increase font
ctrl+- decrease font 
### smart move in file

ctrl+r goto function, methode... @
ctrl+shift+r goto symbol in project
ctrl+g goto line :
ctrl+; goto word #

F12 goto definition 

alt+- jump back
alt+shift+- jump forward 

### scroll

ctrl+up scroll up line
ctrl+down scroll down line 

## move line

ctrl+shift+up move up line 
ctrl+shift+down move down line

## join line, duplicate
ctrl+j join line
ctrl+shift+d duplicate line

## completion 
alt+/ auto complete, repeate many time 

## indent
ctrl+[ indent
ctrl+] unindent


## switch to column mode

alt+shift+up select line 
alt+shift+down select line 

## complete tag

alt+. close tag

## comment / uncomment 

ctrl+/ comment 
ctrl+shift+/ uncomment 

## selection line, word, expand selection

ctrl+l select line
ctrl+d select word (find word and select)
ctrl+k ctrl+d find next word and select 
ctrl+shift+space expand select to scope ? 

ctrl+shift+m select bracket to bracket
ctrl+shift+j select indentation
ctrl+shift+a select to next tag  

## macro 

ctrl+alt+q start record macro
ctrl+alt+q end record macro 
ctrl+alt+shift+q run macro

ctrl+shift+k run macro file

ctrl+enter run macro file ?
ctrl+shift+enter run macro file ?

## research, incremental, replace

ctrl+i incremental find
ctrl+shift+i incremental find backward 

ctrl+f find panel
f3 find next
shift+f3 find previous
ctrl+f3 find under
ctrl+shift+f3 find under previous
alt+f3 find all

ctrl+e slurp find string, followinf f3 or shift+f3 
ctrl+shift+e slurp replace string ??

ctrl+h replace panel 
ctrl+shift+h replace next 

ctrl+shift+f find in files 
f4 next result 
shift+f4 previous result

### shortcut in panel search, replace, incremental 

alt+c toggle case sensitive
alt+r toggle regex 
alt+w toggle whole word
alt+a preserve case 

enter find next 
shift+enter find previous
alt+enter find all
ctrl+alt+enter replace all

## spell checking 

F6 spell check
ctrl+f6 next misspelling
ctrl+shift+f6 prev misspelling 

## build 
f7 build 
ctrl+b build 

## sort lines 
f9 sort case insensitive
ctrl+f9 sort case sensitive


## question 

{ "keys": ["ctrl+alt+shift+p"], "command": "show_scope_name" },


Config à changer sous windows.
Remap au travail
  { "keys": ["alt+shift+up"], "command": "select_lines", "args": {"forward": false} },
  { "keys": ["alt+shift+down"], "command": "select_lines", "args": {"forward": true} },

remap
{ "keys": ["ctrl+home"], "command": "move_to", "args": {"to": "bof", "extend": false} },
{ "keys": ["ctrl+end"], "command": "move_to", "args": {"to": "eof", "extend": false} },

{ "keys": ["ctrl+]"], "command": "indent" },
{ "keys": ["ctrl+["], "command": "unindent" },

{ "keys": ["ctrl+/"], "command": "toggle_comment", "args": { "block": false } },
{ "keys": ["ctrl+shift+/"], "command": "toggle_comment", "args": { "block": true } },

{ "keys": ["ctrl+1"], "command": "focus_group", "args": { "group": 0 } },
  { "keys": ["ctrl+2"], "command": "focus_group", "args": { "group": 1 } },
  { "keys": ["ctrl+3"], "command": "focus_group", "args": { "group": 2 } },
  { "keys": ["ctrl+4"], "command": "focus_group", "args": { "group": 3 } },
  { "keys": ["ctrl+5"], "command": "focus_group", "args": { "group": 4 } },
  { "keys": ["ctrl+6"], "command": "focus_group", "args": { "group": 5 } },
  { "keys": ["ctrl+7"], "command": "focus_group", "args": { "group": 6 } },
  { "keys": ["ctrl+8"], "command": "focus_group", "args": { "group": 7 } },
  { "keys": ["ctrl+9"], "command": "focus_group", "args": { "group": 8 } },
  { "keys": ["ctrl+shift+1"], "command": "move_to_group", "args": { "group": 0 } },
  { "keys": ["ctrl+shift+2"], "command": "move_to_group", "args": { "group": 1 } },
  { "keys": ["ctrl+shift+3"], "command": "move_to_group", "args": { "group": 2 } },
  { "keys": ["ctrl+shift+4"], "command": "move_to_group", "args": { "group": 3 } },
  { "keys": ["ctrl+shift+5"], "command": "move_to_group", "args": { "group": 4 } },
  { "keys": ["ctrl+shift+6"], "command": "move_to_group", "args": { "group": 5 } },
  { "keys": ["ctrl+shift+7"], "command": "move_to_group", "args": { "group": 6 } },
  { "keys": ["ctrl+shift+8"], "command": "move_to_group", "args": { "group": 7 } },
  { "keys": ["ctrl+shift+9"], "command": "move_to_group", "args": { "group": 8 } },
  


{ "keys": ["ctrl+shift+space"], "command": "expand_selection", "args": {"to": "scope"} },
  

{ "keys": ["ctrl+shift+z"], "command": "redo" },



Entrer un code UTF8
===================

Taper ctrl+Alt+shift+u puis le code unicode 0153 pour le o dans le e.
Puis espace

Snippet
=======

Pour déterminer le scope à positionner lors de la définition d'une snippet ::

   <scope>text.html.markdown</scope>

Pour identifier le scope il y a le raccourci ctrl+shift+alt+p à taper dans le
fichier source, apparait alors en bas dans la bar de status le scope pour ce
fichier.

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
- article à lire http://www.macstories.net/roundups/sublime-text-2-and-markdown-tips-tricks-and-links/



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


Pair programming
----------------

Configurer le plugin floobits

- https://floobits.com/help/plugins/sublime
