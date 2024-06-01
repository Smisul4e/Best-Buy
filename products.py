from abc import ABC, abstractmethod

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
        self.promotion = None

    def is_active(self) -> bool:
        return self.quantity > 0

    def buy(self, quantity: int):
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")
        self.quantity -= quantity
        return self.apply_promotion(quantity)

    def apply_promotion(self, quantity: int) -> float:
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def show(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")
        if self.promotion:
            print(f"Promotion: {self.promotion.name}")

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    def set_promotion(self, promotion):
        self.promotion = promotion

    def remove_promotion(self):
        self.promotion = None


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


# Abstract Promotion Class
class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        pass


class PercentageDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity


class SecondItemHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        pairs = quantity // 2
        remainder = quantity % 2
        return (pairs * (product.price * 1.5)) + (remainder * product.price)


class BuyTwoGetOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        sets_of_three = quantity // 3
        remainder = quantity % 3
        return (sets_of_three * 2 * product.price) + (remainder * product.price)
