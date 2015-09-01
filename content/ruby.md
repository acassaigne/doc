:Title: Ruby
:Category: Ruby
:Date: 2014-09-28
:Modified: 2014-09-28
:tags: initiation, ruby

# Outils

L'interpréteur intéractif est 'irb'. 

Pour tester du code dans l'interpréteur il convient d'utiliser la commande load 'filename.rb' et de positionner ces quelques lignes dans votre code.

    :::ruby
    if $0 == __FILE__
       check_usage()
        compare_inventory_files(ARGV[0], ARGV[1])
    end


Installer la doc sous Ubuntu

    :::bash
    sudo apt-get install ri1.9

## encodage des fichiers source

ajouter sur la première ligne du fichier ceci 

    :::ruby
    # encoding: UTF-8

# Eléments du langage

L'instruction 'unless' à moins que...

    :::ruby
    unless <condition>
        <instruction 1>
        <instruction 2>
    end

A moins que la condition ne soit fausse sinon les instructions :

    :::ruby
        <instruction 1>
        <instruction 2>
        
# Les tests

Il convient de faire la distinction entre erreur et échec sur un test.
L'erreur renvoit à un problème lors de l'exécution : erreur de syntaxe...
alors que l'échec est levé sur une assertion.

Déclarer un classe de tests

    :::ruby
        require 'test/unit' 
        require_relative 'mine_code_to_test'     

        class ChurnTests < Test::Unit::TestCase 

            def test_month_before_is_28_days
                 assert_equal(Time.local(2005, 1, 1),
                 month_before(Time.local(2005, 1, 29)))
            end
        end


Pour lancer les tests :

    :::bash
        ruby test_class_file-tests.rb 

Pour lancer que certains tests :

    :::bash
        ruby test_class_file-tests.rb --name=/asterisks/


# shell & ruby

Pour exécuter une commande shell il suffit d'encadrer la commande par
ces caractères anti-quote.


# Itérateur

Les itérateurs permette d'envoyer un message (éxécuter une méhode) sur chaque
élément d'un tableau. Cela permet de travailler sur chaque élément d'un
tableau.

    :::ruby
    [1, 2, 3].each do | element | 
        puts(element)
    end

Afin de pouvoir utiliser l'élément au sein du bloc de code, il faut nommer cet
élément du tableau. Cela se fait en donnant un nom de variable entre le
caractère barre verticale (ou pipe) ainsi | var_name |

Le précédent bloc est exécuté trois fois.
En fin d'exécution le tableau d'origine est retourné par la méthode each.

each est le plus simple itérateur. L'itérateur collect construit un nouveau
tableau avec les valeurs calculés par le bloc.

Les itérateurs existent le plus souvent sur des objets composés de plusieurs
parties comme les fichiers.

Par exemple :

    :::ruby
    downcase_file = File.open('myFile.txt').collect() do | line | 
        line.downcase()
    end

## l'itérateur reject 

L'itérateur reject permet de construire une nouvelle collection purgé des éléments souhaités 

    :::ruby
    array.reject() do | line |
        line.include?('a_rejeter')
    end

# Fichier

    :::ruby
    an_array = File.open('filename.txt').readlines

# Tableau / array

## opérations ensembliste sur les tableaux 

### soustraction 

Il est possible de réaliser la soustraction de deux tableaux.

    :::ruby
    array_result = array1 - array2

### intersection 

    :::ruby 
    array_resul = array1 & array2 

## Quelques méthodes sur pour travailler avec les tableaux 

Pour obtenir la taille d'un tableau utilisez la méthode size ou length. 

    :::ruby
    array.size 
    array.length

Obtenir le premier élément d'un tableau 

    :::ruby
    array[0]

Obtenir le dernier élément d'un tableau 

    :::ruby
    array[-1]

Tout élément demandé hors index retourne un nil 

    :::ruby
    little_array[200]
    nil

obtenir un sous tableau (slice)

    :::ruby 
    array[1,3]
    array[1..3]

obtenir un sous tableau en excluant le dernier indice donné 

    :::ruby
    array[1...3]

changer un sous ensemble du tableau (slice)

    :::ruby
    array[1..2] = [ 'a', 'b']

Tester la présence d'un élément dans le tableaul : include?

    :::ruby
    array.include?('a')

effacer un élément à un indice donné 

    ruby:::
    array.delete_at(4)

efface l'élément à l'indice 4 les tableaux étant indicé à partir de zéro.

Effacer tous les éléments ayant une valeur donné :

    ruby:::
    array.delete('b')

efface tous les éléments dans le tableau array ayant pour valeur le caractère 'b'.

Supprimer une partie d'un tableau (un slice) 

    :::ruby
    array.slice!(2..4)

Note : les méthodes avec un point d'exclamation modifient l'objet sur lequel elles sont appelées.

Un tableau est-il vide ?

    :::ruby 
    array.empty?

Ajouter un élément en fin de tableau 

    :::ruby
    array.push('c')
    array << 'c'

Ajouter l'élément 'c' en fin de tableau.

Retire le dernier élément du tableau, le tableau est vu comme une pile 

    :::ruby
    array.pop()

Retire le premier élément du tableau avec la méthode shift, le tableau est vu comme une file

    :::ruby
    array.shift()

Ajouter un élément en tête du tableau 

    :::ruby
    array.unsift('a')

Remplacer un sous ensemble du tableau (slice) par un unique élément 

    :::ruby 
    array[1..2] = 'un element'


### identifier les méthodes d'un objet 

    :::ruby
    array.methods()

# Variables, Constantes

La convention veut que les varaibles aient un identifiant composé de minuscule et de _
Par exemple ma_variable est un nom valide, vous ne pouvez pas
utiliser le caractère trait d'union. 

Les constantes commencent par une Majuscule et n'ont pas de caractères _
Par exemple MaConstant est un nom de constante.

# Type 

## Integer 

Opération sur les entiers :

    :::ruby
        18/5
        3
        18/5.0
        3.6

Lorsqu'un nombre à virgule entre en jeu alors le résultat est un flottant.


# Scripting

Pour obtenir les arguments de votre script, il convient d'utiliser le tableau
ARGV. Ce tableau commence à zéro pour obtenir le premier argument.


