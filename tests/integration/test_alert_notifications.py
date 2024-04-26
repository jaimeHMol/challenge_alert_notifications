from fastapi.testclient import TestClient

from alert_notifications.controlers.main import app

client = TestClient(app)

def test_send_notifications():
    """ Integration tests to ensure that the whole notification system is working as
    expected. """

    # Create user

    # Create notifications preference

    # Schedule notifications
    response = client.post("/notifications")
    
    # Check email and/or sms were correctly received
    