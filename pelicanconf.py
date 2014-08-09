#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anthony Cassaigne'
SITENAME = u'Wiki Anthony'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('acassaigne', 'http://acassaigne.eu/'),
         )

# Social widget
SOCIAL = (('twitter acassaigne', 'https://twitter.com/acassaigne'),
          ('github acassaigne', 'https://github.com/acassaigne'),)



DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/acassaigne/devel/wiki/pelican-octopress-theme"
