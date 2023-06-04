__all__ = [
    "get_stamps_list",
    "get_untrash_reasons",
]

from .aliases import *
from .paths import (
    STAMPS_LIST_URL,
    UNTRASH_REASONS_URL,
)

def get_stamps_list(session: Session) -> Response:
    """Return available stamps"""

    return session.get(STAMPS_LIST_URL)

def get_untrash_reasons(session: Session) -> Response:
    """Return available untrash reasons"""

    return session.get(UNTRASH_REASONS_URL)
