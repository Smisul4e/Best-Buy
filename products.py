# products.py

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount > self.quantity:
            return f"Cannot buy {amount} units. Only {self.quantity} units in stock."
        self.quantity -= amount
        return f"Successfully bought {amount} units of {self.name}."

    def is_active(self):
        return self.quantity > 0

    def show(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
