from datetime import datetime

USER_NAME = "nnmnnms"
GAME_ID = 6767

BASE_URL = "https://gamebanana.com"

BASE_URL_API = f"{BASE_URL}/apiv11"

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

ACCESS_MAP = {
    "Public": "0", # Everyone can access
    "Private": "2" # Only you, permit holders, studio leaders and moderators can access
}

TOC_MAP = {
    "Enabled": "true", # A Table Of Contents is automatically generated
    "Disabled": "false"
}

COMMENTS_MODE_MAP = {
    "Open": "open",       # Anyone can comment (except members you block or block you)
    "Buddies": "buddies", # Only you and your buddies can comment
    "Authors": "creator", # Only you, credited members and this Submission's studio members can comment (if studio release)
    "Locked": "locked",   # Commenting not allowed, but existing comments appear
    "Hidden": "hidden"    # Commenting not allowed and any existing comments are hidden
}

CSS_SELECTORS = {
    "token": "input[type=hidden]",
    "title": "#Name input",
    "game": "#Category .GameCategory input[type=hidden]",
    "category": "#Category .Category input[type=hidden]",
    "text": "#Article .Source textarea",
    "subtitle": "#Description input",
    "access": "#Status input",
    "toc": "#TableOfContentsToggle input",
    "analytics": "#AnalyticsToggle input",
    "comments": "#CommentsMode input",
    "form_name": "input[name=FormName]"
}

THREAD_FORM_ENTRIES = {
    "title": "Test Thread",
    "game": f"{GAME_ID}",
    "category": "5148", # Other/Misc
    "text": f"{LOREM_IPSUM} {str(datetime.utcnow())}",
    "subtitle": "I\'m afraid I can\'t do that, Dave",
    "access": ACCESS_MAP["Private"],
    "toc": TOC_MAP["Disabled"],
    "comments": COMMENTS_MODE_MAP["Open"]
}

ADD_THREAD_URL = f"{BASE_URL}/threads/add?gameid={GAME_ID}"
