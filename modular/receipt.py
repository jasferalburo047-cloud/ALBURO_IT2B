# receipt.py

from data import menu


def print_receipt(orders):
    print("\n*** RECEIPT ***")
    print("-------------------")

    total = 0

    for item, qty in orders.items():
        price = menu[item]
        subtotal = price * qty
        total += subtotal

        print(
            f"{item:<15} x{qty:<3} ₱{price:.2f} -> ₱{subtotal:.2f}"
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