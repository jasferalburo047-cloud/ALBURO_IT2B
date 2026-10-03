# main.py

from menu import Menu
from order import Order
from receipt import Receipt


class RestaurantSystem:

    def __init__(self):
        self.menu = Menu()
        self.order = Order()
        self.receipt = Receipt(self.menu.items)

    def run(self):

        self.menu.display_menu()

        choice = input("\nDo you want to order? (y/n): ").lower()

        if choice != "y":
            print("Goodbye! Come again.")
            return

        while True:

            try:
                item_number = int(
                    input("Enter item number: ")
                )

                item = self.menu.get_item_by_number(
                    item_number
                )

                if item is None:
                    print("Invalid item number.")
                    continue

            except ValueError:
                print("Please enter a valid number.")
                continue

            try:
                quantity = int(
                    input(f"Enter quantity for {item}: ")
                )

                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue

            except ValueError:
                print("Please enter a valid quantity.")
                continue

            self.order.add_order(item, quantity)

            another = input(
                "Order another item? (y/n): "
            ).lower()

            if another != "y":
                break

        self.receipt.print_receipt(
            self.order.get_orders()
        )


if __name__ == "__main__":

    system = RestaurantSystem()
    system.run()