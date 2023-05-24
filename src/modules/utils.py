from modules.assertions import assert_status_code

from modules.constants import BASE_URL_API, LOREM_IPSUM

from datetime import datetime

from bs4 import BeautifulSoup, SoupStrainer

def get_lorem_ipsum() -> str:
    """Return Lorem ipsum with a timestamp"""

    return f"{LOREM_IPSUM} {str(datetime.utcnow())}"

def get_response_text(api_session, url: str) -> str:
    """Send GET request and return response text"""

    res = api_session.get(url)
    assert_status_code(res, 200)
    return res.text

def send_formdata(api_session, url: str, data: dict) -> str:
    """Send POST request and return response text"""

    res = api_session.post(url, data = data)
    assert_status_code(res, 200)
    return res.text

def get_submission_properties(api_session, model: str, id: int, properties: str) -> dict:
    """Send GET request and return response JSON"""

    res = api_session.get(f"{BASE_URL_API}/{model}/{id}?_csvProperties={properties}")
    assert_status_code(res, 200)
    return res.json()

def get_page_id(html: str) -> int:
    """Parse submission's ID from page HTML"""

    breadcrumbs = SoupStrainer("nav", attrs = {"id": "Breadcrumb"})
    soup = BeautifulSoup(html, "html.parser", parse_only = breadcrumbs)
    return int((soup.select_one("a:last-child"))["href"].split("/")[-1])
