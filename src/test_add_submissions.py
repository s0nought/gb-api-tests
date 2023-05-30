import pytest
from time import sleep

from modules.constants import BASE_URL_API, USER_NAME
from modules.formdata import (
    EVENT_DATA,
    PROJECT_DATA,
    QUESTION_DATA,
    REQUEST_DATA,
    SCRIPT_DATA,
    THREAD_DATA,
    WARE_DATA
)
from modules.utils import get_add_url
from modules.utils_parse import get_id, get_formdata

CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"

test_params = "model_name, form_entries"

test_data = [
    pytest.param("Event", EVENT_DATA, marks = pytest.mark.regress, id = "Event"),
    pytest.param("Project", PROJECT_DATA, marks = pytest.mark.regress, id = "Project"),
    pytest.param("Question", QUESTION_DATA, marks = pytest.mark.regress, id = "Question"),
    pytest.param("Request", REQUEST_DATA, marks = pytest.mark.regress, id = "Request"),
    pytest.param("Script", SCRIPT_DATA, marks = pytest.mark.regress, id = "Script"),
    pytest.param("Thread", THREAD_DATA, marks = [pytest.mark.regress, pytest.mark.smoke], id = "Thread"),
    pytest.param("Ware", WARE_DATA, marks = pytest.mark.regress, id = "Ware"),
]

@pytest.fixture(scope = "function")
def w8(request):
    sleep(1.337)
    yield None

@pytest.mark.usefixtures("api_session")
@pytest.mark.parametrize(test_params, test_data)
def test_add(w8, api_session, model_name, form_entries):
    url = get_add_url(model_name)

    form_html = api_session.get(url).text
    form_data = get_formdata(form_html, form_entries)
    res_html = api_session.post(url, form_data).text

    submission_id = get_id(res_html)
    submission_url = f"{BASE_URL_API}/{model_name}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
    submission_props = api_session.get(submission_url).json()

    assert submission_props["_idRow"] == submission_id
    assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
    assert submission_props["_sText"] == form_entries["text"]
