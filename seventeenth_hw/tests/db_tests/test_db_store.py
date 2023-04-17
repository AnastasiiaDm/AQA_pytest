from twenty_second_hw.db_repo.order_repository import OrderRepository
from twenty_second_hw.db_repo.products_repository import ProductsRepository


def test_create_and_delete_table(create_db_store_connection):
    products_repo = ProductsRepository(create_db_store_connection[0], create_db_store_connection[1])
    order_repo = OrderRepository(create_db_store_connection[0], create_db_store_connection[1])
    try:
        products_repo.create_test_product_table()
        products_repo.insert_into_test_products()
        order_repo.create_test_order_table()
        order_repo.insert_into_test_order()
        products_repo.get_total_profit()
        for total in products_repo.get_total_profit():
            print(total)
    finally:
        products_repo.delete_table()
        order_repo.delete_table()

# def test():
#     products_repo = ProductsRepository()
#     products_repo.get_by_id(1)

