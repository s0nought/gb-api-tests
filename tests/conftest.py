import pytest
import requests

from common.constants import BASE_URL_API
from common.credentials import CREDENTIALS

@pytest.fixture(scope = "session")
def api_session() -> requests.sessions.Session:
    """Set up an authenticated Session"""

    session = requests.Session()

    url = f"{BASE_URL_API}/Member/Authenticate"
    data = CREDENTIALS

    response = session.post(url, json = data)
    body = response.json()

    assert response.status_code == 200
    assert body["_sStatus"] == "SUCCESS"

    yield session
