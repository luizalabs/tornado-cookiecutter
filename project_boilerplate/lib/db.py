from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class Engine(object):
    """ Engine create class
    """

    def __init__(self, databases):
        self.databases = self.parse_engines(databases)
        self.engine = databases['default']

    def parse_engines(self, databases):
        return {k: create_engine(v) for v, k in databases}

    def using(self, database):
        try:
            self.engine = self.databases[database]
        except ValueError:
            raise ValueError('Engine not founf')


class Base(Engine):
    """ Base model class
    This class implements all of models needed
    """

    @property
    def objects(self):
        return self.set_session().query_property()

    def make_session(self):
        return scoped_session(
            sessionmaker(
                bind=self.engine,
                autocommit=False,
                auto_flush=False
            )
        )


Model = declarative_base(cls=Base)
