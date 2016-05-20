import datetime

from contrib.db import Model

from sqlalchemy import Column, String, Integer, DateTime


class Customer(Model):
    __tablename__ = 'cliente'

    id = Column('id_cliente', Integer, primary_key=True)
    name = Column('nome_razao_cliente', String(60), nullable=False)
    created_at = Column('dt_cadastro_cliente',
                        DateTime,
                        default=datetime.datetime.now(),
                        nullable=False)
