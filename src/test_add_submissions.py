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

@pytest.mark.usefixtures("api_session")
class TestAddSubmissions:

    @pytest.fixture(scope = "function")
    def w8(request):
        sleep(1.337)
        yield None

    @pytest.mark.regress
    def test_add_event(self, w8, api_session):
        MODEL_NAME = "Event"
        CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"
        ADD_URL = get_add_url(MODEL_NAME)

        form_html = api_session.get(ADD_URL).text
        form_data = get_formdata(form_html, EVENT_DATA)
        res_html = api_session.post(ADD_URL, form_data).text

        submission_id = get_id(res_html)
        submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
        submission_props = api_session.get(submission_url).json()

        assert submission_props["_idRow"] == submission_id
        assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
        assert submission_props["_sText"] == EVENT_DATA["text"]

    @pytest.mark.regress
    def test_add_project(self, w8, api_session):
        MODEL_NAME = "Project"
        CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"
        ADD_URL = get_add_url(MODEL_NAME)

        form_html = api_session.get(ADD_URL).text
        form_data = get_formdata(form_html, PROJECT_DATA)
        res_html = api_session.post(ADD_URL, form_data).text

        submission_id = get_id(res_html)
        submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
        submission_props = api_session.get(submission_url).json()

        assert submission_props["_idRow"] == submission_id
        assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
        assert submission_props["_sText"] == PROJECT_DATA["text"]

    @pytest.mark.regress
    def test_add_question(self, w8, api_session):
        MODEL_NAME = "Question"
        CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"
        ADD_URL = get_add_url(MODEL_NAME)

        form_html = api_session.get(ADD_URL).text
        form_data = get_formdata(form_html, QUESTION_DATA)
        res_html = api_session.post(ADD_URL, form_data).text

        submission_id = get_id(res_html)
        submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
        submission_props = api_session.get(submission_url).json()

        assert submission_props["_idRow"] == submission_id
        assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
        assert submission_props["_sText"] == QUESTION_DATA["text"]

    @pytest.mark.regress
    def test_add_request(self, w8, api_session):
        MODEL_NAME = "Request"
        CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"
        ADD_URL = get_add_url(MODEL_NAME)

        form_html = api_session.get(ADD_URL).text
        form_data = get_formdata(form_html, REQUEST_DATA)
        res_html = api_session.post(ADD_URL, form_data).text

        submission_id = get_id(res_html)
        submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
        submission_props = api_session.get(submission_url).json()

        assert submission_props["_idRow"] == submission_id
        assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
        assert submission_props["_sText"] == REQUEST_DATA["text"]

    @pytest.mark.regress
    def test_add_script(self, w8, api_session):
        MODEL_NAME = "Script"
        CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"
        ADD_URL = get_add_url(MODEL_NAME)

        form_html = api_session.get(ADD_URL).text
        form_data = get_formdata(form_html, SCRIPT_DATA)
        res_html = api_session.post(ADD_URL, form_data).text

        submission_id = get_id(res_html)
        submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
        submission_props = api_session.get(submission_url).json()

        assert submission_props["_idRow"] == submission_id
        assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
        assert submission_props["_sText"] == SCRIPT_DATA["text"]

    @pytest.mark.smoke
    @pytest.mark.regress
    def test_add_thread(self, w8, api_session):
        MODEL_NAME = "Thread"
        CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"
        ADD_URL = get_add_url(MODEL_NAME)

        form_html = api_session.get(ADD_URL).text
        form_data = get_formdata(form_html, THREAD_DATA)
        res_html = api_session.post(ADD_URL, form_data).text

        submission_id = get_id(res_html)
        submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
        submission_props = api_session.get(submission_url).json()

        assert submission_props["_idRow"] == submission_id
        assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
        assert submission_props["_sText"] == THREAD_DATA["text"]

    @pytest.mark.regress
    def test_add_ware(self, w8, api_session):
        MODEL_NAME = "Ware"
        CSV_PROPERTIES = "_idRow,_aSubmitter,_sText"
        ADD_URL = get_add_url(MODEL_NAME)

        form_html = api_session.get(ADD_URL).text
        form_data = get_formdata(form_html, WARE_DATA)
        res_html = api_session.post(ADD_URL, form_data).text

        submission_id = get_id(res_html)
        submission_url = f"{BASE_URL_API}/{MODEL_NAME}/{submission_id}?_csvProperties={CSV_PROPERTIES}"
        submission_props = api_session.get(submission_url).json()

        assert submission_props["_idRow"] == submission_id
        assert submission_props["_aSubmitter"]["_sName"] == USER_NAME
        assert submission_props["_sText"] == WARE_DATA["text"]
