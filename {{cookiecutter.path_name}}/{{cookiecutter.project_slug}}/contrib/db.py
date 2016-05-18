from restless.exceptions import NotFound

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr

from settings import settings


class Engine(object):
    """
    A base engine handler

    :param engines: Dict of engines

    Engine manage the __engine__ of model when have one or more databases
    engines in your models

    Example:

        DATABASES = {
            'default': {
                'ENGINE': 'sqlite,
                'NAME: 'db.sqlite3'
            },
            'other': {
                'ENGINE': 'sqlite,
                'NAME: 'other.sqlite3'
            }
        }

        engine = Engine(DATABASES, 'default')
        engine.base_engines()

        # Load engine to create instance o Engine() 
        engine.load()
        engine.engines

        # By default get_engine() return a default DATABASE engine
        # but your model have a peculiar __engine__ 
        # at instance of model get_engine() return a current engine
        engine.get_engine()
    """

    def __init__(self, engines, current_engine='default'):
        self.base_engines = self.clean_engines(engines)
        self.__engine__ = current_engine

    def load(self):
        """
        Comprehension base_engines and create dict with
        instance of SQLAlchemy Engine

        Example:

            engine.load()
            >>> {'default': Engine('sqlite:///db.sqlite3')} 
        """ 
        self.engines = {k: self.parse_engine(k, v)
                        for (k, v) in self.base_engines.items()}

    def clean_engines(self, engines):
        """
        Validate if have a default engine because it a required

        Example:

            DATABASES = {
                'default': {
                    'ENGINE': 'sqlite,
                    'NAME: 'db.sqlite3'
                }
            }

            engine.clean_engines(DATABASES)
            >>> DATABASES
        """
        if 'default' not in engines:
            raise ValueError('Default missing at DATABASES')
        return engines

    def get_engine(self):
        """
        Return current __engine__ instance

        Example:

            engine.__engine__ = 'default'
            engine.get_engine()
            >>> dict('default')
        """
        if self.__engine__ in self.base_engines:
            return self.engines[self.__engine__]
        else:
            raise ValueError(
                '{0} engine missing at mapped engines'.format(self.__engine__))

    def parse_engine(self, name, connection_string):
        """
        Create a instance of SQLAlchemy Engine

        :param connection_string: String connections tring

        Example:

            connection_string = 'sqlite:///db.sqlite3'
            engine.parse_engine(connection_string) 
            >>> Engine('sqlite:///sqlite3')
        """
        parse_string = self.parse_connection_string(connection_string)

        if parse_string:
            return create_engine(parse_string, echo=settings.SQL_ECHO)
        else:
           raise ValueError('Connection String not parsed')

    def parse_connection_string(self, data):
        """
        Create a connection string based at ENGINE key
        
        :param data: Dict database config

        Example:

            DATABASE = {
                'ENGINE': 'sqlite',
                'NAME': 'db.sqlite3'
            } 

            engine.parse_connection_string(ENGINE)
            >>> 'sqlite:///db.sqlite3
        """
        if data['ENGINE'] == 'sqlite':
            conn_string = '{ENGINE}:///{NAME}'
        else:
            conn_string = '{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'
        return conn_string.format(**data)


class BaseSession(Session):
    """
    Session handler

    Create a instance of SQLAlchemy Session based at a current model __engine__

    :param base: Base model
    """
    session = sessionmaker()

    def __init__(self, base):
        self.base = base
        self.engine = Engine(settings.DATABASES, base.__engine__)
        self.engine.load()

    def _make_session(self):
        """
        Create a Session based at a current_engine

        Example:

            base = Model
            base_session = BaseSession(base)
            base._make_session()
            >>> session(engine)
        """
        engine = self.engine.get_engine()
        return sessionmaker(bind=engine, autocommit=False, autoflush=False)

    def session(self):
        """
        Return a instance of session

        Example:

            base = BaseModel
            base_session = BaseSession(base)
            base.session()
            >>> Session(engine)
        """
        session = self._make_session()
        return session()


class BaseQuery(BaseSession):
    """
    Base Query Handler provide a instance of query_property session
    """
    def query(self):
        """
        Return a scoped session to execute query

        Example:

            >>> query_property() 
        """
        Session = scoped_session(self._make_session())
        return Session.query_property()


class Base(object):
    """
    Base model class

    This class implements all of models needed
    """
    __engine__ = 'default'

    def session(cls):
        return BaseSession(cls).session()

    @declared_attr
    def query(cls):
        """
        Retun a scoped session query_property

        Example:

            class Food(Model):
                # attrs
            foods = Food.query.all()
            >>> [<Food>, <Food>]
        """
        return BaseQuery(cls).query()

    @classmethod
    def create_all(cls):
        """
        Create all tables based at all engines

        Example:

            Base.create_all(0
        """
        engine = Engine(settings.DATABASES)
        engine.load()

        for (name, engine) in engine.engines.items():
            cls.metadata.create_all(engine)

    @classmethod
    def drop_all(cls):
        """
        Drop all tables based at all engines

        Example:

            Base.drop_all(0
        """
        engine = Engine(settings.DATABASES)
        engine.load()

        for (name, engine) in engine.engines.items():
            cls.metadata.drop_all(engine)

    @classmethod
    def get_or_404(cls, pk):
        """
        Get a object or raise a 404 exception

        :param pk: ID of record

        Example:

            food = Food.get_or_404(1)
            food.name
            >>> Palmito 
            food.price
            >>> 10.9
        """
        obj = cls.query.get(pk)

        if obj:
            return obj
        else:
            raise NotFound()

    def save(self, commit=True):
        """
        Alias to save or update object

        :param commit: Boolean to commit or only add object at session

        Usage example:

            class Food(Model):
                id = Column(Integer, primary_key=True)
                name = Column(String(60))
                price = Column(Float(precision=2))

            palmito = Food(name='Palmito', price=10.9)
            palmito.save()
            palmito.id
            >>> 1
        """
        session = self.session()

        if not self.id:
            session.add(self)

        if commit:
            session.commit()
            session.close()

        return self

    def delete(self):
        """
        Alias to delete record 

        This method work with a self instance of object 
        and get a ID attribute automatically

        Example:

            palmito = Food.query.get(1)
            palmito.delete()
        """
        session = self.session()
        session.delete(self)
        session.commit()
        session.flush()

Model = declarative_base(cls=Base)
