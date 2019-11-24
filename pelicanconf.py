#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Katharina Fey'
SITENAME = 'fun memory violations'
SITEURL = ''

THEME = 'crumbs'

EXTRA_PATH_METADATA = {
		# 'robots.txt': {'path': 'robots.txt'},
		'favicon.ico': {'path': 'favicon.ico'}
}

PLUGIN_PATHS = ['plugins/',]
PLUGINS = ['summary', 'read_time']

TEMPLATE_DEBUG = True
DEBUG = True
READ_TIME = 180

PATH = 'content'
STATIC_PATHS = ['images', 'downloads', '.well-known',
                'keys.txt', '555F2E4B6F87F91A4110.txt' ]
SITE_LOGO = 'favicon.ico'

SUMMARY_MAX_LENGTH = 120
# SUMMARY_END_MARKER = "( ... )"

#############################################
#############################################

# THEME = 'lazystrap' # Why doesn't this work? :(

DEFAULT_CATEGORY = 'Blog'
DEFAULT_DATE = 'fs'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
  ('WHOAMI', '/'),
  ('Blog', '/blog/'),
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
RSS_FEED_SUMMARY_ONLY = False

JINJA_ENVIRONMENT = {
  'extensions': ['webassets.ext.jinja2.AssetsExtension', 'jinja2.ext.with_']
}


# Blogroll
# LINKS = (('Lonely Robot', 'http://www.lonelyrobot.io'), )

# Social widget
SOCIAL = (('Twitter', 'https://www.twitter.com/spacekookie'),('Github','https://www.github.com/spacekookie'),)

DEFAULT_PAGINATION = 20


from pygments.lexer import RegexLexer
from pygments.token import *

class LoveLexer(RegexLexer):
    name = 'Love'
    aliases = ['love']
    filenames = ['*.love']

    tokens = {
        'root': [
            ("❤", Keyword.Namespace),
        ]
    }
