# products.py

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.quantity > 0

    def buy(self, quantity: int):
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")
        self.quantity -= quantity
        return self.quantity

    def show(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def set_quantity(self, quantity: int):
        self.quantity = quantity
