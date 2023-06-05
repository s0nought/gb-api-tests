__all__ = [
    "get_issues",
    "get_issues_count_and_latest_id_and_text",
    "add_issue",
    "change_issue",
    "remove_issue",
]

from .aliases import *
from .paths import (
    ISSUES_LIST_URL,
    ISSUES_ADD_URL,
    ISSUES_CHANGE_URL,
    ISSUES_REMOVE_URL,
)

ISSUE_FIELDS = [
    "_sText", # "test"
    "_bIsSticky", # True
    "_sState", # "open|closed"
]

def get_issues(session: Session, model_name: str, id_: int, page: int = 1) -> Response:
    """Return issues list"""

    url = ISSUES_LIST_URL.format(model_name, id_, page)

    return session.get(url)

# Can't request issues count with get_model_properties
def get_issues_count_and_latest_id_and_text(response: Response) -> tuple[int, int, str]:
    """Return issues count and latest issue's id and text"""

    body = response.json()

    count = body["_aMetadata"]["_nRecordCount"]
    record = body["_aRecords"][0]

    issue_id = 0
    source_text = ""

    if record:
        issue_id = record["_idRow"]
        source_text = record["_sText"]

    return count, issue_id, source_text

def add_issue(session: Session, model_name: str, id_: int, source_text: str,
              state: str = "open", sticky: bool = False) -> Response:
    """Add Issue"""

    url = ISSUES_ADD_URL.format(model_name, id_)

    data = {
        "_sText": source_text,
        "_bIsSticky": sticky,
        "_sState": state,
    }

    return session.post(url, json = data)

def change_issue(session: Session, issue_id: int, source_text: str, **kwargs) -> Response:
    """Change Issue"""

    url = ISSUES_CHANGE_URL.format(issue_id)

    data = {
        "_sText": source_text,
    }

    if kwargs:
        for k, v in kwargs.items():
            if k != "_sText" and k in ISSUE_FIELDS:
                data.update({k : v})

    return session.patch(url, json = data)

def remove_issue(session: Session, issue_id: int) -> Response:
    """Remove Issue"""

    url = ISSUES_REMOVE_URL.format(issue_id)

    return session.delete(url)
