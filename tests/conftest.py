import pytest
import requests

from apiv11.authenticate import log_in
from credentials import *

@pytest.fixture(scope = "session")
def api_session() -> requests.sessions.Session:
    """Set up an authenticated Session"""

    session = requests.Session()

    res = log_in(session, user_name, password)

    yield session
