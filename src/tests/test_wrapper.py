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


def test_get_campaign_hourly_stats(client):
    """
    Verifies successful call for acquiring a campaign's hourly statistics.
    :param client: The test client to simulate HTTP calls.
    """
    post = client.post('/get_data', data=dict(campaign_id=6030858694602))
    assert post.status_code == 200
    assert post.content_type == "application/json"

