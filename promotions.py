from abc import ABC, abstractmethod


class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, product_price: float, quantity: int) -> float:
        pass


class PercentageDiscount(Promotion):
    def __init__(self, discount_percent: float):
        self.discount_percent = discount_percent

    def apply_promotion(self, product_price: float, quantity: int) -> float:
        discount = product_price * (self.discount_percent / 100)
        return product_price * quantity - discount * quantity


class SecondItemHalfPrice(Promotion):
    def apply_promotion(self, product_price: float, quantity: int) -> float:
        sets_of_two = quantity // 2
        price = (sets_of_two * product_price) + ((quantity % 2) * (product_price / 2))
        return price


class BuyTwoGetOneFree(Promotion):
    def apply_promotion(self, product_price: float, quantity: int) -> float:
        sets_of_three = quantity // 3
        price = (sets_of_three * 2 * product_price) + ((quantity % 3) * product_price)
        return price
