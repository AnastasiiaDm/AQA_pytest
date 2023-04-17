from seventeenth_hw.utilities.BaseDbRepository import BaseRepository


class ProductsRepository(BaseRepository):
    def __init__(self, connection, cursor):
        super().__init__(connection, cursor)
        self.table_name = 'test_products'

    def create_test_product_table(self):
        self.cursor.execute(
            f'create table {self.table_name}(id int not null AUTO_INCREMENT, name varchar(25) not null, '
            f'price DECIMAL(10,2) null, primary key (id));')
        self.connection.commit()

    def insert_into_test_products(self):
        self.cursor.execute(
            f'insert into {self.table_name} (name, price) values ("iPhone", 1300.99), ("MacBook", 2000), '
            '("AirPods", 200.01), ("Apple Watch", 500), ("iPad", 700);')
        self.connection.commit()

    def get_total_profit(self):
        self.cursor.execute(
            f'select p.name, p.price, o.quantity, format(p.price * o.quantity, 2) as total '
            f'from {self.table_name} as p join test_order as o on p.id = o.product_id;')
        return self.cursor.fetchall()

# from session import session
# from twenty_second_hw.db_repo.products import Products
#
#
# class ProductsRepository:
#     def __init__(self):
#         self.__session = session
#
#     def get_by_id(self, id_value):
#         return self.__session.get(Products, {'id': id_value})
