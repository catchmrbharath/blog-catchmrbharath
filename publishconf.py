#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://blog.catchmrbharath.in'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
#RELATIVE_URLS = False

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
ARTICLE_URL = 'posts/{category}/{date}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date}-{slug}.html'
