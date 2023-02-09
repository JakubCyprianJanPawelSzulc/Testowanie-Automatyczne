from Item import Item
class OutOfStockError(Exception):
    pass

class Warehouse:
    def __init__(self):
        self.items = {}

    def add(self, item_list):
        for item in item_list:
            if item in self.items:
                self.items[item].quantity += 1
            else:
                self.items[item] = Item(item, 1)

    def set_price(self, item, price):
        if item in self.items:
            self.items[item].price = price
        else:
            self.items[item] = Item(item, 0, price)

    def remove(self, items):
        for name in items:
            if name in self.items:
                if self.items[name].quantity == 0:
                    raise OutOfStockError()
                else:
                    self.items[name].quantity -= 1


    
    def showStock(self):
        for item in self.items:
            print(self.items[item])
