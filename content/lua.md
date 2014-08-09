title: Langage Lua
category: Langage
date: 2014-08-09
modified: 2014-08-09
tags: Lua, Langage



Ma prise de note concernant le livre [Programming in Lua](http://www.lua.org/pil/)

# Les types 

##String 

On peut utiliser l'opérateur [[ pour des chaines sur plusieurs lignes.

Test sur du code lua 

    :::lua
    my_var = [[
    Ceci est une string
    sur 
    plusieurs
    lignes
    ]]

### concaténation de strings

l'opérateur à utiliser est ..

    :::lua 
    message = "Hello" .. " World"
    print(message)

## Les tables

Les tables sont des tableaux associatifs, la syntaxe pour déclarer un tel
tableau est

    :::lua
    my_tab = {}

Indexer une valeur 

    :::lua
    my_var["msg_hello"] = "Hello world!"

Il est également possible d'accéder à la valeur de msg_hello par la notion
avec un point.

    :::lua
    print(my_var.msg_hello)

## Les booléens 

Il existe les valeurs classique *true* et *false*. Les tests conditionnel
considère la valeur *false* et *nil* à faux. Attention Lua considère donc la
valeur zéro (0) et la chaîne vide ("") comme des valeurs à vrai dans les
tests.

    :::lua
    my_var = ""
    if my_var then
        print("Ok empty string is true value.")
    end

Retourne

    :::lua
    Ok empty string is true value.

idem pour

    :::lua
    my_var = 0
    if my_var then
        print("Ok zero is true value.")
    end

Retourne

    :::lua
    Ok it's true


##Ressources

- http://www.amazon.fr/gp/offer-listing/859037985X/ref=tmm_other_meta_binding_new_olp_sr?ie=UTF8&condition=new&sr=8-2&qid=1406814811
- http://www.amazon.fr/guide-Lua-ses-applications-dapprentissage-ebook/dp/B009WQR6F0/ref=tmm_kin_swatch_0?_encoding=UTF8&sr=8-1&qid=1406814811


