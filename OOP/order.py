# order.py

class Order:

    def __init__(self):
        self.orders = {}

    def add_order(self, item, quantity):

        if item in self.orders:
            self.orders[item] += quantity
        else:
            self.orders[item] = quantity

    def get_orders(self):
        return self.orders