import os
import pytest

# set a test config
os.environ.setdefault('TORNADO_SETTINGS_MODULE', 'settings.test')

from app import make_app

from contrib.db import Model


@pytest.fixture
def db(request):
    migrate = Model.create_all()

    def teardown():
        Model.drop_all()

    request.addfinalizer(teardown)
    return migrate


@pytest.fixture
def app():
    return make_app()
