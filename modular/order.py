# order.py

from menu import get_item_by_number


def take_orders():
    orders = {}

    while True:

        try:
            choice = int(input("Enter item number: "))

            item = get_item_by_number(choice)

            if item is None:
                print("Invalid number. Please choose from the menu.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        try:
            qty = int(input(f"Enter quantity for {item}: "))

            if qty <= 0:
                print("Quantity must be positive.")
                continue

        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        if item in orders:
            orders[item] += qty
        else:
            orders[item] = qty

        another = input("Order another item? (y/n): ").lower()

        if another != "y":
            break

    return orders