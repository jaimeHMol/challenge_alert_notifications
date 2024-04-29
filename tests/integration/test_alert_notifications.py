from fastapi.testclient import TestClient

from alert_notifications_api.controlers.main import app

client = TestClient(app)

def test_send_notifications():
    """ Integration tests to ensure that the whole notification system is working as
    expected. """

    # Setup
    # Create data base structure


    # Create users, offers and user_notification_preferences


    # Schedule notifications
    response = client.post("/notifications")
    
    # Check email and/or sms were correctly received

    # tear down
    # Remove tables and session
