import pytest

from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_root(client):
    r = client.get('/')
    assert b'Hello, world!' in r.data
