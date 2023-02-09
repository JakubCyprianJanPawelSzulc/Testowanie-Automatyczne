from adres import Adres

class Pracownik:
    def __init__(self, id, imie, nazwisko, wiek, doswiadczenie, adres):
        self.id=id
        self.imie=imie
        self.nazwisko=nazwisko
        self.wiek=wiek
        self.doswiadczenie=doswiadczenie
        self.adres=adres

class PracownikBiurowy(Pracownik):
    def __init__(self, id, imie, nazwisko, wiek, doswiadczenie, adres, stanowisko, intelekt):
            super().__init__(id, imie, nazwisko, wiek, doswiadczenie, adres)
            self.stanowisko=stanowisko
            self.intelekt=intelekt
    def wyswietlMnie(self):
        return(self.id, "PB: ", self.imie, self.nazwisko, "wiek: ", self.wiek, "d: ", self.doswiadczenie, "adres: ", self.adres.ulica, self.adres.miasto ,"st: ", self.stanowisko, "iq: ", self.intelekt)
    def wyswietlMnieZWartoscia(self):
        return(self.id, "PB: ", self.imie, self.nazwisko, "wiek: ", self.wiek, "d: ", self.doswiadczenie, "adres: ", self.adres.ulica, self.adres.miasto ,"st: ", self.stanowisko, "iq: ", self.intelekt, 'WARTOSC:', self.doswiadczenie*self.intelekt)

class PracownikFizyczny(Pracownik):
    def __init__(self, id, imie, nazwisko, wiek, doswiadczenie, adres, sila):
            super().__init__(id, imie, nazwisko, wiek, doswiadczenie, adres)
            self.sila=sila
    def wyswietlMnie(self):
        return(self.id, "PF: ", self.imie, self.nazwisko, "wiek: ", self.wiek, "d: ", self.doswiadczenie,"adres: ", self.adres.ulica, self.adres.miasto , "sila: ", self.sila)
    def wyswietlMnieZWartoscia(self):
        return(self.id, "PF: ", self.imie, self.nazwisko, "wiek: ", self.wiek, "d: ", self.doswiadczenie,"adres: ", self.adres.ulica, self.adres.miasto , "sila: ", self.sila, 'WARTOSC:', self.doswiadczenie*self.sila/self.wiek)

class Handlarz(Pracownik):
    def __init__(self, id, imie, nazwisko, wiek, doswiadczenie, adres, skutecznosc, prowizja):
            super().__init__(id, imie, nazwisko, wiek, doswiadczenie, adres)
            self.skutecznosc=skutecznosc
            self.prowizja=prowizja
    def wyswietlMnie(self):
        return(self.id ,"H: ", self.imie, self.nazwisko, "wiek: ", self.wiek, "d: ", self.doswiadczenie, "adres: ", self.adres.ulica, self.adres.miasto , "skutecznosc: ", self.skutecznosc, "prowizja: ", self.prowizja)
    def wyswietlMnieZWartoscia(self):
        if(self.skutecznosc=='NISKA'):
            return(self.id, "H: ", self.imie, self.nazwisko, "wiek: ", self.wiek,"d: ", self.doswiadczenie, "adres: ", self.adres.ulica, self.adres.miasto , "skutecznosc: ", self.skutecznosc, "prowizja: ", self.prowizja, 'WARTOSC:', self.doswiadczenie*60)
        if(self.skutecznosc=='SREDNIA'):
            return(self.id, "H: ", self.imie, self.nazwisko, "wiek: ", self.wiek,"d: ", self.doswiadczenie, "adres: ", self.adres.ulica, self.adres.miasto , "skutecznosc: ", self.skutecznosc, "prowizja: ", self.prowizja, 'WARTOSC:', self.doswiadczenie*90)
        if(self.skutecznosc=='WYSOKA'):
            return(self.id, "H: ", self.imie, self.nazwisko, "wiek: ", self.wiek,"d: ", self.doswiadczenie, "adres: ", self.adres.ulica, self.adres.miasto , "skutecznosc: ", self.skutecznosc, "prowizja: ", self.prowizja, 'WARTOSC:', self.doswiadczenie*120)  







        