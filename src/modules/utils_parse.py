import re

from bs4 import BeautifulSoup, SoupStrainer

from .selectors import CSS_SELECTORS

def get_id(html: str) -> int:
    """Parse Submission's ID"""

    breadcrumbs = SoupStrainer("nav", attrs = {"id": "Breadcrumb"})
    soup = BeautifulSoup(html, "html.parser", parse_only = breadcrumbs)
    return int((soup.select_one("a:last-child"))["href"].split("/")[-1])

CUSTOM_ACTION_ENTRIES = [
    "image",
    "request_requirements",
    "submission_authors",
    "license_checklist",
    "requirements"
]

def get_formdata(html: str, entries: dict[str, str]) -> dict[str, str]:
    """Parse FormData"""

    form = SoupStrainer("form", class_ = "MainForm")
    soup = BeautifulSoup(html, "html.parser", parse_only = form)

    data = dict()

    # token and form_name are required

    token = soup.select_one(CSS_SELECTORS["token"])
    data.update({token["name"] : token["value"]})

    form_name = soup.select_one(CSS_SELECTORS["form_name"])
    data.update({form_name["name"] : form_name["value"]})

    for k, v in entries.items():

        if k not in CUSTOM_ACTION_ENTRIES:
            tag = soup.select_one(CSS_SELECTORS[k])
            data.update({tag["name"] : v})
            continue

        if k == "image":
            tag = soup.select_one(CSS_SELECTORS[k])

            data.update({"_sTicketId" : ""})
            data.update({tag["name"] : "REPLACE_WITH_IMAGE_LIST"})

        if k == "request_requirements":
            tag = soup.select_one(CSS_SELECTORS[k])
            data.update({tag["id"] + "[]" : v})

        if k == "submission_authors":
            match = re.findall(CSS_SELECTORS[k], html)
            name = match[0][16:-2]

            # refactor
            for i in range(1, 5):
                group_name, user_id, author_name, author_url, author_roles = entries["submission_authors"][i - 1]
                data.update({f"{name}[{i}][group_name]" : group_name})
                data.update({f"{name}[{i}][author_userids][]" : user_id})
                data.update({f"{name}[{i}][author_names][]" : author_name})
                data.update({f"{name}[{i}][author_offsite_urls][]" : author_url})
                data.update({f"{name}[{i}][author_roles][]" : author_roles})

        if k == "license_checklist":
            tag = soup.select_one(CSS_SELECTORS[k])
            name = tag["name"].split("[")[0]

            # why does it require 6 items?
            for i in range(1, 7):
                data.update({f"{name}[_aOptions][{i}]" : v})

        if k == "requirements":
            tags = soup.select(CSS_SELECTORS[k])

            for i in range(len(tags)):
                data.update({tags[i]["name"] : v[i]})

    return data
