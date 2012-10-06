#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Bharath M R"
SITENAME = u"Bharath M R"
SITEURL = ''

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          #('Python.org', 'http://python.org'),
          #('Jinja2', 'http://jinja.pocoo.org'),
          #('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images']
ARTICLE_URL = 'posts/{category}/{date:%Y}-{date:%b}-{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{category}/{date:%Y}-{date:%b}-{date:%d}/{slug}/index.html'
