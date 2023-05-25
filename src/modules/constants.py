from datetime import datetime

# from os.path import dirname, join, normpath

USER_NAME = "nnmnnms"
GAME_ID = 6767

BASE_URL = "https://gamebanana.com"

BASE_URL_API = f"{BASE_URL}/apiv11"

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# ASSETS_DIR = join(normpath(dirname(__file__)), "..", "assets")
# EVENT_IMAGE_PATH = join(ASSETS_DIR, "images", "event.png")

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
    "token": "input[type=hidden]", # all submissions
    "title": "#Name input", # thread, question, event
    "game": "#Category .GameCategory input[type=hidden]", # thread, question, event
    "category": "#Category .Category input[type=hidden]", # thread, question, event
    "text": "#Article .Source textarea", # thread, question, event
    "subtitle": "#Description input", # thread, question
    "access": "#Status input", # thread, question, event
    "toc": "#TableOfContentsToggle input", # thread, event
    "analytics": "#AnalyticsToggle input", # thread, question, event
    "comments": "#CommentsMode input", # thread, question
    "start_date_month": "#StartDate select", # values: 1-12; event
    "start_date_day": "#StartDate select:nth-child(2)", # values: 1-31; event
    "start_date_year": "#StartDate select:nth-child(3)", # values: 1990-<current+10>; event
    "start_date_hour": "#StartDate select:nth-child(5)", # values: 0-23; event
    "start_date_minute": "#StartDate select:nth-child(7)", # values: 0-55, step: 5; event
    "end_date_month": "#EndDate select", # values: 1-12; event
    "end_date_day": "#EndDate select:nth-child(2)", # values: 1-31; event
    "end_date_year": "#EndDate select:nth-child(3)", # values: 1990-<current+10>; event
    "end_date_hour": "#EndDate select:nth-child(5)", # values: 0-23; event
    "end_date_minute": "#EndDate select:nth-child(7)", # values: 0-55, step: 5; event
    "timezone": "#Timezone select", # format: <continent>/<country> and 'UTC'; event
    "repeat": "#Repeat select", # values: never, daily, weekly, monthly, yearly; event
    "location": "#Location input", # event
    "image": "#Image input[type=hidden]", # event
    "form_name": "input[name=FormName]" # all submissions
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

QUESTION_FORM_ENTRIES = {
    "title": "Test Question",
    "game": f"{GAME_ID}",
    "category": "1553", # Other/Misc
    "text": f"{LOREM_IPSUM} {str(datetime.utcnow())}",
    "subtitle": "What is the answer to the ultimate question?",
    "access": ACCESS_MAP["Private"],
    "comments": COMMENTS_MODE_MAP["Open"]
}

EVENT_FORM_ENTRIES = {
    "title": "Test Event",
    "game": f"{GAME_ID}",
    "category": "118", # Other/Misc
    "text": f"{LOREM_IPSUM} {str(datetime.utcnow())}",
    "start_date_month": "4",
    "start_date_day": "1",
    "start_date_year": "2023",
    "start_date_hour": "13",
    "start_date_minute": "30",
    "end_date_month": "5",
    "end_date_day": "1",
    "end_date_year": "2023",
    "end_date_hour": "13",
    "end_date_minute": "30",
    "timezone": "UTC",
    "repeat": "never",
    "location": "GameBanana\'s Battle Museum",
    # "image": ("event.png", EVENT_IMAGE_PATH, "image/png"),
    "access": ACCESS_MAP["Private"],
    "toc": TOC_MAP["Disabled"]
}

ADD_THREAD_URL = f"{BASE_URL}/threads/add?gameid={GAME_ID}"
ADD_QUESTION_URL = f"{BASE_URL}/questions/add?gameid={GAME_ID}"
ADD_EVENT_URL = f"{BASE_URL}/events/add?gameid={GAME_ID}"
