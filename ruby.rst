****
Ruby
****

resource
========

- http://www.lee-dohm.com/2013/05/05/thoughts-on-why-ruby-is-awesome.html

Objets
======

tester le type d'objet ::

  assert_equal true, "Ma String".is_a?(String)

Chaque objet a un object_id ::

    MonObjet.object_id

Instancier un objet ::

   Object.new()

Cloner un objet ::

    obj = Object.new
    copy = obj.clone

mais il n'y a pas égalité ::

    assert_equal true, obj           != copy
    assert_equal true, obj.object_id != copy.object_id

égalité
-------

c'est ==

Assert
------

L'assert en ruby ::

  assert expected_value == actual_value

a better way ::

  assert_equal expected_value, actual_value


assert et match ::

  assert_match(/undefined method `some_method_nil_doesnt_know_about' for nil:NilClass/, ex.message)

Tester si un objet est nil ?

c'est via cette syntaxe ::

   MonObjet.nil?


Simple caractère
================

La déclaration d'un caractère est la suivante ::

  ?a

String
======

Le split de stings ::

    string = "Sausage Egg Cheese"
    words = string.split
    assert_equal ["Sausage", "Egg", "Cheese"], words

Définir des string avec des caractères ' ou " ::

    a = %(flexible quotes can handle both ' and " characters)
    b = %!flexible quotes can handle both ' and " characters!
    c = %{flexible quotes can handle both ' and " characters}
    assert_equal true, a == b
    assert_equal true, a == c

    long_string = <<EOS
    It was the best of times,
    It was the worst of times.
    EOS
    assert_equal 53, long_string.length
    assert_equal 2, long_string.lines.count
    assert_equal "I", long_string[0,1]

méthode sur les string length et count lignes ::

    assert_equal 54, long_string.length
    assert_equal 3, long_string.lines.count

Accéder au premier caractère de la première ligne ::

    assert_equal "\n", long_string[0,1]

Array
=====

Déclarer un array vide ::

  empty_array = Array.new

L'index commence à zéro ::

    array[0] = 1
    assert_equal [1], array

    array[1] = 2
    assert_equal [1, 2], array

Ajouter un élément en bout de tableau ::

    array << 333
    assert_equal [1, 2, 333], array

Tableau et index
----------------

  array.first
  array.last

Tranche de tableau
------------------

  array[0,1] prendre un élément depuis l'élément zéro
  array[0,2] prendre deux éléments depuis l'élément zéro

tant que l'on part d'un élément existant on obtient un tableau vide par exemple ::

  array = [:peanut, :butter, :and, :jelly]
  assert_equal [], array[4,100]

mais si on part d'un élément inexistant nil on obtien nil ::

  array = [:peanut, :butter, :and, :jelly]
  assert_equal nil, array[5,0]

Range n'est pas un tableau
--------------------------

exemple d'utilisation du Range ::

    assert_equal Range, (1..5).class
    assert_not_equal [1,2,3,4,5], (1..5)
    assert_equal [1,2,3,4,5], (1..5).to_a
    assert_equal [1,2,3,4], (1...5).to_a

mais permet des manipulation d'index de tableau ::

    array[1..3]
    array[1...3]

push, pop, shift, unshift et tableau
------------------------------------

Exemple ::

    array = [1,2]
    array.push(:last)

    assert_equal [1,2,:last], array
    popped_value = array.pop
    assert_equal :last, popped_value


Tableau associatif
==================

Definir un tableau ::

  My_Hash = {}

ou ::

  my_hash = Hash.new

Avoir la taille ::

   my_hash.size

Valeur par défaut et tableau associatif
---------------------------------------

exemple de valeur par défaut qui est un tableau ::

    hash = Hash.new([])

ici nous ajoutons à l'unique valeur par défaut (le tableau vide) deux éléments :

Ajout de deux valeurs ::

    hash[:one] << "uno"
    hash[:two] << "dos"

Si l'on veut une valeur par défaut pour chaque clé inexistante alors il faut utiliser la
déclaration suivante ::

    hash = Hash.new {|hash, key| hash[key] = [] }
    hash[:one] << "uno"
    hash[:two] << "dos"


Assignement multiples
=====================

Comme à la python ::

    first_name, last_name = ["John", "Smith", "III"]
    assert_equal "John", first_name
    assert_equal "Smith", last_name

Opérateur * ::

    first_name, *last_name = ["John", "Smith", "III"]
    assert_equal "John", first_name
    assert_equal  ["Smith", "III"], last_name

Autres resources
================

Tutorial
https://www.ruby-lang.org/fr/documentation/quickstart/3/
http://ruby.about.com/od/beginningruby/ss/The-Zen-Of-Learning-Ruby.htm

librairie
=========

A regarder pour analyser les options de la ligne de commande ::

   http://trollop.rubyforge.org/

