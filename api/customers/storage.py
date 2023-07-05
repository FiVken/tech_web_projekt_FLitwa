from functools import lru_cache

from .schema import Customer, Order, Product

CustomerStorageType = dict[int, Customer]
OrdersStorageType = dict[int, Order]
ProductsStorageType = dict[int, Product]

CUSTOMERS: CustomerStorageType = {}

ORDERS: OrdersStorageType = {
    0: Order(customer_id=0, order_items=[0, 1, 2, 3],order_id=0),
    1: Order(customer_id=1, order_items=[24,32,1,8],order_id=1),
    2: Order(customer_id=2, order_items=[8,8,8],order_id=2),
    3: Order(customer_id=3, order_items=[2,22,222,222],order_id=3)
}
PRODUCTS: ProductsStorageType = {
    0: Product(name="Product", price=18.99, description="test", id=0),
    1: Product(name="Product2", price=32.11, description="testtest", id=1),
    2: Product(name="Product3", price=89.00, description="testtesttest", id=2)
}


@lru_cache(maxsize=1)
def get_customers_storage() -> CustomerStorageType:
    return CUSTOMERS


@lru_cache(maxsize=1)
def get_orders_storage() -> OrdersStorageType:
    return ORDERS


@lru_cache(maxsize=1)
def get_products_storage() -> ProductsStorageType:
    return PRODUCTS