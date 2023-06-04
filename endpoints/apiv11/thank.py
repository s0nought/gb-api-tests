__all__ = [
    "get_thankers",
    "get_thankers_count",
    "add_thank",
]

from .aliases import *
from .paths import (
    THANKERS_LIST_URL,
    THANK_ADD_URL,
)
from .model import (
    get_model_properties,
)

def get_thankers(session: Session, model_name: str, id_: int, page: int = 1) -> Response:
    """Return thankers list"""

    url = THANKERS_LIST_URL.format(model_name, id_, page)

    return session.get(url)

def get_thankers_count(session: Session, model_name: str, id_: int, properties: str = "_nThanksCount") -> int:
    """Return thankers count"""

    res = get_model_properties(session, model_name, id_, properties)

    return res.json()[properties]

def add_thank(session: Session, model_name: str, id_: int, points_amount: int = 5) -> Response:
    """Add Thank"""

    url = THANK_ADD_URL.format(model_name, id_)

    data = {
        "_nPointsToDonate": points_amount,
    }

    return session.post(url, json = data)
