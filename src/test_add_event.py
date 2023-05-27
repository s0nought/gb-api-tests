MODEL_NAME = "Event"
CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"

from modules.constants import BASE_URL_API, USER_NAME, ADD_EVENT_URL
from modules.fixtures import api_session
from modules.formdata import EVENT_DATA
from modules.utils import send_get_request, send_post_request#, upload_image
from modules.utils_parse import get_id, get_formdata

def test_fn(api_session):
    form_html = (send_get_request(api_session, ADD_EVENT_URL)).text
    form_data = get_formdata(form_html, EVENT_DATA)

    # see dictionaries.py
    # sfile, ticket_id = upload_image(api_session, MODEL_NAME, EVENT_DATA["image"])
    # form_data.update({"_sTicketId": ticket_id})

    # for k, v in form_data.items():
    #     if v == "REPLACE_WITH_IMAGE_LIST":
    #         image_field = k

    # form_data.update({image_field : '[{"name":"_sTicketId","value":"' + ticket_id + '"}]'})

    res_html = (send_post_request(api_session, ADD_EVENT_URL, form_data)).text

    submission_id = get_id(res_html)
    submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
    submission_props = (send_get_request(api_session, submission_url)).json()

    assert submission_props["_idRow"] == submission_id
    assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
    assert submission_props["_sText"] == EVENT_DATA["text"]
