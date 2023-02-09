import unittest
from unittest.mock import Mock
from InvoiceRepository import InvoiceRepository
from Shop import Shop
from Invoice import Invoice
from Warehouse import Warehouse

class ShopTests(unittest.TestCase):
    def test_while_buy_the_repository_add_should_be_called(self):
        spy_repository = Mock(InvoiceRepository)
        warehouse = Mock(Warehouse)
        shop = Shop(spy_repository, warehouse)
        shop.buy(customer="Jan", items_list=["cukierki", "wafle"])
        spy_repository.add.assert_called_once()

    def test_while_returning_goods_the_repository_returns_false_when_not_find(self):
        stub_repository = Mock(InvoiceRepository)
        warehouse = Mock(Warehouse)
        shop = Shop(stub_repository, warehouse)
        stub_repository.find_by_number.return_value = None
        result = shop.returning_goods(Mock(Invoice), ["cukierki"])
        self.assertEqual(result, False)

    def test_while_returning_goods_the_repository_delete_should_be_called_when_find(self):
        spy_repository = Mock(InvoiceRepository)
        warehouse = Mock(Warehouse)
        shop = Shop(spy_repository, warehouse)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Mock(Invoice, items=["cukierki"]), ["cukierki"])
        spy_repository.delete.assert_called_once()

    def test_while_returning_goods_the_repository_add_should_be_called_when_find(self):
        spy_repository = Mock(InvoiceRepository)
        warehouse = Mock(Warehouse)
        shop = Shop(spy_repository, warehouse)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Mock(Invoice, items=["cukierki"]), ["cukierki"])
        spy_repository.add.assert_called_once()

    def test_stub(self):
        # Tworzymy stub obiektu InvoiceRepository, który będzie symulował zwracanie określonego obiektu z metody find_by_number()
        stub_invoice_repository = Mock(InvoiceRepository)
        stub_invoice_repository.find_by_number.return_value = Invoice(number=1, customer="Jan", items=["cukierki"])
        # Tworzymy fake obiektu Warehouse, który będzie symulował zachowanie obiektu prawdziwego
        fake_warehouse = Mock(Warehouse)
         # Tworzymy obiekt Shop z naszymi fake i stub obiektami
        shop = Shop(stub_invoice_repository, fake_warehouse)
        # Ustawiamy oczekiwanie na wywołanie metody add() z odpowiednim parametrem
        fake_warehouse.add.expect_called_with(["cukierki"])
        # Wywołujemy metodę returning_goods() na obiekcie Shop
        self.assertTrue(shop.returning_goods(Invoice(number=1, customer="Jan", items=["cukierki"]), ["cukierki"]))
        # Sprawdzamy, czy nasze oczekiwania zostały spełnione
        fake_warehouse.add.assert_called_once()

    def test_dummy(self):
        # Tworzymy dummy obiekt typu Invoice, który będzie pełnił rolę zwykłego obiektu, ale nie będzie używany do niczego innego
        dummy_invoice = Mock(Invoice)
        # Tworzymy stub obiektu InvoiceRepository, który będzie zwracał zawsze None
        stub_invoice_repository = Mock(InvoiceRepository)
        stub_invoice_repository.find_by_number.return_value = None
        # Tworzymy obiekt Shop z naszym stub obiektem
        shop = Shop(stub_invoice_repository)
        # Wywołujemy metodę returning_goods() na obiekcie Shop i sprawdzamy, czy daje ona False
        self.assertFalse(shop.returning_goods(dummy_invoice, ["cukierki"]))
        
    def test_spy(self):
        # Tworzymy spy obiektu InvoiceRepository, który będzie zapisywał informację o wywołaniach metody delete()
        spy_invoice_repository = Mock(InvoiceRepository)
        # Tworzymy fake obiektu Warehouse, który będzie symulował zachowanie obiektu prawdziwego
        fake_warehouse = Mock(Warehouse)
        # Tworzymy obiekt Shop z naszymi fake i spy obiektami
        shop = Shop(spy_invoice_repository, fake_warehouse)
        # Wywołujemy metodę returning_goods() na obiekcie Shop
        shop.returning_goods(Invoice(number=1, customer="Jan", items=["cukierki"]), ["cukierki"])
        # Sprawdzamy, ile razy została wywołana metoda delete() na naszym spy obiekcie
        self.assertEqual(spy_invoice_repository.delete.call_count, 1)

if __name__ == "__main__":
    unittest.main()