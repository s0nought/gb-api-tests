from datetime import datetime

from .constants import BASE_URL, GAME_ID, LOREM_IPSUM
from .dictionaries import PLURALS

def get_lorem_ipsum() -> str:
    """Return lorem ipsum with a timestamp"""

    return f"{LOREM_IPSUM} {str(datetime.utcnow())}"

def get_add_url(model_name: str) -> str:
    """Return Add <model_name> page URL"""

    return f"{BASE_URL}/{PLURALS[model_name]}/add?gameid={GAME_ID}"
