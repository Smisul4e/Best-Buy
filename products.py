class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price cannot be negative")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

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


class Electronics(Product):
    def __init__(self, name: str, price: float, quantity: int, warranty_years: int):
        super().__init__(name, price, quantity)
        self.warranty_years = warranty_years

    def show(self):
        super().show()
        print(f"Warranty: {self.warranty_years} years")


class Clothing(Product):
    def __init__(self, name: str, price: float, quantity: int, size: str, material: str):
        super().__init__(name, price, quantity)
        self.size = size
        self.material = material

    def show(self):
        super().show()
        print(f"Size: {self.size}, Material: {self.material}")


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def is_active(self) -> bool:
        return True

    def show(self):
        print(f"Non-Stocked Product: {self.name}, Price: {self.price}")


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int):
        if quantity > self.maximum:
            raise ValueError("Cannot buy more than the maximum limit.")
        return super().buy(quantity)

    def show(self):
        super().show()
        print(f"Maximum purchase limit: {self.maximum}")
