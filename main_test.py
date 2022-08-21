import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_route():
    response = client.get('/roleUsers/337c929384d461e87dd550e15a8d6ff7c6878247')
    assert response.status_code == 400

def test_route_no_content():
    response = client.get('/roleUsers/test')
    assert response.status_code == 204