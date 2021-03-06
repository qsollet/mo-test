import pytest

from main import app, calculate_ride

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_root(client):
    r = client.post('/api/v1/rides', json={"rides":[{
        "id": 1,
        "distance": 2,
        "startTime": "2020-06-19T13:01:17.031Z",
        "duration": 9000
    }]})
    assert b'{"rides":[{"cost":6.0,"distance":2,"duration":9000,"id":1,"startTime":"2020-06-19T13:01:17.031Z"}]}\n' in r.data

def test_calculate_ride():
    assert calculate_ride(13, 2) == 6

def test_calculate_ride_night():
    assert calculate_ride(21, 4) == 21
    assert calculate_ride(4, 10) == 51

def test_calculate_ride_evening():
    assert calculate_ride(17, 5) == 38.5
    assert calculate_ride(18, 7) == 53.5
