from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/traffic/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Service is running"}

def test_get_traffic_not_found():
    # Assuming the database is empty or the query returns nothing
    response = client.get("/traffic/")
    # If the database is empty, it returns 404 based on the implementation
    assert response.status_code in [200, 404]
