from modules.assertions import assert_status_code

def upload_file(api_session, file_name: str, file_path: str, mime_type: str) -> tuple[str, str]:
    """Send POST request (Multi-Part) and return file info"""

    url = "https://gamebanana.com/responders/jfu"

    data = {
        "d": "81b8761ab78e51033f13947a1d6ba1c1" # event
        # "d": "e36b3626ab232d1ce51ae9d79dfded05" # mod
    }

    files = {
        "files[]": (file_name, open(file_path, mode = "rb"), mime_type)
    }

    res = api_session.post(url, files = files, data = data)
    assert_status_code(res, 200)

    file_info = res.json()["files"][0]
    return file_info["_sFile"], file_info["_sTicketId"]
