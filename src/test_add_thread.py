"""Add a Thread and test if actual properties of the created submission match expected"""

from modules.constants import (
    USER_NAME,
    THREAD_FORM_ENTRIES,
    ADD_THREAD_URL
)

from modules.fixtures import api_session

from modules.utils import (
    get_response_text,
    get_formdata,
    send_formdata,
    get_submission_properties,
    get_page_id
)

def test_add_thread(api_session):
    form_html = get_response_text(api_session, ADD_THREAD_URL)
    form_data = get_formdata(form_html, THREAD_FORM_ENTRIES)
    res_html = send_formdata(api_session, ADD_THREAD_URL, form_data)
    submission_id = get_page_id(res_html)
    submission_props = get_submission_properties(api_session, "Thread", submission_id, "_idRow,_aSubmitter,_sText")

    assert submission_props["_idRow"] == submission_id
    assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
    assert submission_props["_sText"] == THREAD_FORM_ENTRIES["text"]
