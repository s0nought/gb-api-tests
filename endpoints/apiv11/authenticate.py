__all__ = [
    "log_in",
]

from .aliases import *
from .paths import (
    AUTHENTICATE_URL,
)

def log_in(session: Session, user_name: str, password: str) -> Response:
    """Authenticate"""

    url = AUTHENTICATE_URL

    data = {
        "_sUsername": user_name,
        "_sPassword": password,
    }

    return session.post(url, json = data)
