*************
Bootstrap 3.0
*************

Pour débuter
============

Récupérer la version 3 de bootstap.  Tout ce dont vous avez besoin est dans le
répertoire dist.

La première page en pointant sur les ressources jquery ::

        <!DOCTYPE html>
        <html>
          <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>Bootstrap 101 Template</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <!-- Bootstrap -->
            <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">


          </head>
          <body>
            <h1>Hello, world!</h1>

            <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
            <script src="http://codeorigin.jquery.com/jquery.js"></script>
            <!-- Include all compiled plugins (below), or include individual files as needed -->
            <script src="js/bootstrap.min.js"></script>
          </body>
        </html>


Bar de navigation
=================

Pour cela utiliser la classe class="navbar navbar-inverse navbar-fixed-top" ::

    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
          <div class="container">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="#">Apside</a>
      </div>

          <div class="collapse navbar-collapse navbar-ex1-collapse">
            <ul class="nav navbar-nav">
              <li><a href="#">Ajouter CV</a></li>
              <li><a href="#">Chercher CV</a></li>
            </ul>
          </div>
        </div>
        </nav>

La partie navbar-header permet d'avoir un bouton sur le coté droit quand on
passe sur une taille d'écran de type mobile.
Si une partie du contenu se trouve sous la bar de menu alors il convient ajouter
ce style ::

    <style>
      body {
        padding-top: 60px;
      }
    </style>

