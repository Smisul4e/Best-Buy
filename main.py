import products
import store

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Creating promotions
percentage_discount = products.PercentageDiscount("20% off", 20)
second_item_half_price = products.SecondItemHalfPrice("Second item half price")
buy_two_get_one_free = products.BuyTwoGetOneFree("Buy 2, get 1 free")

# Adding promotions to products
product_list[0].set_promotion(percentage_discount)  # 20% off MacBook Air M2
product_list[1].set_promotion(second_item_half_price)  # Second item at half price for Bose Earbuds
product_list[2].set_promotion(buy_two_get_one_free)  # Buy 2 get 1 free for Google Pixel 7

best_buy = store.Store(product_list)

# Show all products in the store
best_buy.show_products()

# Additional operations to test functionality
print("\nTotal stock in store:", best_buy.get_total_stock())
try:
    best_buy.buy_product("MacBook Air M2", 5)
    best_buy.buy_product("Bose QuietComfort Earbuds", 3)
    best_buy.buy_product("Google Pixel 7", 5)
    best_buy.buy_product("Windows License", 1)  # Non-stocked product
    best_buy.buy_product("Shipping", 1)  # Limited product within limit
    best_buy.buy_product("Shipping", 2)  # Limited product exceeding limit
except ValueError as e:
    print(e)
