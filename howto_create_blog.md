# Création blog

Se créer un environnement :

mkdir ~/devel/blog
mkvirtualenv -a ~/devel/blog my_blog
pip install pelican Markdown

pelican-quickstart


git clone file:///home/acassaigne/Dropbox/blog.git
ln -s my_config/publishconf.py
ln -s my_config/pelicanconf.py
ln -s my_config/fabfile.py 
