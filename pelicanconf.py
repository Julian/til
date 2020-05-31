AUTHOR = "Julian Berman"

SITEURL = ""
SITENAME = "TIL"
SITESUBTITLE = "Today I Learned"

TIMEZONE = "America/New_York"
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%B %d, %Y"

PATH = "entries"

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["filetime_from_git"]

GITHUB_URL = "https://github.com/Julian"
TWITTER_USERNAME = "JulianWasTaken"
SOCIAL = [
    ("github", GITHUB_URL),
    ("twitter", "https://twitter.com/" + TWITTER_USERNAME),
    ("instagram", "https://instagram.com/julianberman"),
]

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

DRAFT_URL = "drafts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
DRAFT_SAVE_AS = "drafts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

AUTHOR_URL = "authors/{slug}/"
AUTHOR_SAVE_AS = "authors/{slug}/index.html"
AUTHORS_SAVE_AS = "authors/index.html"

CATEGORY_URL = "categories/{slug}/"
CATEGORY_SAVE_AS = "categories/{slug}/index.html"
CATEGORIES_SAVE_AS = "categories/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

TAG_URL = "tags/{slug}/"
TAG_SAVE_AS = "tags/{slug}/index.html"
TAGS_SAVE_AS = "tags/index.html"

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TYPOGRIFY = True
