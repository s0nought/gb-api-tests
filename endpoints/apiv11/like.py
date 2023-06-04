__all__ = [
    "get_likes",
    "get_likes_count_and_latest_liker_id",
    "add_like",
    "remove_like",
]

from .aliases import *
from .paths import (
    LIKES_LIST_URL,
    LIKE_ADD_URL,
    LIKE_REMOVE_URL,
)

def get_likes(session: Session, model_name: str, id_: int, page: int = 1) -> Response:
    """Return likes list"""

    url = LIKES_LIST_URL.format(model_name, id_, page)

    return session.get(url)

def get_likes_count_and_latest_liker_id(response: Response) -> tuple[int, int]: # refactor ?
    """Return likes count and latest liker's ID"""

    body = response.json()

    count = body["_aMetadata"]["_nRecordCount"]
    record = body["_aRecords"][0]
    latest_id = record["_aSubmitter"]["_idRow"]

    return count, latest_id

def add_like(session: Session, model_name: str, id_: int) -> Response:
    """Add Like"""

    url = LIKE_ADD_URL.format(model_name, id_)

    return session.post(url, json = {})

def remove_like(session: Session, model_name: str, id_: int) -> Response:
    """Remove Like"""

    url = LIKE_REMOVE_URL.format(model_name, id_)

    return session.delete(url)
