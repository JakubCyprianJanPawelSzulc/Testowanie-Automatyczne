from abc import ABC
from Invoice import Invoice
from InvoiceRepository import InvoiceRepository
from Warehouse import Warehouse


class Shop(ABC):
    def __init__(self, repository=None, warehouse=None):
        self.__invoice_repository = repository
        self.__warehouse = warehouse

    def buy(self, customer, items_list):
        invoice = Invoice(number=self.invoice_repository.get_next_number(), customer=customer, items=items_list)
        self.invoice_repository.add(invoice)
        self.warehouse.remove(items_list)
        return invoice

    def returning_goods(self, invoice, items_list):
        if self.invoice_repository.find_by_number(invoice.number):
            self.invoice_repository.delete(invoice)
            self.warehouse.add(items_list)

            returned_items = []
            for item in invoice.items:
                if item not in items_list:
                    returned_items.append(item)

            new_invoice = Invoice(number=self.invoice_repository.get_next_number(), customer=invoice.customer, items=returned_items)
            self.invoice_repository.add(new_invoice)
            return True
        else:
            return False

    @property
    def invoice_repository(self):
        return self.__invoice_repository

    @property 
    def warehouse(self):     
        return self.__warehouse

invoice_repository = InvoiceRepository()
warehouse = Warehouse()
myShop=Shop(invoice_repository, warehouse)
myShop.warehouse.add(["piwo", "wino","wódka"])
myShop.warehouse.set_price("piwo", 10)
myShop.warehouse.set_price("wino",50)
myShop.warehouse.set_price("wódka", 40)
myShop.warehouse.showStock()
myShop.buy("Jan", ["piwo", "wino"])
myShop.warehouse.showStock()
myShop.returning_goods(Invoice(number=1, customer="Jan", items=["piwo", "wino"]), ["wino"])
print('po oddaniu towaru')
myShop.warehouse.showStock()
