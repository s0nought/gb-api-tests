MODEL_NAME = "Request"
CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"

from modules.constants import BASE_URL_API, USER_NAME, ADD_REQUEST_URL
from modules.fixtures import api_session
from modules.formdata import REQUEST_DATA
from modules.utils import send_get_request, send_post_request
from modules.utils_parse import get_id, get_formdata

def test_fn(api_session):
    form_html = (send_get_request(api_session, ADD_REQUEST_URL)).text
    form_data = get_formdata(form_html, REQUEST_DATA)
    res_html = (send_post_request(api_session, ADD_REQUEST_URL, form_data)).text

    submission_id = get_id(res_html)
    submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
    submission_props = (send_get_request(api_session, submission_url)).json()

    assert submission_props["_idRow"] == submission_id
    assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
    assert submission_props["_sText"] == REQUEST_DATA["text"]
