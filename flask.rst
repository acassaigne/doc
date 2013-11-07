*****
Flask
*****

Introduction
============

Flask est un micro-framework, qu'est-ce donc qu'un micro-framework ? A
l'oppossé de la phylosophie Django qui inclue la quasi totalité de ce qu'un
développeur peut avoir besoin pour développer une application web. Django
propose des API pour la gestion des formulaire, une API (ORM) de gestion de la
base de données, une API pour la gestion des sessions etc... Flask ne propose
que quelques éléments de bases permettant de développer une application, c'est
à dire une API rudimentaire ne proposant que le minimum. Libre au développeur
ensuite d'installer des plugging en fonction de ses besoins. Il a ainsi que ce
dont-il a réllement besoin.



Tutoriel
--------

Pour un tutoriel suivre ce lien quick_start_

.. _quick_start: http://flask.pocoo.org/docs/quickstart/


Formulaire avec WTForms
=======================

Commençons pas installer le plugging ``WTForms``, je n'ai pas utilisé le pluging
flask-WTF. Je n'ai utilisé que WTForms de base.

Création d'une page statique html
.. code-block:: html

    <form method="post" action="/post_wtf">
    <table>
        <tr>
            <td>
                Nom :
            </td>
            <td>
                <input type="text" name="last_name">
            </td>
        </tr>
        <tr>
            <td>
                Prénom :
            </td>
            <td>
                <input type="text" name="first_name" >
            </td>
        </tr>
        <tr>
            <td>
                <input type="submit" value="Valider">
            </td>
            <td>
                &nbsp;
            </td>
        </tr>
    </table>
    </form>

Déposer le fichier dans le répertoire template.

première méthode envoyant le fichier statique (#FIXME)
.. code-block:: python

    @app.route('/wtf')
    def wtf():
       return render_template('wtf.html')

Installer WTForms
-----------------

Pour cela utiliser la commmande ``pip install WTForms``.


Lien à consulter
================

Très bon lien, complet sur le développement d'une application :

- https://github.com/mitsuhiko/flask/wiki/Large-app-how-to

Un serie d'articles de type tutoriel `turoriels <http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms>`_