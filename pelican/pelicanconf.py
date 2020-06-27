from pathlib import Path

HERE = Path(__file__).parent.resolve()
PATH = HERE.parent / "entries"

AUTHOR = "Julian Berman"

SITEURL = ""
SITENAME = "TIL"
SITESUBTITLE = "Today I Learned"

TIMEZONE = "America/New_York"
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%B %d, %Y"

THEME = HERE / "theme"

PLUGIN_PATHS = [HERE / "plugins", "plugins"]
PLUGINS = ["filetime_from_git", "til_to_anki"]

GITHUB_URL = "https://github.com/Julian"
TWITTER_USERNAME = "JulianWasTaken"
SOCIAL = [
    ("github", GITHUB_URL),
    ("twitter", "https://twitter.com/" + TWITTER_USERNAME),
    ("instagram", "https://instagram.com/julianberman"),
]

ARTICLE_URL = "entries/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "entries/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

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

DOCUTILS_SETTINGS = dict(
    initial_header_level=4,  # Use h4 since we use h3 for entry titles
)
