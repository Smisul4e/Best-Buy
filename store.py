# store.py

from products import Product, NonStockedProduct, LimitedProduct

class Store:
    def __init__(self, products: list[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_total_stock(self) -> int:
        return sum(product.quantity for product in self.products if product.is_active())

    def buy_product(self, product_name: str, quantity: int):
        for product in self.products:
            if product.name == product_name:
                total_price = product.buy(quantity)
                print(f"Total price for {quantity} {product_name}: ${total_price:.2f}")
                return total_price
        raise ValueError(f"Product {product_name} not found in store")

    def show_products(self):
        for product in self.products:
            product.show()
