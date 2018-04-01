#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings
AUTHOR = u'Herbert Yang'
SITENAME = u'the Good the Bad and the Curious'
SITEURL = 'https://guizishanren.com'
DISQUS_SITENAME = 'goodbadcurious'
GOOGLE_ANALYTICS = 'UA-714838-2'
AUTHOR_EMAIL = 'webmaster@inturious.com'
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = 50
ADDTHIS_PROFILE = 'ra-538a1ad51a39747d'

# Settings from pure-single theme

COVER_IMG_URL = SITEURL + '/static/img/bg001_shinjuku.jpg'

PROFILE_IMG_URL = SITEURL + '/static/img/profile001_yang.jpeg'

FAVICON_URL = SITEURL + '/static/img/favicon.ico'

MENUITEMS = (
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
  )

# Blogroll
#LINKS = (('About Me', 'pages/about-me.html'))

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

GITHUB_URL = 'https://github.com/zire'
TWITTER_USERNAME = 'herbertyang'

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'https://feeds.feedburner.com'
FEED_RSS = 'feeds/rss'
FEED_ALL_RSS = 'feeds/all.rss.xml'
# FEED_ATOM = 'GoodBadCurious/main.xml'
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_URL = 'https://feeds.feedburner.com/GoodBadCurious'
TAG_FEED_RSS = None
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/category/.%s.rss'
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (
          ('twitter', 'https://twitter.com/herbertyang'),
          ('linkedin', 'https://www.linkedin.com/in/herbertyang'),
          ('instagram', 'https://instagram.com/zire'),
          ('github', 'https://github.com/zire'),
 #         ('weibo', 'https://weibo.com/zire'),
 #         ('flickr','https://www.flickr.com/photos/gankyun/'),
 #         ('tumblr','https://zynphendale.tumblr.com'),
 #         ('pinterest','https://www.pinterest.com/zire'),
 #         ('quora', 'https://www.quora.com/Herbert-Yang'),
          ('rss','https://www.guizishanren.com/feeds/rss'))

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Formatting date
DEFAULT_DATE_FORMAT = ('%Y %m %d %A')
WITH_FUTURE_DATES = True

# Formatting for urls
DEFAULT_PAGINATION = 10

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

# ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_URL = "{slug}"
# ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"
ARTICLE_SAVE_AS = "{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

PAGINATED_DIRECT_TEMPLATES = [('index'),('tags'), ('categories'),('archives')]
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')

#PAGINATION_PATTERNS = (
#    (1, '{base_name}/', '{base_name}/index.html'),
#    (2, '{base_name}/', '{base_name}/index{number}.html'),
#)

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = False

# Specify theme & plug-ins
THEME = "themes/pure-single"
PLUGINS = ['sitemap','neighbors','gravatar']

# Specify important paths
OUTPUT_PATH = 'output'
PATH = 'content'
STATIC_PATHS = ['images']
PLUGIN_PATHS = ['plugins']
CACHE_PATH = 'cache'

# Define sitemap parameters
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

MARKUP=('rst', 'md', 'markdown', 'html')

LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'
