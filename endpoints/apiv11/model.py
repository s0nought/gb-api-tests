__all__ = [
    "get_model_properties",
]

from .aliases import *
from .paths import (
    MODEL_PROPERTIES_URL,
)

def get_model_properties(session: Session, model_name: str, id_: int, properties: str = "_idRow") -> Response:
    """Return model properties"""

    url = MODEL_PROPERTIES_URL.format(model_name, id_, properties)

    return session.get(url)
