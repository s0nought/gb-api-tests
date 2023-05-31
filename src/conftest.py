import pytest
import requests

from modules.constants import BASE_URL_API
from modules.credentials import credentials

@pytest.fixture(scope = "session")
def api_session() -> requests.sessions.Session:
    """Set up an authenticated Session"""

    session = requests.Session()

    url = f"{BASE_URL_API}/Member/Authenticate"
    data = credentials

    response = session.post(url, json = data)
    body = response.json()

    assert response.status_code == 200
    assert body["_sStatus"] == "SUCCESS"

    yield session
