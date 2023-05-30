import pytest

from modules.constants import BASE_URL_API, USER_NAME
from modules.formdata import EVENT_DATA
from modules.utils import get_add_url
from modules.utils_parse import get_id, get_formdata

MODEL_NAME = "Event"
CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"
ADD_URL = get_add_url(MODEL_NAME)

@pytest.mark.usefixtures("api_session")
def test_fn(api_session):
    form_html = api_session.get(ADD_URL).text
    form_data = get_formdata(form_html, EVENT_DATA)
    res_html = api_session.post(ADD_URL, form_data).text

    submission_id = get_id(res_html)
    submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
    submission_props = api_session.get(submission_url).json()

    assert submission_props["_idRow"] == submission_id
    assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
    assert submission_props["_sText"] == EVENT_DATA["text"]
