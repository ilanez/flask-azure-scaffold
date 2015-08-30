"""
    Scaffold basic tests.
    ~~~~~~~~~~~~
    Tests the REST API
    :author Beni Ben Zikry

"""


import pytest
from src import app


@pytest.fixture
def client(request):

    """
    Initializes a fixture for the client.
    :param request:
    :return:
    """
    app.config['TESTING'] = True
    client = app.test_client()

    # Cleanup after request is finalized. currently not needed.
    def teardown():
        pass
    request.addfinalizer(teardown)
    return client


def test_get_data(client):
    """
    Verifies successful call for get_data
    :param client: The test client to simulate HTTP calls.
    """
    post = client.post('/get_data')
    assert post.status_code == 200
    assert post.content_type == "application/json"

