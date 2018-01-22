#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kate'
SITENAME = 'Fun Memory Violations'
SITEURL = ''
# DISQUS_SITENAME = 'katesnullpointers'

THEME = 'crumbs'
# NEST_HEADER_IMAGES = 'banner_bg2x.png'

EXTRA_PATH_METADATA = {
		# 'robots.txt': {'path': 'robots.txt'},
		'favicon.ico': {'path': 'favicon.ico'}
}

PLUGIN_PATHS = ['plugins/',]
PLUGINS = ['summary', ]

TEMPLATE_DEBUG = True
DEBUG = True

PATH = 'content'
STATIC_PATHS = ['images', 'downloads', 'kookie.txt']
SITE_LOGO = 'favicon.ico'
SUMMARY_MAX_LENGTH = 140

#############################################
#############################################

# THEME = 'lazystrap' # Why doesn't this work? :(

DEFAULT_CATEGORY = 'Dev Diary'
DEFAULT_DATE = 'fs'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
	('WHOAMI', '/'),
	('Blog', '/blog/'),
	# ('Guides', '/guides/'),
	# ('Showcase', '/showcase/'),
	# ('WHOAMI', '/whoami/'),
)

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'

TAG_URL = '{slug}'
TAG_SAVE_AS = '{slug}/index.html'

#############################################
#############################################

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'
LOCALE = 'C'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

FEED_RSS = 'rss.xml'
CATEGORY_FEED_RSS = '%s/rss.xml'


JINJA_EXTENSIONS = ['webassets.ext.jinja2.AssetsExtension', 'jinja2.ext.with_']
# Blogroll
# LINKS = (('Lonely Robot', 'http://www.lonelyrobot.io'), )

# Social widget
SOCIAL = (('Twitter', 'https://www.twitter.com/spacekookie'),('Github','https://www.github.com/spacekookie'),)

DEFAULT_PAGINATION = 20
