import pytest

from mixer.backend.sqlalchemy import mixer

from apps.customers.models import Customer


@pytest.fixture
def customers_mock_data():
    mixer.cycle(4).blend(Customer)


@pytest.mark.gen_test
def test_list(db, customers_mock_data, http_client, base_url):
    resp = yield http_client.fetch('{}/{}'.format(base_url, 'customers'))
    assert resp.code == 200
