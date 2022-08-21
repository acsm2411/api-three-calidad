import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_route():
    response = client.get('/roleUsers/0da37474320000bfb14d1cbeb8a508687c5053b0')
    assert response.status_code == 200

def test_route_no_content():
    response = client.get('/roleUsers/test')
    assert response.status_code == 204