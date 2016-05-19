from sqlalchemy import create_engine

from settings import settings


class Engine(object):
    """
    A base Engine handler

    :param engines: dict of engines

    engine manage the __engine__ of model when have one or more databases
    engines in your models

    Example:

        DATABASES = {
            'default': {
                'engine': 'sqlite,
                'name: 'db.sqlite3'
            },
            'other': {
                'engine': 'sqlite,
                'name: 'other.sqlite3'
            }
        }

        engine = Engine(DATABASES, 'default')
        engine.base_engines()

        # load engine to create instance o engine()
        engine.load()
        engine.engines

        # by default get_engine() return a `default` engine
        # but your model have a peculiar __engine__
        # at instance of model get_engine() return a current engine
        engine.get_engine()
    """

    def __init__(self, engines):
        self.base_engines = self.clean_engines(engines)

    def load(self):
        """
        Comprehension base_engines and create a instanc of Engine

        Example:

            DATABASES = {
                'default': {
                    'engine': 'sqlite,
                    'name: 'db.sqlite3'
                }
            }

            engine = Engine(DATABASES)
            engine.load()
            >>> {'default': engine('sqlite:///db.sqlite3')}
        """
        self.engines = {k: self.parse_engine(k, v)
                        for (k, v) in self.base_engines.items()}

    def clean_engines(self, engines):
        """
        Validate if have a default engine because it a required

        Example:

            DATABASES = {
                'default': {
                    'engine': 'sqlite,
                    'name: 'db.sqlite3'
                }
            }

            engine.clean_engines(databases)
            >>> databases
        """
        if 'default' not in engines:
            raise ValueError('Missing `default` engine')

        return engines

    def get_engine(self, engine):
        """
        Return current __engine__ instance

        Example:

            engine.__engine__ = 'default'
            engine.get_engine()
            >>> dict('default')
        """
        if engine in self.base_engines:
            return self.engines[engine]
        else:
            raise ValueError(
                '{0} Engine missing at mapped engines'.format(engine))

    def parse_engine(self, name, connection_string):
        """
        Create a instance of sqlalchemy engine

        :param connection_string: string connections tring

        Example:

            connection_string = 'sqlite:///db.sqlite3'
            engine.parse_engine(connection_string)
            >>> engine('sqlite:///sqlite3')
        """
        parse_string = self.parse_connection_string(connection_string)

        if parse_string:
            return create_engine(parse_string,
                                 logging_name=name,
                                 echo=settings.SQL_ECHO)
        else:
            raise ValueError('Connection string not parsed')

    def parse_connection_string(self, data):
        """
        Create a connection string based at engine key

        :param data: dict database config

        Example:

            DATABASE = {
                'engine': 'sqlite',
                'name': 'db.sqlite3'
            }

            engine.parse_connection_string(engine)
            >>> 'sqlite:///db.sqlite3
        """
        if data['ENGINE'] == 'sqlite':
            conn_string = '{ENGINE}:///{NAME}'
        else:
            conn_string = '{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'
        return conn_string.format(**data)
