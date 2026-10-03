# menu.py

from data import menu


def print_menu():
    print("\n=== FAST FOOD MENU ===")

    for idx, (item, price) in enumerate(menu.items(), start=1):
        print(f"{idx}. {item:<15} ₱{price:.2f}")

    print("======================")


def get_item_by_number(choice):
    items = list(menu.keys())

    if 1 <= choice <= len(items):
        return items[choice - 1]

    return None