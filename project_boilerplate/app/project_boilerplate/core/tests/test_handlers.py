from library.app import make_app
from tornado.testing import AsyncHTTPTestCase, gen_test


@pytest.fixtures
def get_app(self):
       return make_app()

@pytest.mark.gen_test
def test_healthcheck(self):
    ' GET /healthcheck should be return 200 ' 
    resp = self.fetch('/')
    assert resp.code == 200

