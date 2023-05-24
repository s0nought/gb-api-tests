import requests

Response = requests.models.Response

error_message = "Expected {0}, but got {1}"

def assert_status_code(response: Response, expected: int):
    """Test if actual response status code match the expected"""

    actual = response.status_code
    assert actual == expected, error_message.format(expected, actual)
