"""Upload a Image"""

from modules.assertions import assert_status_code

from modules.fixtures import api_session

from modules.utils_image import upload_file

from modules.constants import EVENT_FORM_ENTRIES # temporary

def test_upload_image(api_session):
    file_name, file_path, mime_type = EVENT_FORM_ENTRIES["image"]
    file, ticket_id = upload_file(api_session, file_name, file_path, mime_type)

    url_event = f"https://images.gamebanana.com/img/banners/events/{file}"
    # url_mod = f"https://files.gamebanana.com/img/ss/mods/{file}"
    res = api_session.get(url_event)

    assert_status_code(res, 200)
    assert len(res.headers["etag"]) > 0
