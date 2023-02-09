from pracownicy import PracownikBiurowy, PracownikFizyczny, Handlarz
from adres import Adres
from exceptions import *

class ListaPracownikow:
    def __init__(self):
        self.lista = []
    def unikatowyId(self,id):
        test = True
        for pracownik in self.lista:
            if pracownik.id == id:
                test = False
        return test

    def unikatoweStanowisko(self,idStanowiska):
        test = True
        for pracownik in self.lista:
            if hasattr(pracownik, 'stanowisko'):
                if pracownik.stanowisko == idStanowiska:
                    test = False
        return test

    def dodaj(self, typ, dane):
        if self.unikatowyId(dane[0]) and dane[0]>=1:
            if(len(dane)>8):
                raise ZlaIloscArgumentow()
            elif (typ == 1 and dane[7]>=70 and dane[7]<=150 and self.unikatoweStanowisko(dane[6])==True):
                if(len(dane)==8):
                    pracownik = PracownikBiurowy(dane[0], dane[1], dane[2], dane[3], dane[4], Adres(dane[5][0],dane[5][1],dane[5][2],dane[5][3]), dane[6], dane[7])
                    self.lista.append(pracownik)
                else:
                    raise ZlaIloscArgumentow()
            elif (typ == 2 and dane[6]>=1 and dane[6]<=100):
                if(len(dane)==7):
                    pracownik = PracownikFizyczny(dane[0], dane[1], dane[2], dane[3], dane[4], Adres(dane[5][0],dane[5][1],dane[5][2],dane[5][3]), dane[6])
                    self.lista.append(pracownik)
                else:
                    raise ZlaIloscArgumentow()
            elif (typ == 3 and (dane[6]=='NISKA' or dane[6]=='SREDNIA' or dane[6]=='WYSOKA')):
                if(len(dane)==8):
                    pracownik = Handlarz(dane[0], dane[1], dane[2], dane[3], dane[4], Adres(dane[5][0],dane[5][1],dane[5][2],dane[5][3]), dane[6], dane[7])
                    self.lista.append(pracownik)
                else: 
                    raise ZlaIloscArgumentow()
            else:
                raise NiepoprawneDane()
        else:
            raise NiepoprawneID()

    
    def wyswietl(self):
        wynik=[]
        for pracownik in self.lista:
            wynik.append(pracownik.wyswietlMnie())
        return wynik    
    
    def usun(self, id):
        for pracownik in self.lista:
            if pracownik.id == id:
                self.lista.remove(pracownik)

    def dodajKilku(self,typy, danePracownikow):
        dlugosc = len(typy)
        for i in range(dlugosc):
            self.dodaj(typy[i], danePracownikow[i])
            
            
    def wyswietlPosortowanych(self):
        self.lista.sort(key=lambda pracownik: (-pracownik.doswiadczenie, pracownik.wiek, pracownik.nazwisko))
        return(self.wyswietl())

    def posortujZID(self):
        self.lista.sort(key=lambda pracownik: (pracownik.id))
        return(self.wyswietl())
            
    def wyswietlZMiastem(self, miasto):
        wynik=[]
        for pracownik in self.lista:
            if pracownik.adres.miasto == miasto:
                wynik.append(pracownik.wyswietlMnie())
        return wynik


    def wyswietlZWartoscia(self):
        for pracownik in self.lista:
            print(pracownik.wyswietlMnieZWartoscia())

