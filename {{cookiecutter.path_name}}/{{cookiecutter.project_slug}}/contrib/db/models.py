from sqlalchemy import Column, Integer
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from settings import settings

from .engine import Engine

from .session import session


class Base(object):

    id = Column(Integer, primary_key=True)


BaseDeclarative = declarative_base(cls=Base)


class Model(BaseDeclarative):
    __abstract__ = True
    __bind__ = 'default'
    metadata = MetaData()

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
        if self.id is None:
            session.add(self)

        if commit:
            session.commit()
            session.flush()

    def delete(self):
        """
        Alias to delete record 
        This method work with a self instance of object 
        and get a ID attribute automatically
        Example:
            palmito = Food.query.get(1)
            palmito.delete()
        """
        session.delete(self)
        session.commit()
        session.flush()

    @classmethod
    def create_all(cls):
        """
        Create all tables based at all engines
        Example:
            Base.create_all()
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
            Base.drop_all()
        """
        engine = Engine(settings.DATABASES)
        engine.load()

        for (name, engine) in engine.engines.items():
            cls.metadata.drop_all(engine)
