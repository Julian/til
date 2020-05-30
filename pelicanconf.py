AUTHOR = "Julian Berman"

SITENAME = "TIL"
SITESUBTITLE = "Today I Learned"
SITEURL = "https://til.grayvines.com"

TIMEZONE = "America/New_York"
DEFAULT_DATE = "fs"

GITHUB_URL = "https://github.com/Julian"
TWITTER_USERNAME = "JulianWasTaken"
SOCIAL = [
    ("@JulianWasTaken", "https://twitter.com/" + TWITTER_USERNAME),
    ("@julianberman", "https://instagram.com/julianberman"),
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

TYPOGRIFY = True
