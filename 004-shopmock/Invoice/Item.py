class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.price = 0
    def __str__(self):
        return "Item: " + self.name + " Price: " + str(self.price) + " Quantity: " + str(self.quantity) 
