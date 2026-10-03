# menu.py

class Menu:

    def __init__(self):
        self.items = {
            "Burger": 50,
            "Fries": 30,
            "Soda": 20,
            "Fried Chicken": 80,
            "Spaghetti": 60,
            "Ice Cream": 25
        }

    def display_menu(self):
        print("\n=== FAST FOOD MENU ===")

        for index, (item, price) in enumerate(self.items.items(), start=1):
            print(f"{index}. {item:<15} ₱{price:.2f}")

        print("======================")

    def get_item_by_number(self, choice):
        item_list = list(self.items.keys())

        if 1 <= choice <= len(item_list):
            return item_list[choice - 1]

        return None