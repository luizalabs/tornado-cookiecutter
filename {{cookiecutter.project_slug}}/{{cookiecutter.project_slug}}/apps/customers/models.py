from contrib.db import Model
from sqlalchemy import Column, String, Integer, Date


class Customer(Model):
    __tablename__ = 'cliente'

    id = Column('id_cliente', Integer, primary_key=True)
    name = Column('nome_razao_cliente', String(60))
    created_at = Column('dt_cadastro_cliente', Date)
