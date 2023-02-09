import unittest
from bank import *
import csv
import datetime
from exceptions import *

def clear_csv(plik):
    f = open(plik, "w+")
    f.close

class BankTest(unittest.TestCase):

    def test_init(self):
        clear_csv('kliencitest.csv')
        expected_value = [['100000', 'Steffen', 'Moller', '0']]
        k0=Bank('100000', 'Steffen', 'Moller', 'kliencitest.csv')
        with open('kliencitest.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        self.assertEqual(expected_value, data, msg='test inicjalizacji')
        f.close()
        clear_csv('kliencitest.csv')
        
    
    def test_takiesameID(self):
        clear_csv('kliencitest.csv')
        with self.assertRaises(TakiNumerJuzIstniejeException, msg='sprawdzenie czy moga byc takie same id'):
            k1=Bank('100000', 'Steffen', 'Moller', 'kliencitest.csv')
            k2=Bank('100000', 'Marcin', 'Prokop', 'kliencitest.csv')
        clear_csv('kliencitest.csv')
        
    def test_wplata(self):
        clear_csv('kliencitest.csv')
        expected_value = [['100000', 'Steffen', 'Moller', '665']]
        k0=Bank('100000', 'Steffen', 'Moller', 'kliencitest.csv')
        Bank.wplata(100000,665,'kliencitest.csv','logtest.csv')
        with open('kliencitest.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        self.assertEqual(expected_value, data, msg='test wplaty')
        clear_csv('kliencitest.csv')
        clear_csv('logtest.csv')

    def test_zapislog(self):
        clear_csv('logtest.csv')
        expected_value = [['1666005583.792466','2022-10-17 13:19:43.792466','100000','przelew','847', '100001']]
        Bank.zapislog(['1666005583.792466','2022-10-17 13:19:43.792466',100000,'przelew',847, 100001],'logtest.csv')
        with open('logtest.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        self.assertEqual(expected_value, data, msg='test wpisania do log')
        clear_csv('logtest.csv')
    
    def test_wyplata(self):
        clear_csv('kliencitest.csv')
        expected_value = [['100000', 'Steffen', 'Moller', '500']]
        k0=Bank('100000', 'Steffen', 'Moller', 'kliencitest.csv')
        Bank.wplata(100000,550,'kliencitest.csv','logtest.csv')
        Bank.wyplata(100000,50,'kliencitest.csv','logtest.csv')
        with open('kliencitest.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        self.assertEqual(expected_value, data, msg='test wyplaty')
        clear_csv('kliencitest.csv')
        clear_csv('logtest.csv')
    
    def test_wyplata_zamalopieniazkow(self):
        clear_csv('kliencitest.csv')
        clear_csv('logtest.csv')
        with self.assertRaises(NieWystarczyZebyWyplacicException, msg='sprawdzenie czy mozna wyplacic wiecej niz jest'):
            k1=Bank('100000', 'Steffen', 'Moller', 'kliencitest.csv')
            Bank.wplata(100000,100,'kliencitest.csv','logtest.csv')
            Bank.wyplata(100000,200,'kliencitest.csv','logtest.csv')
        clear_csv('kliencitest.csv')
        clear_csv('logtest.csv')
    
    def test_przelew_zamalopieniazkow(self):
        clear_csv('kliencitest.csv')
        clear_csv('logtest.csv')
        with self.assertRaises(NieWystarczyZebyPrzelacException, msg='sprawdzenie czy mozna wyplacic wiecej niz jest'):
            k1=Bank('100000', 'Piesek', 'Leszek', 'kliencitest.csv')
            k1=Bank('200000', 'Koń', 'Rafał', 'kliencitest.csv')
            Bank.wplata(100000,100,'kliencitest.csv','logtest.csv')
            Bank.przelew(100000,200,200000,'kliencitest.csv','logtest.csv')
        clear_csv('kliencitest.csv')
        clear_csv('logtest.csv')

    def test_przelew(self):
        clear_csv('kliencitest.csv')
        expected_value = [['100000', 'Dorota', 'Wellman', '10'],['100001','Marcin','Prokop','10']]
        k0=Bank('100000', 'Dorota', 'Wellman', 'kliencitest.csv')
        k1=Bank('100001','Marcin','Prokop', 'kliencitest.csv')
        Bank.wplata(100000,20,'kliencitest.csv','logtest.csv')
        Bank.przelew(100000,10,100001,'kliencitest.csv','logtest.csv',)
        with open('kliencitest.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        self.assertEqual(expected_value, data, msg='test przelewu')
        clear_csv('kliencitest.csv')
        clear_csv('logtest.csv')

    def test_wplata_log(self):
        clear_csv('logtest.csv')
        expected_value1 = ['100000', 'wplata', '665']
        k0=Bank('100000', 'Steffen', 'Moller', 'kliencitest.csv')
        Bank.wplata(100000,665,'kliencitest.csv','logtest.csv')
        with open('logtest.csv', 'r') as f:
            reader = csv.reader(f)
            uncutdata = list(reader)
            data1=uncutdata[0][2]
            data2=uncutdata[0][3]
            data3=uncutdata[0][4]
            datatable=[data1,data2,data3]
        self.assertEqual(expected_value1, datatable, msg='test wplaty')
        clear_csv('kliencitest.csv')
        clear_csv('logtest.csv')

    def test_wyplata_log(self):
        clear_csv('logtest.csv')
        expected_value1 = ['100000', 'wyplata', '5']
        k0=Bank('100000', 'Steffen', 'Moller', 'kliencitest.csv')
        Bank.wplata(100000,670,'kliencitest.csv','logtest.csv')
        Bank.wyplata(100000,5,'kliencitest.csv','logtest.csv')
        with open('logtest.csv', 'r') as f:
            reader = csv.reader(f)
            uncutdata = list(reader)
            data1=uncutdata[1][2]
            data2=uncutdata[1][3]
            data3=uncutdata[1][4]
            datatable=[data1,data2,data3]
        self.assertEqual(expected_value1, datatable, msg='test wyplaty')
        clear_csv('kliencitest.csv')
        clear_csv('logtest.csv')

    def test_przelew_log(self):
        clear_csv('logtest.csv')
        expected_value1 = ['100000', 'przelew', '10', '100001']
        k0=Bank('100000', 'Dorota', 'Wellman', 'kliencitest.csv')
        k1=Bank('100001','Marcin','Prokop', 'kliencitest.csv')
        Bank.wplata(100000,20,'kliencitest.csv','logtest.csv')
        Bank.przelew(100000,10,100001,'kliencitest.csv','logtest.csv',)
        with open('logtest.csv', 'r') as f:
            reader = csv.reader(f)
            uncutdata = list(reader)
            data1=uncutdata[1][2]
            data2=uncutdata[1][3]
            data3=uncutdata[1][4]
            data4=uncutdata[1][5]
            datatable=[data1,data2,data3,data4]
        self.assertEqual(expected_value1, datatable, msg='test wyplaty')
        clear_csv('kliencitest.csv')
        clear_csv('logtest.csv')

    def test_czywystarczypieniedzy1(self):
        clear_csv('kliencitest.csv')
        k0=Bank('100000', 'Bogdan', 'Italia', 'kliencitest.csv')
        Bank.wplata(100000,50,'kliencitest.csv','logtest.csv')
        self.assertFalse(Bank.czywystarczypieniedzy(100000,60,'kliencitest.csv'))

    def test_czywystarczypieniedzy2(self):
        clear_csv('kliencitest.csv')
        k0=Bank('100000', 'Bogdan', 'Italia', 'kliencitest.csv')
        Bank.wplata(100000,50,'kliencitest.csv','logtest.csv')
        self.assertTrue(Bank.czywystarczypieniedzy(100000,40,'kliencitest.csv'))
    
    

if __name__ == '__main__':
    unittest.main()

