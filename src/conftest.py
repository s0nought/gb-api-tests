import pytest
import requests

from modules.assertions import assert_status_code
from modules.constants import BASE_URL_API
from modules.credentials import credentials

@pytest.fixture(scope = "session")
def api_session() -> requests.sessions.Session:
    """Set up an authenticated Session"""

    session = requests.Session()

    url = f"{BASE_URL_API}/Member/Authenticate"
    data = credentials

    response = session.post(url, json = data)

    assert_status_code(response, 200)

    yield session
