# main.py

from store import Store
import products as prod_mod


def main():
    product_list = [
        prod_mod.Product("MacBook Air M2", price=1450, quantity=100),
        prod_mod.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        prod_mod.Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)
    active_products = store.get_all_products()
    print(f"Total quantity in store: {store.get_total_quantity()}")

    order_cost = store.order([(active_products[0], 1), (active_products[1], 2)])
    print(f"Order cost: {order_cost} dollars.")


if __name__ == "__main__":
    main()
