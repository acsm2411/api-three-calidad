import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_route():
    response = client.get('/roleUsers/138370d9957f043bdb3afde5dd014298effc0913')
    assert response.status_code == 200

def test_route_no_content():
    response = client.get('/roleUsers/test')
    assert response.status_code == 204