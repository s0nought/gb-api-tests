__all__ = [
    "get_posts_count",
    "get_posts",
    "get_latest_post_id_and_text",
    "add_post",
    "change_post",
    "trash_post",
    "untrash_post",
]

from .aliases import *
from .paths import (
    POSTS_LIST_URL,
    POST_ADD_URL,
    POST_CHANGE_URL,
    POST_TRASH_URL,
    POST_UNTRASH_URL,
)
from .model import (
    get_model_properties,
)

def get_posts_count(session: Session, model_name: str, id_: int, properties: str = "_nPostCount") -> int:
    """Return posts count"""

    res = get_model_properties(session, model_name, id_, properties)

    return res.json()[properties]

def get_posts(session: Session, model_name: str, id_: int, page: int = 1, per_page: int = 15, sort_order: str = "newest") -> Response:
    """Return posts list"""

    url = POSTS_LIST_URL.format(model_name, id_, page, per_page, sort_order)

    return session.get(url)

def get_latest_post_id_and_text(response: Response) -> tuple[int, str]:
    """Return latest post's ID and source text"""

    body = response.json()

    post_id = 0
    source_text = ""

    record = body["_aRecords"][0]

    if record:
        post_id = record["_idRow"]
        source_text = record["_sText"]

    return post_id, source_text

def add_post(session: Session, model_name: str, id_: int, source_text: str) -> Response:
    """Add Post"""

    url = POST_ADD_URL.format(model_name, id_)

    data = {
        "_sText": source_text,
    }

    return session.post(url, json = data)

def change_post(session: Session, post_id: int, source_text: str) -> Response:
    """Change Post"""

    url = POST_CHANGE_URL.format(post_id)

    data = {
        "_sText": source_text,
    }

    return session.patch(url, json = data)

def trash_post(session: Session, post_id: int) -> Response:
    """Trash Post"""

    url = POST_TRASH_URL.format(post_id)

    return session.delete(url)

def untrash_post(session: Session, post_id: int, reason_id: int = 4) -> Response:
    """Untrash Post"""

    url = POST_UNTRASH_URL.format(post_id)

    data = {
        "_idReasonRow": reason_id,
    }

    return session.patch(url, json = data)
