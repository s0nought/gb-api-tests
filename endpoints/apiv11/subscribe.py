__all__ = [
    "get_subscriber_count",
    "subscribe",
    "unsubscribe",
]

from .aliases import *
from .paths import (
    SUBSCRIBE_ADD_URL,
    SUBSCRIBE_REMOVE_URL,
)
from .model import (
    get_model_properties,
)

def get_subscriber_count(session: Session, model_name: str, id_: int, properties: str = "_nSubscriberCount") -> int:
    """Return subscriber count"""

    res = get_model_properties(session, model_name, id_, properties)

    return res.json()[properties]

def subscribe(session: Session, model_name: str, id_: int) -> Response:
    """Subscribe"""

    url = SUBSCRIBE_ADD_URL.format(model_name, id_)

    return session.post(url, json = {})

def unsubscribe(session: Session, subscription_id: int) -> Response:
    """Unsubscribe"""

    url = SUBSCRIBE_REMOVE_URL.format(subscription_id)

    return session.delete(url)
