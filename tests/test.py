import pytest
import time
from backend.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        app.config["TESTING"] = True
        yield client

def test_status_pending(client):
    # Test initial "Pending" status
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json.get("result") == "Pending"

def test_status_completed(client):
    # Simulate time passing to test "completed" status
    app.config["START_TIME"] = time.time() - 20
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json.get("result") == "Completed"

def test_invalid_endpoint(client):
    # Test invalid endpoint
    response = client.get('/home')
    assert response.status_code == 404
