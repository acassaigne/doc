****
Ruby
****

Objets
======

tester le type d'objet ::

  assert_equal true, "Ma String".is_a?(String)

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