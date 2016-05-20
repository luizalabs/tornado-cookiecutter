from sqlalchemy.orm import scoped_session, sessionmaker, Session

from .engine import Engine

from settings import settings


# Load engines
engine = Engine(settings.DATABASES)
engine.load()


class RoutingSession(Session):
    _name = None

    def get_bind(self, mapper=None, clause=None):
        if self._name:
            return engine.get_engine(self._name)
        elif mapper and mapper.class_.__bind__:
            return engine.get_engine(mapper.class_.__bind__)
        else:
            return engine.get_engine('default')

    def using(self, name):
        s = RoutingSession()
        s._name = name
        return s


# Register session
Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, class_=RoutingSession)
)
session = Session()
