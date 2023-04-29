class BaseRepository:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
        self.table_name = None

    def get_all(self):
        self.cursor.execute(f'select * from {self.table_name}')
        return self.cursor.fetchall()

    def delete_table(self):
        self.cursor.execute(f'drop table {self.table_name};')
