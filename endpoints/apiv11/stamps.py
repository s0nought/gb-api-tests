__all__ = [
    "get_post_stamps_by_all",
    "get_post_stamps_by_accessor",
    "change_post_stamps",
]

from .aliases import *
from .paths import (
    STAMPS_ON_POST_BY_ALL_URL,
    STAMPS_ON_POST_BY_ACCESSOR_URL,
    STAMPS_CHANGE_URL,
)

def get_post_stamps_by_all(session: Session, post_id: int) -> Response:
    """Return post stamps by all users"""

    url = STAMPS_ON_POST_BY_ALL_URL.format(post_id)

    return session.get(url)

def get_post_stamps_by_accessor(session: Session, post_id: int) -> Response:
    """Return post stamps by the accessor"""

    url = STAMPS_ON_POST_BY_ACCESSOR_URL.format(post_id)

    return session.get(url) # json() -> list[str]

def change_post_stamps(session: Session, post_id: int, stamp_ids: list[int] = [2]) -> Response:
    """Change post stamps"""

    url = STAMPS_CHANGE_URL.format(post_id)

    data = {
        "_aStampIds": stamp_ids,
    }

    return session.patch(url, json = data)
