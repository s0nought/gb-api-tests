"""Add a Event and test if actual properties of the created submission match expected"""

from modules.constants import (
    USER_NAME,
    EVENT_FORM_ENTRIES,
    ADD_EVENT_URL
)

from modules.fixtures import api_session

from modules.utils import (
    get_response_text,
    get_formdata,
    send_formdata,
    get_submission_properties,
    get_page_id
)

from modules.utils_image import upload_file

def test_add_thread(api_session):
    form_html = get_response_text(api_session, ADD_EVENT_URL)
    form_data = get_formdata(form_html, EVENT_FORM_ENTRIES)

    # I've confirmed I can upload images and return _sTicketId
    # and construct FormData containing the mentioned field.
    # It'd POST successfully. Still, there's no image I've uploaded.
    # 
    # Commenting this block out for now.
    # 
    # file_name, file_path, mime_type = EVENT_FORM_ENTRIES["image"]
    # file, ticket_id = upload_file(api_session, file_name, file_path, mime_type)
    # form_data.update({"_sTicketId": ticket_id})

    res_html = send_formdata(api_session, ADD_EVENT_URL, form_data)
    submission_id = get_page_id(res_html)
    submission_props = get_submission_properties(api_session, "Event", submission_id, "_idRow,_aSubmitter,_sText")

    assert submission_props["_idRow"] == submission_id
    assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
    assert submission_props["_sText"] == EVENT_FORM_ENTRIES["text"]
