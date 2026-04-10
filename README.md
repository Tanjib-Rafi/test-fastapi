# Traffic Monitoring API 🚦

A simple and robust FastAPI application for monitoring and recording real-time traffic data, deployed on Render.

## 🚀 Live API
The API is live at: [https://test-fastapi-x371.onrender.com](https://test-fastapi-x371.onrender.com)

- **Interactive API Docs (Swagger)**: [https://test-fastapi-x371.onrender.com/docs](https://test-fastapi-x371.onrender.com/docs)
- **Health Check**: [https://test-fastapi-x371.onrender.com/traffic/health](https://test-fastapi-x371.onrender.com/traffic/health)

---

## 🛠 API Usage

### 1. Get All Traffic Data
Retrieve a list of all recorded traffic events, sorted by the most recent.

**URL**: `GET /traffic/`
```bash
curl --location 'https://test-fastapi-x371.onrender.com/traffic/'
```

### 2. Bulk Insert Traffic Data
Insert multiple traffic records at once.

**URL**: `POST /traffic/bulk`
```bash
curl --location 'https://test-fastapi-x371.onrender.com/traffic/bulk' \
--header 'Content-Type: application/json' \
--data '{
  "data": [
    {
      "timestamp": "2026-04-08T12:00:00",
      "location_id": "LOC123",
      "vehicle_count": 25,
      "average_speed": 45.5,
      "congestion_level": "medium"
    },
    {
      "timestamp": "2026-04-08T12:01:00",
      "location_id": "LOC124",
      "vehicle_count": 30,
      "average_speed": 40.0,
      "congestion_level": "high"
    },
    {
      "timestamp": "2026-04-08T12:02:00",
      "location_id": "LOC125",
      "vehicle_count": 15,
      "average_speed": 50.0,
      "congestion_level": "low"
    }
  ]
}'
```

---

## 🧪 Testing
The project includes a comprehensive test suite using `pytest` with an isolated SQLite database.

To run the tests locally:
```bash
# From the test-fastapi/test-fastapi directory
../venv/bin/python3 -m pytest
```

---

## 💻 Local Development

1. **Activate Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Run the Application**:
   ```bash
   cd test-fastapi
   uvicorn api.main:app --reload
   ```

3. **Check Local Logs**: The application will be available at `http://127.0.0.1:8000`.
