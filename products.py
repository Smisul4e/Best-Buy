class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None

    def is_active(self) -> bool:
        return self.quantity > 0

    def buy(self, quantity: int) -> float:
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self.price, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity
        return total_price

    def show(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")
        if self.promotion:
            print(f"Promotion: {self.promotion.__class__.__name__}")

    def set_promotion(self, promotion):
        self.promotion = promotion

    def remove_promotion(self):
        self.promotion = None
