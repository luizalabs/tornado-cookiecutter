import pytest

from apps.customers.models import Customer


@pytest.fixture
def customers_mock_data(mixer):
    mixer.cycle(4).blend(Customer)


@pytest.mark.gen_test
def test_customers_list(customers_mock_data, http_client, base_url):
    resp = yield http_client.fetch('{}/{}'.format(base_url, 'customers'))

    assert resp.code == 200


@pytest.mark.gen_test
def test_customers_detail(customers_mock_data, http_client, base_url):
    resp = yield http_client.fetch(
        '{}/{}/{}'.format(base_url, 'customers', 1)
    )

    assert resp.code == 200
