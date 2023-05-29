from modules.constants import BASE_URL_API, USER_NAME
from modules.fixtures import api_session
from modules.formdata import SCRIPT_DATA
from modules.utils import get_add_url, send_get_request, send_post_request
from modules.utils_parse import get_id, get_formdata

MODEL_NAME = "Script"
CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"
ADD_URL = get_add_url(MODEL_NAME)

def test_fn(api_session):
    form_html = (send_get_request(api_session, ADD_URL)).text
    form_data = get_formdata(form_html, SCRIPT_DATA)
    res_html = (send_post_request(api_session, ADD_URL, form_data)).text

    submission_id = get_id(res_html)
    submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
    submission_props = (send_get_request(api_session, submission_url)).json()

    assert submission_props["_idRow"] == submission_id
    assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
    assert submission_props["_sText"] == SCRIPT_DATA["text"]
