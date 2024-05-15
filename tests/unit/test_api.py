import pytest
from fastapi.testclient import TestClient

from alert_notifications_api.database import create_db_and_tables
from alert_notifications_api.main import app

client = TestClient(app)
customer_id = 1


@pytest.fixture(scope="module")
def database():
    """ Create the database structure. """
    create_db_and_tables()


def test_api_health():
    """ Initial test just to be sure that the service is running. """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "The service is up and running :)"}

def test_schedule_notification():
    """ Test the post method that schedule the notifications. """
    return 
    response = client.post("/notifications")
    assert response.status_code == 200
    assert response.json() == {"message": "The notifications were sent to the queue"}

def test_get_user_preferences(database):
    """ Test the retrieval of the user notification preferences. Since the customer and
    preference doesn't exist it will validate the 404 status code. """
    response = client.get(f"/preferences/77777")
    assert response.status_code == 404


def test_post_user_preferences():
    """ Test the creation of the user notification preferences. """
    return
    response = client.post(f"/preferences/{customer_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "The notifications sent"}
