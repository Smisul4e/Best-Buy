# main.py

from store import Store
import products as prod_mod


def start(store: Store):
    while True:
        print("\nWelcome to the Store")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please enter your choice: ")

        if choice == '1':
            print("\nListing all products:")
            active_products = store.get_all_products()
            for product in active_products:
                product.show()

        elif choice == '2':
            total_quantity = store.get_total_quantity()
            print(f"\nTotal amount in store: {total_quantity}")

        elif choice == '3':
            print("\nMake an order:")
            order_list = []
            while True:
                product_name = input("Enter the product name (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break
                quantity = int(input(f"Enter the quantity for {product_name}: "))

                for product in store.products:
                    if product.name == product_name:
                        order_list.append((product, quantity))
                        break
                else:
                    print("Product not found. Please try again.")

            if order_list:
                total_price = store.order(order_list)
                print(f"Order placed successfully! Total cost: {total_price} dollars.")
            else:
                print("No products ordered.")

        elif choice == '4':
            print("Thank you for visiting the store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    # setup initial stock of inventory
    product_list = [
        prod_mod.Product("MacBook Air M2", price=1450, quantity=100),
        prod_mod.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        prod_mod.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
