__all__ = [
    "get_likes_count",
    "get_likes",
    "get_latest_liker_id",
    "add_like",
    "remove_like",
]

from .aliases import *
from .paths import (
    LIKES_LIST_URL,
    LIKE_ADD_URL,
    LIKE_REMOVE_URL,
)
from .model import (
    get_model_properties,
)

def get_likes_count(session: Session, model_name: str, id_: int, properties: str = "_nLikeCount") -> int:
    """Return likes count"""

    res = get_model_properties(session, model_name, id_, properties)

    return res.json()[properties]

def get_likes(session: Session, model_name: str, id_: int, page: int = 1) -> Response:
    """Return likes list"""

    url = LIKES_LIST_URL.format(model_name, id_, page)

    return session.get(url)

def get_latest_liker_id(response: Response) -> dict:
    """Return latest liker's ID"""

    body = response.json()

    return body["_aRecords"][0]["_aSubmitter"]["_idRow"]

def add_like(session: Session, model_name: str, id_: int) -> Response:
    """Add Like"""

    url = LIKE_ADD_URL.format(model_name, id_)

    return session.post(url, json = {})

def remove_like(session: Session, model_name: str, id_: int) -> Response:
    """Remove Like"""

    url = LIKE_REMOVE_URL.format(model_name, id_)

    return session.delete(url)
