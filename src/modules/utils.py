from datetime import datetime

from .assertions import assert_status_code
from .constants import BASE_URL, LOREM_IPSUM
# from .dictionaries import IMAGE_UPLOADER_D

def get_lorem_ipsum() -> str:
    """Return lorem ipsum with a timestamp"""

    return f"{LOREM_IPSUM} {str(datetime.utcnow())}"

def send_get_request(api_session, url: str):
    """Send GET request and return its response"""

    res = api_session.get(url)
    assert_status_code(res, 200)
    return res

def send_post_request(api_session, url: str, data: dict):
    """Send POST request and return its response"""

    res = api_session.post(url, data = data)
    assert_status_code(res, 200)
    return res

def send_post_multipart_request(api_session, url: str, files: dict, data: dict):
    """Send POST (multipart/form-data) request and return its response"""

    res = api_session.post(url, files = files, data = data)
    assert_status_code(res, 200)
    return res

# see dictionaries.py
# def upload_image(api_session, model_name: str, image: tuple[str, str, str]) -> tuple[str, str]:
#     """Upload an image and return its _sFile and _sTicketId"""

#     file_name, file_path, mime_type = image

#     url = f"{BASE_URL}/responders/jfu"
#     data = {"d": IMAGE_UPLOADER_D[model_name]}
#     files = {"files[]": (file_name, open(file_path, mode = "rb"), mime_type)}

#     res = send_post_multipart_request(api_session, url, files = files, data = data)
#     img = res.json()["files"][0]

#     return img["_sFile"], img["_sTicketId"]
