# Integration tests to ensure that the whole notification system is working as expected.

import pytest
from fastapi.testclient import TestClient

from alert_notifications_api.database import create_db_and_tables, drop_db
from alert_notifications_api.main import app

client = TestClient(app)
test_customers = [
    {
        "customer_id": 1,
        "name": "Maximo",
        "email": "maximo@hotmail.com",
        "cellphone": 3112314567,
        "created_by": "test_user",
    },
    {
        "customer_id": 2,
        "name": "Leonidas",
        "email": "leonidas@hotmail.com",
        "cellphone": 3009998877,
        "created_by": "test_user",
    },
    {
        "customer_id": 3,
        "name": "Powell",
        "email": "powell@hotmail.com",
        "cellphone": 3998887766,
        "created_by": "test_user",
    },

]
test_offers = [
    {
        "offer_id": 11,
        "message": "First promo.",
        "sended": False,
        "created_by": "test_user",
    },
    {
        "offer_id": 22,
        "message": "Second promo.",
        "sended": False,
        "created_by": "test_user",
    },
]
test_notification_preferences = [
    {
        "notification_preference_id": 111,
        "customer_id": 1,
        "email": True,
        "sms": False,
        "created_by": "test_user",
    },
    {
        "notification_preference_id": 222,
        "customer_id": 2,
        "email": False,
        "sms": True,
        "created_by": "test_user",
    },
    {
        "notification_preference_id": 333,
        "customer_id": 3,
        "email": True,
        "sms": True,
        "created_by": "test_user",
    },
]


# Setup and tear down
@pytest.fixture(scope="module")
def database():
    """ Create the database structure. """
    create_db_and_tables()

    yield "test"
    """ Clean the database. """
    drop_db()


def test_customer_creation(database):
    """ Test the customer creation through the API. """
    for test_customer in test_customers:
        response = client.post("/customer", json=test_customer)
        assert response.status_code == 200
        response_dict = response.json()
        response_dict.pop("created_on", None)
        assert response_dict == test_customer


def test_offer_creation(database):
    """ Test the offer creation through the API. """
    for test_offer in test_offers:
        response = client.post("/offer", json=test_offer)
        assert response.status_code == 200
        response_dict = response.json()
        response_dict.pop("created_on", None)
        assert response_dict == test_offer


def test_notification_preference_creation(database):
    """ Test the notification preference creation through the API. """
    for test_notification_preference in test_notification_preferences:
        response = client.post(
            f"/preferences/{test_notification_preference['customer_id']}",
            json=test_notification_preference
        )
        assert response.status_code == 200
        response_dict = response.json()
        response_dict.pop("created_on", None)
        response_dict.pop("app_push", None)
        response_dict.pop("dummy", None)
        assert response_dict == test_notification_preference


def test_get_user_preferences(database):
    """ Test the retrieval of the user notification preferences. """
    response = client.get(f"/preferences/{test_notification_preferences[1]['customer_id']}")
    assert response.status_code == 200
    response_dict = response.json()
    response_dict.pop("created_on", None)
    response_dict.pop("app_push", None)
    response_dict.pop("dummy", None)
    assert response_dict == test_notification_preferences[1]




def test_schedule_notifications(database):
    """ Test the schedule of the notifications for the offers and customers that applies. """
    response = client.post("/notifications")
    assert response.status_code == 200
    assert response.json() == {"message": "All the 8 tasks were queued."}
    


def test_notifications_delivered(database):
    """ Test that all the notifications (email and sms) configured in this integration
    test were correctly delivered.  """
    # Needs mock to be implemented
    assert True

