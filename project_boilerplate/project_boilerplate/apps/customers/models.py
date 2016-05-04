from library.db import Model
from sqlalchemy import Column, String, Integer


class Customer(Model):
    __tablename__ = 'cliente'

    id = Column('id_cliente', Integer, primary_key=True)
    name = Column('nome_razao_cliente', String(60))

