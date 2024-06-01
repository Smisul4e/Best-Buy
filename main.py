import products
import promotions

# Create promotions
percentage_discount = promotions.PercentageDiscount(20)
second_item_half_price = promotions.SecondItemHalfPrice()
buy_two_get_one_free = promotions.BuyTwoGetOneFree()

# Create products
macbook = products.Product("MacBook Air M2", price=1450, quantity=100)
earbuds = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
pixel = products.Product("Google Pixel 7", price=500, quantity=250)

# Apply promotions to products
macbook.set_promotion(percentage_discount)
earbuds.set_promotion(second_item_half_price)
pixel.set_promotion(buy_two_get_one_free)

# Show products
macbook.show()
earbuds.show()
pixel.show()

# Test buying products
try:
    print("Buying MacBook Air M2 (5 units): Total price =", macbook.buy(5))
    print("Buying Bose QuietComfort Earbuds (3 units): Total price =", earbuds.buy(3))
    print("Buying Google Pixel 7 (5 units): Total price =", pixel.buy(5))
except ValueError as e:
    print(e)
