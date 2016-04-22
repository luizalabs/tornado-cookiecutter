import pytest
import lib.server

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


@pytest.fixture
def app():
    os.environ['TORNADO_SETTING_MODULE'] = 'project_boilerplate.settings.test'
    return lib.server.run()

@pytest.fixture(scope='session')
def connection(request):
    engine = create_engine('sqlite://', echo=True)
    Base.metadata.create_all(engine)
    conn = engine.connect()

    def finnaly():
        conn.close()
        engine.dispose()

    request.addfinalizer(finnaly)
    return conn

@pytest.fixture
def transaction(request, connection):
    transaction = connection.begin()

    def finnaly():
        transaction.rollback()

    request.addfinalizer(finnaly)
    return transaction


@pytest.fixture
def session(request, connection, transaction):
    session = scoped_session(sessionmaker(connection))

    def finnaly():
        session.close()

    request.addfinalizer(finnaly)
    return session
