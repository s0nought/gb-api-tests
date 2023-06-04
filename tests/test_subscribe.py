import pytest

from apiv11.subscribe import *

subscription_id = 0

@pytest.mark.usefixtures("api_session")
@pytest.mark.parametrize("model_name, id_", [("Mod", 444709)])
class TestSubscribe:

    def test_subscribe(api_session, model_name, id_):
        global subscription_id

        count_before = get_subscriber_count(api_session, model_name, id_)

        res = subscribe(api_session, model_name, id_)
        body = res.json()

        assert body["_sSuccessCode"] == "SUBSCRIPTION_ADDED"
        assert body["_bAccessorIsSubscribed"] == True

        subscription_id = body["_idAccessorSubscriptionRow"]
        count_after = body["_nSubscriberCount"]

        assert count_after == count_before + 1

    def test_unsubscribe(api_session, model_name, id_):
        global subscription_id

        count_before = get_subscriber_count(api_session, model_name, id_)

        res = unsubscribe(api_session, subscription_id)
        body = res.json()

        assert body["_sSuccessCode"] == "SUBSCRIPTION_REMOVED"
        assert body["_bAccessorIsSubscribed"] == False

        count_after = body["_nSubscriberCount"]

        assert count_before - 1 == count_after
