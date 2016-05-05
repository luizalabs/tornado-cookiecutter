import pytest

from mixer.backend.sqlalchemy import mixer

from apps.customers.models import Customer


@pytest.mark.gen_test
def test_list(http_client, base_url, db):
    # mock data
    mixer.cycle(4).blend(Customer)

    resp = yield http_client.fetch('{}/{}'.format(base_url, 'customers'))
    assert resp.code == 200
