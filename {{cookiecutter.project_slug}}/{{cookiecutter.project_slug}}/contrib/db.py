from restless.exceptions import NotFound

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr

from config.settings import settings


class Engine(object):
    """ Load engines """
    __engine__ = 'default'

    def __init__(self, engines):
        self.base_engines = self.clean_engines(engines)

    def load(self):
        self.engines = {k: self.parse_engine(k, v)
            for (k, v) in self.base_engines.items()}

    def clean_engines(self, engines):
        if 'default' not in engines:
            raise ValueError('Default missing at DATABASES')
        return engines

    def get_engine(self):
        if self.__engine__ in self.base_engines:
            return self.engines[self.__engine__]
        else:
            raise ValueError(
                '{0} engine missing at mapped engines'.format(self.__engine__))

    def parse_engine(self, name, connection_string):
        parse_string = self.parse_connection_string(connection_string)

        if parse_string:
            return create_engine(parse_string)
        else:
            raise ValueError('Connection String not parsed')

    def parse_connection_string(self, data):
        if data['ENGINE'] == 'sqlite':
            return '{ENGINE}:///{NAME}'.format(**data)
        else:
            template = '{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'
            return template.format(**data)


class BaseSession(Session):
    session = sessionmaker()
    engine = Engine(settings['DATABASES'])

    def __init__(self, base):
        self.base = base
        self.load()

    def load(self):
        self.engine.load()

    def make_session(self):
        engine = self.engine.get_engine()
        return sessionmaker(bind=engine)

    def session(self):
        session = self.make_session()
        return session()


class BaseQuery(BaseSession):

    def query(self):
        Session = scoped_session(self.make_session())
        return Session.query_property()


class Base(object):
    """ Base model class
    This class implements all of models needed
    """
    __engine__ = 'default'

    @declared_attr
    def session(cls):
        return BaseSession(cls).session()

    @declared_attr
    def query(cls):
        return BaseQuery(cls).query()

    @classmethod
    def get_or_404(cls, pk):
        obj = cls.query.get(pk)

        if obj:
            return obj
        else:
            raise NotFound()

    def save(self, commit=True):
        session = self.session()
        if not session.id:
            session.add(self)
        if commit:
            session.commit()

    def delete(self):
        session = self.session()
        session.delete(self)
        session.commit()

Model = declarative_base(cls=Base)
