from sqlalchemy.orm import scoped_session, sessionmaker, Session

from .engine import Engine

from settings import settings


# Load engines
engine = Engine(settings.DATABASES)
engine.load()


class RoutingSession(Session):
    _name = 'default'

    def get_bind(self, bind=None, clause=None):
        return engine.get_engine(self._name)

    def using(self, bind):
        s = RoutingSession()
        s._name = bind
        return s


# Register session
Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, class_=RoutingSession)
)
session = Session()
