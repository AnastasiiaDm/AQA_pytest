from sqlalchemy import Column, INTEGER, VARCHAR, DECIMAL
from sqlalchemy.orm import declarative_base
from sqlalchemy.schema import ForeignKey

from twenty_second_hw.db_repo.products import ProductsTest

Base = declarative_base()


class OrdersTest(Base):
    __tablename__ = 'test_orders'
    id = Column(INTEGER, primary_key=True)
    product_id = Column(INTEGER, ForeignKey(ProductsTest.id))
    quantity = Column(INTEGER)

    def __str__(self):
        return f'id: {self.id}, product_id: {self.product_id}, quantity: {self.quantity}'
