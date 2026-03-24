import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()["status"] == "OK."


def test_math_dummy():
    assert 10 + 10 == 20


def test_app_is_testing(client):
    assert app.config['TESTING'] is True