from sqlalchemy import Column, INTEGER, VARCHAR, DECIMAL
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# class Products(Base):
#     __tablename__ = 'products'
#     id = Column(INTEGER, primary_key=True)
#     name = Column(VARCHAR(25))
#     price = Column(DECIMAL(10, 2))
#
#     def __str__(self):
#         return f'id: {self.id}, name: {self.name}, price: {self.price}'

from session import session, get_engine


class ProductsTest(Base):
    __tablename__ = 'test_products'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(25))
    price = Column(DECIMAL(10, 2))

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, price: {self.price}'



