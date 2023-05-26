import pytest

from modules.constants import EVENT_IMAGE_BASE_URL, MOD_IMAGE_BASE_URL
from modules.dictionaries import IMAGE_UPLOADER_D
from modules.fixtures import api_session
from modules.formdata import EVENT_IMAGE, MOD_IMAGE_1
from modules.utils import send_get_request, upload_image

@pytest.mark.parametrize("model_name, image, base_url", [
        ("Event", EVENT_IMAGE, EVENT_IMAGE_BASE_URL),
        ("Mod", MOD_IMAGE_1, MOD_IMAGE_BASE_URL)
    ])
def test_fn(api_session, model_name, image, base_url):
    sfile, ticket_id = upload_image(api_session, model_name, image)
    url = base_url + sfile
    res = send_get_request(api_session, url)

    assert len(res.headers["etag"]) > 0
