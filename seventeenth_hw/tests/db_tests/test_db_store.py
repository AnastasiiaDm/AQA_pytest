# from twenty_second_hw.db_repo.order_repository import OrderRepository
# from twenty_second_hw.db_repo.products_repository import ProductsRepository
#
#
# def test_create_and_delete_table(create_db_store_connection):
#     products_repo = ProductsRepository(create_db_store_connection[0], create_db_store_connection[1])
#     order_repo = OrderRepository(create_db_store_connection[0], create_db_store_connection[1])
#     try:
#         products_repo.create_test_product_table()
#         products_repo.insert_into_test_products()
#         order_repo.create_test_order_table()
#         order_repo.insert_into_test_order()
#         products_repo.get_total_profit()
#         for total in products_repo.get_total_profit():
#             print(total)
#     finally:
#         products_repo.delete_table()
#         order_repo.delete_table()
import time

from twenty_second_hw.db_repo.orders import OrdersTest
from twenty_second_hw.db_repo.store_repository import StoreRepository

from twenty_second_hw.db_repo.products import ProductsTest


def test_create_and_delete_table():
    store_repo = StoreRepository()
    try:
        store_repo.create_table(ProductsTest)
        store_repo.insert_one(ProductsTest(name="iPhone", price=1300.99))
        store_repo.insert_one(ProductsTest(name="MacBook", price=2000))
        store_repo.insert_one(ProductsTest(name="AirPods", price=200.01))
        store_repo.insert_one(ProductsTest(name="Apple Watch", price=500))
        store_repo.insert_one(ProductsTest(name="iPad", price=700))
        print('----------')
        store_repo.get_all_in_table(ProductsTest)
        print('----------')
        # mac = store_repo.get_one_by_name(ProductsTest, "MacBook")
        # print(mac)
        # print('----------')
        # store_repo.delete_one(ProductsTest, 'id', 3)
        # store_repo.get_all_in_table(ProductsTest)
        # print('----------')
        store_repo.create_table(OrdersTest)
        store_repo.insert_one(OrdersTest(product_id=1, quantity=100))
        store_repo.insert_one(OrdersTest(product_id=5, quantity=2))
        store_repo.insert_one(OrdersTest(product_id=2, quantity=500))
        store_repo.insert_one(OrdersTest(product_id=4, quantity=70))
        store_repo.insert_one(OrdersTest(product_id=3, quantity=200))
        store_repo.get_all_in_table(OrdersTest)
        print('----------')
        store_repo.get_total_profit()
    finally:
        store_repo.delete_table(OrdersTest)
        store_repo.delete_table(ProductsTest)



