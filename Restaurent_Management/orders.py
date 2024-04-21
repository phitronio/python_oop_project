class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            # jodi item ta cart e already thake
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity  # cart e item jodi na thake

    def remove(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self):
        self.items = {}
