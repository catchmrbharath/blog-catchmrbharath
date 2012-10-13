#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Bharath M R"
SITENAME = u"Bharath M R"
SITEURL = 'www.catchmrbharath.in'

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

FILES_TO_COPY = (('CNAME', 'CNAME'), )
DEFAULT_PAGINATION = 10
THEME = 'theme'
STATIC_PATHS = ['images', ]
ARTICLE_URL = 'posts/{category}/{date:%Y}-{date:%b}-{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{category}/{date:%Y}-{date:%b}-{date:%d}/{slug}/index.html'
MD_EXTENSIONS = ['codehilite', 'mathjax']
TWITTER_USERNAME = 'catchmrbharath'
GITHUB_URL = 'https://github.com/catchmrbharath'
DISQUS_SITENAME = 'bharathsblog'
GOOGLE_ANALYTICS = 'UA-35535020-1'
