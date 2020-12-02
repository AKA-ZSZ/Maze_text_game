import pytest
import json

from web import app

@pytest.fixture
def client():
    return app.test_client()

def test_json_list(client):
    req = client.get("/api/list")
    test_contents = req.data.decode()
    assert json.loads(test_contents) == {"scores": []}

def test_json_add(client):
    req = client.put("/api/new", json={"name": "Test", "score": 100.00})
    assert req.status_code == 204

    req = client.get("/api/list")
    assert req.get_json() == {"scores": [{"name": "Test", "score": 100.00}]}

    req = client.put("/api/new", json={})
    assert req.status_code == 400

    req = client.put("/api/new", json={"name": "Test", "score": "100.00"})
    assert req.status_code == 400

    req = client.put("/api/new", json={"name": 123, "score": 100.00})
    assert req.status_code == 400

    req = client.put("/api/new")
    assert req.status_code == 400

    req = client.put("/api/new", json={"name": "Test"})
    assert req.status_code == 400