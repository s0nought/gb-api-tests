import pytest
import requests

from .assertions import assert_status_code
from .constants import BASE_URL_API
from .credentials import credentials

Session = requests.sessions.Session

@pytest.fixture(scope = "session")
def api_session() -> Session:
    """Set up an authenticated Session"""

    session = requests.Session()

    url = f"{BASE_URL_API}/Member/Authenticate"
    data = credentials
    response = session.post(url, json = data)

    assert_status_code(response, 200)

    yield session
