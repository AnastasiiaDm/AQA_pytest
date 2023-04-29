from session import session, get_engine
from sqlalchemy import MetaData, Table, select
from sqlalchemy.orm import declarative_base

from twenty_second_hw.db_repo.orders import OrdersTest
from twenty_second_hw.db_repo.products import ProductsTest

Base = declarative_base()


class StoreRepository:
    def __init__(self):
        self.__session = session

    def get_by_key_value(self, table, key, value):
        return self.__session.get(table, {key: value})

    @staticmethod
    def create_table(table):
        table.metadata.create_all(get_engine())

    def insert_one(self, table):
        self.__session.add(table)
        self.__session.commit()

    def get_all_in_table(self, table):

        all_ = self.__session.query(table).all()
        for product in all_:
            print(product)
        self.__session.commit()

    def get_one_by_name(self, table, name):
        return self.__session.query(table).filter_by(name=name).first()

    def delete_one(self, table, key, value):
        row = self.get_by_key_value(table, key, value)
        self.__session.delete(row)
        self.__session.commit()

    def get_total_profit(self):
        query = session.query(ProductsTest, OrdersTest).join(OrdersTest, ProductsTest.id == OrdersTest.product_id).all()
        for p, o in query:
            print(f'name: {p.name}, price: {p.price}, quantity: {o.quantity}, total: {p.price * o.quantity}')
        self.__session.commit()

    # @staticmethod
    def delete_table(self, table):
        metadata = MetaData()
        metadata.reflect(bind=get_engine())
        my_table = Table(table.__tablename__, metadata, autoload=True, autoload_with=get_engine())
        my_table.drop(get_engine())
        self.__session.commit()
#