#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings
AUTHOR = u'Herbert Yang'
SITENAME = u'the Good the Bad and the Curious'
SITEURL = 'http://www.guizishanren.com'
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = 100

# Blogroll
#LINKS = (('About Me', 'pages/about-me.html'))

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

GITHUB_URL = 'http://github.com/zire/'
TWITTER_USERNAME = 'herbertyang'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('Github', 'https://github.com/zire'),
          ('Twitter', 'https://twitter.com/herbertyang'),
		  ('Linkedin', 'http://www.linkedin.com/in/herbertyang'),
		  ('Instagram', 'http://instagram.com/zire'),
          ('Weibo', 'http://weibo.com/zire'),)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Formatting date
DEFAULT_DATE_FORMAT = ('%Y %m %d %A')

# Formatting for urls
DEFAULT_PAGINATION = 10

#PAGE_URL = ('pages/{slug}.html')
#PAGE_SAVE_AS = ('pages/{slug}.html')

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

PAGINATED_DIRECT_TEMPLATES = [('index')]
DIRECT_TEMPLATES = [('index')]

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/', '{base_name}/index{number}.html'),
)

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = False

# Specify theme
THEME = "themes/bootstrap-HY"

OUTPUT_PATH = 'output'
PATH = 'content'
STATIC_PATHS = ['images']


