# main.py

from menu import print_menu
from order import take_orders
from receipt import print_receipt


def main():

    print_menu()

    choice = input("\nDo you want to order? (y/n): ").lower()

    if choice == "y":
        orders = take_orders()
        print_receipt(orders)
    else:
        print("Goodbye! Come again.")


if __name__ == "__main__":
    main()