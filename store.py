# store.py

from products import Product
from typing import List, Tuple


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, new_product: Product):
        self.products.append(new_product)

    def remove_product(self, existing_product: Product):
        self.products.remove(existing_product)

    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0.0
        for shopping_product, quantity in shopping_list:
            if shopping_product in self.products and shopping_product.quantity >= quantity:
                total_price += shopping_product.price * quantity
                shopping_product.buy(quantity)
            else:
                print(f"Not enough {shopping_product.name} in stock or product not found.")
        return total_price


# Testing the Store class
if __name__ == "__main__":
    import products as prod_mod

    product_list = [
        prod_mod.Product("MacBook Air M2", price=1450, quantity=100),
        prod_mod.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        prod_mod.Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)
    active_products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(active_products[0], 1), (active_products[1], 2)]))
