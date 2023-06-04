__all__ = [
    "get_todos",
    "get_todos_count_and_latest_id_and_text",
    "add_todo",
    "change_todo",
    "remove_todo",
]

from .aliases import *
from .paths import (
    TODOS_LIST_URL,
    TODOS_ADD_URL,
    TODOS_CHANGE_URL,
    TODOS_REMOVE_URL,
)

TODO_FIELDS = [
    "_sText", # "test"
    "_nPriority", # 2
    "_nCompletion", # 0
    "_dsDeadline", # "2024-01-30"
    "_sColor", # "#ffffff"
    "_bIsSticky", # False
]

def get_todos(session: Session, model_name: str, id_: int) -> Response:
    """Return todos list"""

    url = TODOS_LIST_URL.format(model_name, id_)

    return session.get(url)

def get_todos_count_and_latest_id_and_text(response: Response) -> tuple[int, int, str]: # refactor ?
    """Return todos count and latest todo's id and source text"""

    body = response.json()

    count = body["_aMetadata"]["_nRecordCount"]
    record = body["_aRecords"][0]
    latest_id = record["_idRow"]
    source_text = record["_sText"]

    return count, latest_id, source_text

def add_todo(session: Session, model_name: str, id_: int, source_text: str,
             priority: int = 2, completion: int = 0, deadline: str = None,
             color: str = None, sticky: bool = None) -> Response:
    """Add Todo"""

    url = TODOS_ADD_URL.format(model_name, id_)

    data = {
        "_sText": source_text,
        "_nPriority": priority,
        "_nCompletion": completion,
    }

    if deadline:
        data.update({"_dsDeadline" : deadline})

    if color:
        data.update({"_sColor" : color})

    if sticky:
        data.update({"_bIsSticky" : sticky})

    return session.post(url, json = data)

def change_todo(session: Session, todo_id: int, source_text: str, **kwargs) -> Response:
    """Change Todo"""

    url = TODOS_CHANGE_URL.format(todo_id)

    data = {
        "_sText": source_text,
    }

    if kwargs:
        for k, v in kwargs.items():
            if k != "_sText" and k in TODO_FIELDS:
                data.update({k : v})

    return session.patch(url, json = data)

def remove_todo(session: Session, todo_id: int) -> Response:
    """Remove Todo"""

    url = TODOS_REMOVE_URL.format(todo_id)

    return session.delete(url)
