from datetime import datetime

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get("/traffic/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Service is running"}

def test_create_traffic(client):
    """Test creating a single traffic entry."""
    payload = {
        "timestamp": datetime.now().isoformat(),
        "location_id": "LOC-001",
        "vehicle_count": 42,
        "average_speed": 65.5,
        "congestion_level": "low"
    }
    response = client.post("/traffic/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "id" in data

def test_get_all_traffic(client):
    """Test retrieving traffic data after insertion."""
    # First, insert some data
    payload = {
        "timestamp": datetime.now().isoformat(),
        "location_id": "LOC-002",
        "vehicle_count": 100,
        "average_speed": 30.0,
        "congestion_level": "high"
    }
    client.post("/traffic/", json=payload)
    
    # Then, retrieve it
    response = client.get("/traffic/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["location_id"] == "LOC-002"

def test_bulk_insert(client):
    """Test bulk insertion of traffic data."""
    payload = {
        "data": [
            {
                "timestamp": datetime.now().isoformat(),
                "location_id": "BULK-1",
                "vehicle_count": 10,
                "average_speed": 50.0,
                "congestion_level": "low"
            },
            {
                "timestamp": datetime.now().isoformat(),
                "location_id": "BULK-2",
                "vehicle_count": 20,
                "average_speed": 40.0,
                "congestion_level": "medium"
            }
        ]
    }
    response = client.post("/traffic/bulk", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "success", "count": 2}

def test_get_traffic_empty(client):
    """Test retrieving traffic data when the database is empty."""
    # The database is cleared between tests by the fixture
    response = client.get("/traffic/")
    assert response.status_code == 404
    assert response.json()["detail"] == "No traffic data found"
