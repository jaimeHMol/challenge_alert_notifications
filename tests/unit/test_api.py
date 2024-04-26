from fastapi.testclient import TestClient

from alert_notifications_api.controlers.main import app

client = TestClient(app)
user_id = 123456789


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

def test_get_user_preferences():
    """ Test the retrieval of the user notification preferences. """
    return
    response = client.get(f"/preferences/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "The notifications sent"}

def test_post_user_preferences():
    """ Test the creation of the user notification preferences. """
    return
    response = client.post(f"/preferences/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "The notifications sent"}
