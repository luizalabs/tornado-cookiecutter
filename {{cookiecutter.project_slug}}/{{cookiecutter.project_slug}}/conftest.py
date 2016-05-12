import os
import pytest

from contrib.app import make_app
from contrib.db import Model, Engine

from apps.settings import settings


@pytest.fixture
def app():
    os.environ.setdefault('TORNADO_SETTINGS_MODULE', 'config.settings.test')

    return make_app()


@pytest.fixture
def db():
    pass #    Model.metadata.create_all()
