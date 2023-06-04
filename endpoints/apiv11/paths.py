__all__ = [
    "BASE_URL",

    # Authenticate
    "AUTHENTICATE_URL",

    # Dictionaries
    "STAMPS_LIST_URL",
    "UNTRASH_REASONS_URL",

    # Like
    "LIKES_LIST_URL",
    "LIKE_ADD_URL",
    "LIKE_REMOVE_URL",

    # Model
    "MODEL_PROPERTIES_URL",

    # Post
    "POSTS_LIST_URL",
    "POST_ADD_URL",
    "POST_CHANGE_URL",
    "POST_TRASH_URL",
    "POST_UNTRASH_URL",

    # Stamps
    "STAMPS_ON_POST_BY_ALL_URL",
    "STAMPS_ON_POST_BY_ACCESSOR_URL",
    "STAMPS_CHANGE_URL",

    # Subscribe
    "SUBSCRIBE_ADD_URL",
    "SUBSCRIBE_REMOVE_URL",

    # Thank
    "THANKERS_LIST_URL",
    "THANK_ADD_URL",

    # Todos
    "TODOS_LIST_URL",
    "TODOS_ADD_URL",
    "TODOS_CHANGE_URL",
    "TODOS_REMOVE_URL",
]

BASE_URL = "https://gamebanana.com/apiv11"

AUTHENTICATE_URL = BASE_URL + "/Member/Authenticate"

STAMPS_LIST_URL = BASE_URL + "/Util/Config/Stamps"
UNTRASH_REASONS_URL = BASE_URL + "/Util/Config/UntrashReasons"

LIKES_LIST_URL = BASE_URL + r"/{0}/{1}/Likes?_nPage={2}"
LIKE_ADD_URL = BASE_URL + r"/{0}/{1}/Like"
LIKE_REMOVE_URL = LIKE_ADD_URL

MODEL_PROPERTIES_URL = BASE_URL + r"/{0}/{1}?_csvProperties={2}"

POSTS_LIST_URL = BASE_URL + r"/{0}/{1}/Posts?_nPage={2}&_nPerpage={3}&_sSort={4}"
POST_ADD_URL = BASE_URL + r"/{0}/{1}/Post/Add"
POST_CHANGE_URL = BASE_URL + r"/Post/{0}"
POST_TRASH_URL = POST_CHANGE_URL
POST_UNTRASH_URL = POST_CHANGE_URL + "/Untrash"

STAMPS_ON_POST_BY_ALL_URL = BASE_URL + r"/Post/{0}/Stamps"
STAMPS_ON_POST_BY_ACCESSOR_URL = BASE_URL + r"/Post/{0}/AccessorStamps"
STAMPS_CHANGE_URL = BASE_URL + r"/Post/{0}/Stamp"

SUBSCRIBE_ADD_URL = BASE_URL + r"/{0}/{1}/Subscription/Add"
SUBSCRIBE_REMOVE_URL = BASE_URL + r"/Subscription/{0}"

THANKERS_LIST_URL = BASE_URL + r"/{0}/{1}/Thanks?_nPage={2}"
THANK_ADD_URL = BASE_URL + r"/{0}/{1}/Thank/Add"

TODOS_LIST_URL = BASE_URL + r"/{0}/{1}/Todos?_nPage={2}"
TODOS_ADD_URL = BASE_URL + r"/{0}/{1}/Todo/Add"
TODOS_CHANGE_URL = BASE_URL + r"/Todo/{0}"
TODOS_REMOVE_URL = TODOS_CHANGE_URL
