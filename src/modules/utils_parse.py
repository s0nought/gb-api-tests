from bs4 import BeautifulSoup, SoupStrainer

from .selectors import CSS_SELECTORS

def get_id(html: str) -> int:
    """Parse Submission's ID"""

    breadcrumbs = SoupStrainer("nav", attrs = {"id": "Breadcrumb"})
    soup = BeautifulSoup(html, "html.parser", parse_only = breadcrumbs)
    return int((soup.select_one("a:last-child"))["href"].split("/")[-1])

def get_formdata(html: str, entries: dict[str, str]) -> dict[str, str]:
    """Parse FormData"""

    entries_list = entries.keys()

    form = SoupStrainer("form", class_ = "MainForm")
    soup = BeautifulSoup(html, "html.parser", parse_only = form)

    data = dict()

    token = soup.select_one(CSS_SELECTORS["token"])
    data.update({token["name"] : token["value"]})

    form_name = soup.select_one(CSS_SELECTORS["form_name"])
    data.update({form_name["name"] : form_name["value"]})

    if "title" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["title"])
        data.update({tag["name"] : entries["title"]})

    if "game" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["game"])
        data.update({tag["name"] : entries["game"]})

    if "category" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["category"])
        data.update({tag["name"] : entries["category"]})

    if "text" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["text"])
        data.update({tag["name"] : entries["text"]})

    if "subtitle" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["subtitle"])
        data.update({tag["name"] : entries["subtitle"]})

    if "access" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["access"])
        data.update({tag["name"] : entries["access"]})

    if "toc" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["toc"])
        data.update({tag["name"] : entries["toc"]})

    if "analytics" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["analytics"]) # requires unlock
        data.update({tag["name"] : entries["analytics"]})

    if "comments" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["comments"])
        data.update({tag["name"] : entries["comments"]})

    if "start_date_month" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["start_date_month"])
        data.update({tag["name"] : entries["start_date_month"]})

    if "start_date_day" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["start_date_day"])
        data.update({tag["name"] : entries["start_date_day"]})

    if "start_date_year" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["start_date_year"])
        data.update({tag["name"] : entries["start_date_year"]})

    if "start_date_hour" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["start_date_hour"])
        data.update({tag["name"] : entries["start_date_hour"]})

    if "start_date_minute" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["start_date_minute"])
        data.update({tag["name"] : entries["start_date_minute"]})

    if "end_date_month" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["end_date_month"])
        data.update({tag["name"] : entries["end_date_month"]})

    if "end_date_day" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["end_date_day"])
        data.update({tag["name"] : entries["end_date_day"]})

    if "end_date_year" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["end_date_year"])
        data.update({tag["name"] : entries["end_date_year"]})

    if "end_date_hour" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["end_date_hour"])
        data.update({tag["name"] : entries["end_date_hour"]})

    if "end_date_minute" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["end_date_minute"])
        data.update({tag["name"] : entries["end_date_minute"]})

    if "timezone" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["timezone"])
        data.update({tag["name"] : entries["timezone"]})

    if "repeat" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["repeat"])
        data.update({tag["name"] : entries["repeat"]})

    if "location" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["location"])
        data.update({tag["name"] : entries["location"]})

    if "image" in entries_list:
        tag = soup.select_one(CSS_SELECTORS["image"])
        data.update({"_sTicketId" : ""})
        data.update({tag["name"] : "REPLACE_WITH_IMAGE_LIST"})

    return data