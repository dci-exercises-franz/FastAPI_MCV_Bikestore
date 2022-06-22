from fastapi.testclient import TestClient
from fastapi import HTTPException
from bikestore.main import app
from bikestore import db

# coverage module!!!!
# pip install fastapi pytest requests

class TestController:

    def get_bike(self, id_):
        try:
            return [bike for bike in db.bikes if bike.id_ == id_]
        except KeyError:
            return None


test_controller = TestController()


@app.get('/bikes/{id_}')
def get_bike(id_):
    bike = test_controller.get_bike(id_)
    if bike:
        return bike
    raise HTTPException(status_code=404)


def test_when_requesting_nonexistent_bike_return_404():

    # pytest.fail("Not Implemented!")
    bike = TestClient(app)
    # choose nonexistent ID !!
    # because this would be successful
    # response = client.get('/client/C1')
    response = bike.get('/bikes/b1')

    assert response.status_code == 404


def test_when_requesting_an_existent_bike_return_200():

    bike = TestClient(app)
    response = bike.get('/bikes/agaag')

    assert response.status_code == 200


# test for bike that isn't there
