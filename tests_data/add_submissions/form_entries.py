__all__ = [
    "THREAD_DATA",
    "QUESTION_DATA",
    "EVENT_DATA",
    "WARE_DATA",
    "PROJECT_DATA",
    "REQUEST_DATA",
    "SCRIPT_DATA",
]

from datetime import datetime

from common.constants import GAME_ID, LOREM_IPSUM
from common.dictionaries import ACCESS, TOC, COMMENTS_MODE, IS_CREATOR, LANGUAGE

def get_lorem_ipsum():
    return f"{LOREM_IPSUM} {str(datetime.utcnow())}"

THREAD_DATA = {
    "title": "Test Thread",
    "game": f"{GAME_ID}",
    "category": "5148", # Other/Misc
    "text": get_lorem_ipsum(),
    "subtitle": "I\'m afraid I can\'t do that, Dave",
    "access": ACCESS["Private"],
    "toc": TOC["Disabled"],
    "comments": COMMENTS_MODE["Open"],
}

QUESTION_DATA = {
    "title": "Test Question",
    "game": f"{GAME_ID}",
    "category": "1553", # Other/Misc
    "text": get_lorem_ipsum(),
    "subtitle": "What is the answer to the ultimate question?",
    "access": ACCESS["Private"],
    "comments": COMMENTS_MODE["Open"],
}

EVENT_DATA = {
    "title": "Test Event",
    "game": f"{GAME_ID}",
    "category": "118", # Other/Misc
    "text": get_lorem_ipsum(),
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
    "access": ACCESS["Private"],
    "toc": TOC["Disabled"],
}

WARE_DATA = {
    "type": "19", # Other
    "title": "Test Ware",
    "game": f"{GAME_ID}",
    "category": "240", # Other/Misc
    "text": get_lorem_ipsum(),
    "pending_message": "Definitely not click-bait",
    "delivered_message": "Thanks for trusting in us",
    "subtitle": "Buy my stuff",
    "screenshots": "[]", # optional
    "access": ACCESS["Private"],
    "toc": TOC["Disabled"],
}

PROJECT_DATA = {
    "title": "Test Project",
    "game": f"{GAME_ID}",
    "category": "564", # Other/Misc
    "text": get_lorem_ipsum(),
    "subtitle": "PROject MT",
    "access": ACCESS["Private"],
    "toc": TOC["Disabled"],
}

REQUEST_DATA = {
    "title": "Test Request",
    "game": f"{GAME_ID}",
    "category": "2696", # Other/Misc
    "text": get_lorem_ipsum(),
    "request_requirements": "Be my guest",
    "subtitle": "",
    "access": ACCESS["Private"],
    "toc": TOC["Disabled"],
}

SCRIPT_DATA = {
    "title": "Test Script",
    "game": f"{GAME_ID}",
    "category": "2697", # Other/Misc
    "text": get_lorem_ipsum(),
    "code": "Lorem ipsum",
    "subtitle": "",
    "comment_instructions": "",
    "who_is_the_creator": IS_CREATOR["Yes"],
    "submission_authors": [
        ("Key Authors", "2642489", "nnmnnms", "", "Coder"),
        ("Original Authors", "", "", "", ""),
        ("Contributors", "", "", "", ""),
        ("Special Thanks", "", "", "", ""),
    ],
    "studio": "0", # Non-Studio
    "license": "",
    "license_checklist": "yes", # some defaults
    "language": LANGUAGE["Plain Text"],
    "requirements": ("", ""),
    "contest": "0", # Non-Contest
    "jam": "0", # Non-jam
    "project": "0", # No associated Project
    "access": ACCESS["Private"],
    "toc": TOC["Disabled"],
}
