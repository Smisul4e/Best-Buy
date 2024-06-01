import products
import store

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

best_buy = store.Store(product_list)

best_buy.show_products()

print("\nTotal stock in store:", best_buy.get_total_stock())
try:
    best_buy.buy_product("MacBook Air M2", 5)
    best_buy.buy_product("Windows License", 1)  # Non-stocked product
    best_buy.buy_product("Shipping", 1)         # Limited product within limit
    best_buy.buy_product("Shipping", 2)         # Limited product exceeding limit
except ValueError as e:
    print(e)
