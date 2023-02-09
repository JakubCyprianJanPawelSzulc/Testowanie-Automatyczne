import unittest
from adres import *
from pracownicy import *
from listaPracownikow import *
from exceptions import *

class TestPracownicy(unittest.TestCase):
    def test_adres(self):
        adres=Adres('Marszałkowska', 1, 1, 'Warszawa')
        with self.subTest():
            self.assertEqual(adres.ulica, 'Marszałkowska')
        with self.subTest():
            self.assertEqual(adres.numerbudynku, 1)
        with self.subTest():
            self.assertEqual(adres.numermieszkania, 1)

    def test_pracownikInit(self):
        pracownik=Pracownik(21, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'])
        with self.subTest():
            self.assertEqual(pracownik.id, 21)
        with self.subTest():
            self.assertEqual(pracownik.imie, 'Adam')
        with self.subTest():
            self.assertEqual(pracownik.nazwisko, 'Małysz')
        with self.subTest():
            self.assertEqual(pracownik.wiek, 30)
        with self.subTest():
            self.assertEqual(pracownik.doswiadczenie, 10)
        with self.subTest():
            self.assertEqual(pracownik.adres, ['Marszałkowska', 1, 1, 'Warszawa'])


    def test_pracownikbiurowyInit(self):
        pracownik=PracownikBiurowy(21, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],99, 100)
        with self.subTest():
            self.assertEqual(pracownik.id, 21)
        with self.subTest():
            self.assertEqual(pracownik.imie, 'Adam')
        with self.subTest():
            self.assertEqual(pracownik.nazwisko, 'Małysz')
        with self.subTest():
            self.assertEqual(pracownik.wiek, 30)
        with self.subTest():
            self.assertEqual(pracownik.doswiadczenie, 10)
        with self.subTest():
            self.assertEqual(pracownik.stanowisko, 99)
        with self.subTest():
            self.assertEqual(pracownik.intelekt, 100)
        with self.subTest():
            self.assertEqual(pracownik.adres, ['Marszałkowska', 1, 1, 'Warszawa'])

    def test_pracownikfizycznyInit(self):
        pracownik=PracownikFizyczny(6, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],100)
        with self.subTest():
            self.assertEqual(pracownik.id, 6)
        with self.subTest():
            self.assertEqual(pracownik.imie, 'Adam')
        with self.subTest():
            self.assertEqual(pracownik.nazwisko, 'Małysz')
        with self.subTest():
            self.assertEqual(pracownik.wiek, 30)
        with self.subTest():
            self.assertEqual(pracownik.doswiadczenie, 10)
        with self.subTest():
            self.assertEqual(pracownik.sila, 100)
        

    def test_handlarzInit(self):
        pracownik=Handlarz(21, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],'WYSOKA', 100)
        with self.subTest():
            self.assertEqual(pracownik.id, 21)
        with self.subTest():
            self.assertEqual(pracownik.imie, 'Adam')
        with self.subTest():
            self.assertEqual(pracownik.nazwisko, 'Małysz')
        with self.subTest():
            self.assertEqual(pracownik.wiek, 30)
        with self.subTest():
            self.assertEqual(pracownik.doswiadczenie, 10)
        with self.subTest():
            self.assertEqual(pracownik.adres, ['Marszałkowska', 1, 1, 'Warszawa'])
        with self.subTest():
            self.assertEqual(pracownik.skutecznosc, 'WYSOKA')
        with self.subTest():
            self.assertEqual(pracownik.prowizja, 100)


    def test_listaPracownikow(self):
        listaTestowa=ListaPracownikow()
        with self.subTest():
            self.assertEqual(listaTestowa.lista, [])

    def test_dodaj(self):
        listaTestowa=ListaPracownikow()
        pracownik=PracownikBiurowy(21, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],99, 100)
        listaTestowa.dodaj(1,[21, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].id, pracownik.id)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].imie, pracownik.imie)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].nazwisko, pracownik.nazwisko)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].wiek, pracownik.wiek)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].doswiadczenie, pracownik.doswiadczenie)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].adres.ulica, pracownik.adres[0])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].adres.numerbudynku, pracownik.adres[1])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].adres.numermieszkania, pracownik.adres[2])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].adres.miasto, pracownik.adres[3])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].stanowisko, pracownik.stanowisko)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].intelekt, pracownik.intelekt)

    def test_usun(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(1,[1, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
        listaTestowa.usun(1)
        self.assertEqual(listaTestowa.lista, [])

    def test_PracownikBiurowyWyswietlMnie(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(1, [6, 'Adam', 'Małysz', 30, 10,['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
        self.assertEqual(listaTestowa.lista[0].wyswietlMnie(), (6, "PB: ", 'Adam', 'Małysz', 'wiek: ', 30, 'd: ', 10, 'adres: ', 'Marszałkowska', 'Warszawa' ,'st: ', 99, 'iq: ', 100))
    
    def test_PracownikBiurowyWyswietlMnieZWartoscia(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(1, [6, 'Adam', 'Małysz', 30, 10,['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
        self.assertEqual(listaTestowa.lista[0].wyswietlMnieZWartoscia(), (6, "PB: ", 'Adam', 'Małysz', 'wiek: ', 30, 'd: ', 10, 'adres: ', 'Marszałkowska', 'Warszawa' ,'st: ', 99, 'iq: ', 100, 'WARTOSC:', 1000))

    def test_PracownikFizycznyWyswietlMnie(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(2, [6, 'Adam', 'Małysz', 30, 10,['Marszałkowska', 1, 1, 'Warszawa'],100])
        self.assertEqual(listaTestowa.lista[0].wyswietlMnie(), (6, "PF: ", 'Adam', 'Małysz', 'wiek: ', 30, 'd: ', 10, 'adres: ', 'Marszałkowska', 'Warszawa' ,'sila: ', 100))

    def test_PracownikFizycznyWyswietlMnieZWartoscia(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(2, [6, 'Adam', 'Małysz', 30, 10,['Marszałkowska', 1, 1, 'Warszawa'],100])
        self.assertEqual(listaTestowa.lista[0].wyswietlMnieZWartoscia(), (6, "PF: ", 'Adam', 'Małysz', 'wiek: ', 30, 'd: ', 10, 'adres: ', 'Marszałkowska', 'Warszawa' ,'sila: ', 100, 'WARTOSC:', 33.333333333333336))
    
    def test_HandlarzWyswietlMnie(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(3, [6, 'Adam', 'Małysz', 30, 10,['Marszałkowska', 1, 1, 'Warszawa'],'WYSOKA', 100])
        self.assertEqual(listaTestowa.lista[0].wyswietlMnie(), (6, "H: ", 'Adam', 'Małysz', 'wiek: ', 30, 'd: ', 10, 'adres: ', 'Marszałkowska', 'Warszawa' ,'skutecznosc: ', 'WYSOKA', 'prowizja: ', 100))

    
    def test_HandlarzWyswietlMnieZWartoscia(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(3, [6, 'Adam', 'Małysz', 30, 10,['Marszałkowska', 1, 1, 'Warszawa'],'WYSOKA', 100])
        self.assertEqual(listaTestowa.lista[0].wyswietlMnieZWartoscia(), (6, "H: ", 'Adam', 'Małysz', 'wiek: ', 30, 'd: ', 10, 'adres: ', 'Marszałkowska', 'Warszawa' ,'skutecznosc: ', 'WYSOKA', 'prowizja: ', 100, 'WARTOSC:', 1200))
    
    def test_dodajKilku(self):
        pracownik1=PracownikBiurowy(1, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],99, 100)
        pracownik2=PracownikFizyczny(2, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],100)
        listaTestowa=ListaPracownikow()
        listaTestowa.dodajKilku([1,2], [[1, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],99, 100], [2, 'Adam', 'Małysz', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'], 100]])
        test=listaTestowa.wyswietl()
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].id, pracownik1.id)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].imie, pracownik1.imie)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].nazwisko, pracownik1.nazwisko)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].wiek, pracownik1.wiek)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].doswiadczenie, pracownik1.doswiadczenie)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].adres.ulica, pracownik1.adres[0])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].adres.numerbudynku, pracownik1.adres[1])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].adres.numermieszkania, pracownik1.adres[2])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].adres.miasto, pracownik1.adres[3])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].stanowisko, pracownik1.stanowisko)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[0].intelekt, pracownik1.intelekt)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[1].id, pracownik2.id)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[1].imie, pracownik2.imie)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[1].nazwisko, pracownik2.nazwisko)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[1].wiek, pracownik2.wiek)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[1].doswiadczenie, pracownik2.doswiadczenie)
        with self.subTest():
            self.assertEqual(listaTestowa.lista[1].adres.ulica, pracownik2.adres[0])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[1].adres.numerbudynku, pracownik2.adres[1])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[1].adres.numermieszkania, pracownik2.adres[2])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[1].adres.miasto, pracownik2.adres[3])
        with self.subTest():
            self.assertEqual(listaTestowa.lista[1].sila, pracownik2.sila)

    def test_wyswietlZMiastem(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(1, [1, 'Piotr', 'Małysz', 30, 10,['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
        listaTestowa.dodaj(2, [2, 'Jan', 'Małysz', 30, 10,['Marszałkowska', 1, 1, 'Warszawa'], 100])
        listaTestowa.dodaj(2, [3, 'Adam', 'Małysz', 30, 10,['Kielnienska', 1, 1, 'Gdańsk'], 100])
        self.assertEqual(listaTestowa.wyswietlZMiastem('Warszawa'), [(1, 'PB: ', 'Piotr', 'Małysz','wiek: ', 30,'d: ', 10,'adres: ', 'Marszałkowska', 'Warszawa','st: ', 99,'iq: ', 100), (2, 'PF: ', 'Jan', 'Małysz','wiek: ', 30,'d: ', 10,'adres: ', 'Marszałkowska', 'Warszawa','sila: ', 100)])

    def test_wyswietlPosortowanych(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(1, [1, 'Piotr', 'Małysz', 35, 11,['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
        listaTestowa.dodaj(2, [2, 'Jan', 'Rodo', 30, 12,['Szkolna', 17, 1, 'Bialystok'], 100])
        listaTestowa.dodaj(2, [3, 'Adam', 'Małysz', 40, 10,['Kielnienska', 1, 1, 'Gdańsk'], 100])
        self.assertEqual(listaTestowa.wyswietlPosortowanych(), [(2, 'PF: ', 'Jan', 'Rodo', 'wiek: ', 30, 'd: ', 12, 'adres: ', 'Szkolna', 'Bialystok', 'sila: ', 100), (1, 'PB: ', 'Piotr', 'Małysz', 'wiek: ', 35, 'd: ', 11, 'adres: ', 'Marszałkowska', 'Warszawa', 'st: ', 99, 'iq: ', 100), (3, 'PF: ', 'Adam', 'Małysz', 'wiek: ', 40, 'd: ', 10, 'adres: ', 'Kielnienska', 'Gdańsk', 'sila: ', 100)]) 

    def test_posortujZID(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(1, [1, 'Piotr', 'Małysz', 35, 11,['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
        listaTestowa.dodaj(2, [2, 'Jan', 'Rodo', 30, 12,['Szkolna', 17, 1, 'Bialystok'], 100])
        listaTestowa.dodaj(2, [3, 'Adam', 'Małysz', 40, 10,['Kielnienska', 1, 1, 'Gdańsk'], 100])
        listaTestowa.wyswietlPosortowanych()
        listaTestowa.posortujZID()
        self.assertEqual(listaTestowa.wyswietl(), [(1, 'PB: ', 'Piotr', 'Małysz', 'wiek: ', 35, 'd: ', 11, 'adres: ', 'Marszałkowska', 'Warszawa', 'st: ', 99, 'iq: ', 100), (2, 'PF: ', 'Jan', 'Rodo', 'wiek: ', 30, 'd: ', 12, 'adres: ', 'Szkolna', 'Bialystok', 'sila: ', 100), (3, 'PF: ', 'Adam', 'Małysz', 'wiek: ', 40, 'd: ', 10, 'adres: ', 'Kielnienska', 'Gdańsk', 'sila: ', 100)])

    def test_unikatoweID(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(1, [1, 'Piotr', 'Małysz', 35, 11,['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
        with self.subTest():
            self.assertEqual(listaTestowa.unikatowyId(1), False)
        with self.subTest():
            self.assertEqual(listaTestowa.unikatowyId(2), True)
    
    def test_unikatoweStanowisko(self):
        listaTestowa=ListaPracownikow()
        listaTestowa.dodaj(1, [1, 'Piotr', 'Małysz', 35, 11,['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
        with self.subTest():
            self.assertEqual(listaTestowa.unikatoweStanowisko(99), False)
        with self.subTest():
            self.assertEqual(listaTestowa.unikatoweStanowisko(98), True)

    def test_niepoprawneDane1(self):
        listaTestowa=ListaPracownikow()
        with self.assertRaises(NiepoprawneDane):
            listaTestowa.dodaj(1, [1, 'Piotr', 'Małysz', 35, 11,['Marszałkowska', 1, 1, 'Warszawa'],99, 1000])
    
    def test_niepoprawneDane2(self):
        listaTestowa=ListaPracownikow()
        with self.assertRaises(NiepoprawneDane):
            listaTestowa.dodaj(2, [1, 'Piotr', 'Małysz', 35, 11,['Marszałkowska', 1, 1, 'Warszawa'],1000])

    def test_niepoprawneID(self):
        listaTestowa=ListaPracownikow()
        with self.assertRaises(NiepoprawneID):
            listaTestowa.dodaj(1, [1, 'Piotr', 'Małysz', 35, 11,['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
            listaTestowa.dodaj(1, [1, 'Piotr', 'Małysz', 35, 11,['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
    def test_zlailoscargumentow(self):
        listaTestowa=ListaPracownikow()
        with self.assertRaises(ZlaIloscArgumentow):
            listaTestowa.dodaj(1, [1, 'Piotr', 'Małysz', 35, 11,['Marszałkowska', 1, 1, 'Warszawa'],99, 100, 420])
    def test_zlailoscargumentow2(self):
        listaTestowa=ListaPracownikow()
        with self.assertRaises(ZlaIloscArgumentow):
            listaTestowa.dodaj(3, [1, 'Piotr', 'Małysz', 35, 11,['Marszałkowska', 1, 1, 'Warszawa'],'WYSOKA'])


if __name__ == '__main__':
    unittest.main()