"""Add a Thread and test if actual properties of the created thread match expected"""

from modules.constants import (
    USER_NAME,
    ACCESS_MAP,
    TOC_MAP,
    COMMENTS_MODE_MAP,
    CSS_SELECTORS,
    ADD_THREAD_URL
)

from modules.fixtures import api_session

from modules.utils import (
    get_response_text,
    send_formdata,
    get_submission_properties,
    get_lorem_ipsum
)

from bs4 import BeautifulSoup, SoupStrainer

TITLE = "Test Thread"
TEXT = get_lorem_ipsum()
CATEGORY = "5148" # Other/Misc
SUBTITLE = ""
ACCESS = ACCESS_MAP["Private"]
TOC = TOC_MAP["Disabled"]
COMMENTS = COMMENTS_MODE_MAP["Open"]

def get_formdata(html: str) -> dict:
    """Parse FormData from page HTML"""

    form = SoupStrainer("form", class_ = "MainForm")
    soup = BeautifulSoup(html, "html.parser", parse_only = form)

    token = soup.select_one(CSS_SELECTORS["token"])
    title = soup.select_one(CSS_SELECTORS["title"])
    game = soup.select_one(CSS_SELECTORS["game"])
    category = soup.select_one(CSS_SELECTORS["category"])
    text = soup.select_one(CSS_SELECTORS["text"])
    subtitle = soup.select_one(CSS_SELECTORS["subtitle"])
    access = soup.select_one(CSS_SELECTORS["access"])
    toc = soup.select_one(CSS_SELECTORS["toc"])
    # analytics = soup.select_one(CSS_SELECTORS["analytics"]) # requires unlock
    comments = soup.select_one(CSS_SELECTORS["comments"])
    form_name = soup.select_one(CSS_SELECTORS["form_name"])

    return {
        token["name"]: token["value"],
        title["name"]: TITLE,
        game["name"]: game["value"],
        category["name"]: CATEGORY,
        text["name"]: TEXT,
        subtitle["name"]: SUBTITLE,
        access["name"]: ACCESS,
        toc["name"]: TOC,
        # analytics["name"]: analytics["value"],
        comments["name"]: COMMENTS,
        form_name["name"]: form_name["value"]
    }

def get_thread_id(html: str) -> int:
    """Get ID of the created thread"""

    breadcrumbs = SoupStrainer("nav", attrs = {"id": "Breadcrumb"})
    soup = BeautifulSoup(html, "html.parser", parse_only = breadcrumbs)
    return int((soup.select_one("a:last-child"))["href"].split("/")[-1])

def test_add_thread(api_session):
    form_html = get_response_text(api_session, ADD_THREAD_URL)
    form_data = get_formdata(form_html)
    res_html = send_formdata(api_session, ADD_THREAD_URL, form_data)
    thread_id = get_thread_id(res_html)
    thread_props = get_submission_properties(api_session, "Thread", thread_id, "_idRow,_aSubmitter,_sText")

    assert thread_props["_idRow"] == thread_id
    assert thread_props["_aSubmitter"]["_sName"] == USER_NAME
    assert thread_props["_sText"] == TEXT
