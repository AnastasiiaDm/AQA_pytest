from seventeenth_hw.utilities.BaseDbRepository import BaseRepository


class OrderRepository(BaseRepository):
    def __init__(self, connection, cursor):
        super().__init__(connection, cursor)
        self.table_name = 'test_order'

    def create_test_order_table(self):
        self.cursor.execute(
            f'create table {self.table_name} (id int not null AUTO_INCREMENT, product_id int not null, quantity int not null, primary key (id), foreign key (product_id) references products(id));')
        self.connection.commit()

    def insert_into_test_order(self):
        self.cursor.execute(
            f'insert into {self.table_name} (product_id, quantity) values (1, 100), (5, 2), (2, 500), (4, 70), (3, 200);')
        self.connection.commit()
