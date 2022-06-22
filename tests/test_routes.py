import pytest
from fastapi.testclient import TestClient
from my_app.main import app

# coverage module!!!!

def test_when_requesting_nonexistent_client_return_404():

    # pytest.fail("Not Implemented!")
    client = TestClient(app)
    # choose nonexistent ID !!
    # because this would be successful
    # response = client.get('/client/C1')
    response = client.get('/client/NONEXISTENT_ID')

    assert response.status_code == 404


def test_when_requesting_an_existent_client_return_200():

    client = TestClient(app)
    response = client.get('/client/C1')

    assert response.status_code == 200
