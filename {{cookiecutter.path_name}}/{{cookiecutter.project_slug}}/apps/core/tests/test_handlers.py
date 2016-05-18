import pytest


@pytest.mark.gen_test
def test_root_url(http_client, base_url):
    ' GET / should be return 200 '
    resp = yield http_client.fetch(base_url)
    assert resp.code == 200
    assert resp.body == b'Hello world'


@pytest.mark.gen_test
def test_healthcheck(http_client, base_url):
    ' GET /healthcheck should be return 200 '
    resp = yield http_client.fetch('{}/{}'.format(base_url, 'healthcheck'))
    assert resp.code == 200
    assert 'application/json' in resp.headers['Content-Type']
