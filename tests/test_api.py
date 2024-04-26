from fastapi.testclient import TestClient

from alert_notifications.controlers.main import app

client = TestClient(app)

def test_api_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "The service is up and running :)"}
