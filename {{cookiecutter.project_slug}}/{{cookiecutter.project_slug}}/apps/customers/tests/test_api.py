import pytest

from mixer.backend.sqlalchemy import Mixer

from apps.customers.api import CustomerHandler


# mock data
mixer.cycle(4).blend('apps.customers.models.Customer')


@pytest.mark.gen_test
def test_list(http_client, base_url):
    resp = yield http_client.fetch('{}/{}'.format(base_url, 'customers'))
    assert resp.code == 200
