# receipt.py

class Receipt:

    def __init__(self, menu_items):
        self.menu_items = menu_items

    def print_receipt(self, orders):

        print("\n*** RECEIPT ***")
        print("-------------------")

        total = 0

        for item, quantity in orders.items():

            price = self.menu_items[item]
            subtotal = price * quantity

            total += subtotal

            print(
                f"{item:<15} x{quantity:<3} ₱{price:.2f} -> ₱{subtotal:.2f}"
            )

        print("-------------------")

        discount = 0

        if total > 500:
            discount = total * 0.10
            print(f"Discount (10%)       -₱{discount:.2f}")

        net_total = total - discount

        print(f"TOTAL                ₱{net_total:.2f}")
        print("===================")
        print("Thank you for ordering!")