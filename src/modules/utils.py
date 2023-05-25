from modules.assertions import assert_status_code

from modules.constants import BASE_URL_API

from bs4 import BeautifulSoup, SoupStrainer

from modules.constants import CSS_SELECTORS

def get_response_text(api_session, url: str) -> str:
    """Send GET request and return response text"""

    res = api_session.get(url)
    assert_status_code(res, 200)
    return res.text

def get_formdata(html: str, entries: dict[str, str]) -> dict[str, str]:
    """Parse FormData from page HTML"""

    entries_list = entries.keys()

    form = SoupStrainer("form", class_ = "MainForm")
    soup = BeautifulSoup(html, "html.parser", parse_only = form)

    result = dict()

    token = soup.select_one(CSS_SELECTORS["token"])
    result.update({token["name"] : token["value"]})

    form_name = soup.select_one(CSS_SELECTORS["form_name"])
    result.update({form_name["name"] : form_name["value"]})

    if "title" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["title"])
        result.update({tag["name"] : entries["title"]})

    if "game" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["game"])
        result.update({tag["name"] : entries["game"]})

    if "category" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["category"])
        result.update({tag["name"] : entries["category"]})

    if "text" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["text"])
        result.update({tag["name"] : entries["text"]})

    if "subtitle" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["subtitle"])
        result.update({tag["name"] : entries["subtitle"]})

    if "access" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["access"])
        result.update({tag["name"] : entries["access"]})

    if "toc" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["toc"])
        result.update({tag["name"] : entries["toc"]})

    if "analytics" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["analytics"]) # requires unlock
        result.update({tag["name"] : entries["analytics"]})

    if "comments" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["comments"])
        result.update({tag["name"] : entries["comments"]})

    return result

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
