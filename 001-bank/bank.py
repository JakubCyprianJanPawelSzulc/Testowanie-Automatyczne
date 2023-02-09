import csv
import datetime
import unittest
from exceptions import *

class Bank():
    def __init__(self, nrKonta, imie, nazwisko,plikklienci):
        self.imie=imie
        self.nazwisko=nazwisko
        self.nrKonta=nrKonta
        self.srodki=0
        Bank.zapisdobazy(self,plikklienci)

    def zapisdobazy(self,plikklienci):
        pom=0
        with open(plikklienci, 'r') as f:
            datareader = csv.reader(f)
            for row in datareader:
                if (int(row[0])==int(self.nrKonta)):
                    pom=pom+1
        f.close()
        print(pom)
        if(pom>0):
            print('taki numer konta juz istnieje')
            raise TakiNumerJuzIstniejeException()
        if(pom==0):
            print('dodawanie konta')
            obj=[self.nrKonta,self.imie,self.nazwisko,self.srodki]
            with open(plikklienci, 'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(obj)
                f.close()
        

    def wplata(nr, kwota,plikklienci,pliklog):
        pom=[]
        with open(plikklienci, 'r') as f:
            datareader = csv.reader(f)
            for row in datareader:
                pom.append(row)
        f.close()
        f = open(plikklienci, "w+")
        f.close()
        for i in pom:
            if i[0]==str(nr):
                i[3]=int(i[3])+kwota

        with open(plikklienci, 'a',newline='') as f:
                writer = csv.writer(f)
                for i in pom:
                    writer.writerow(i)
        f.close()
        x=datetime.datetime.now()
        Bank.zapislog([datetime.datetime.timestamp(x),x,nr,'wplata',kwota],pliklog)
        print('pieniazki wplacone')

    def wyplata(nr, kwota,plikklienci,pliklog):
        if(Bank.czywystarczypieniedzy(nr,kwota,plikklienci)==True):
            pom=[]
            with open(plikklienci, 'r') as f:
                datareader = csv.reader(f)
                for row in datareader:
                    pom.append(row)
            f.close()
            f = open(plikklienci, "w+")
            f.close()
            for i in pom:
                if i[0]==str(nr):
                    i[3]=int(i[3])-kwota

            with open(plikklienci, 'a',newline='') as f:
                    writer = csv.writer(f)
                    for i in pom:
                        writer.writerow(i)
            print('pieniazki wyplacone')
            x=datetime.datetime.now()
            Bank.zapislog([datetime.datetime.timestamp(x),x,nr,'wyplata',kwota],pliklog)
        elif(Bank.czywystarczypieniedzy(nr,kwota,plikklienci)==False):
            print('nie ma tyle pieniazkow')
            raise NieWystarczyZebyWyplacicException()

    def przelew(nr, kwota, nrOdbiorcy,plikklienci,pliklog):
        if(Bank.czywystarczypieniedzy(nr,kwota,plikklienci)==True):
            pom=[]
            with open(plikklienci, 'r') as f:
                datareader = csv.reader(f)
                for row in datareader:
                    pom.append(row)
            f.close()
            f = open(plikklienci, "w+")
            f.close()
            for i in pom:
                if i[0]==str(nr):
                    i[3]=int(i[3])-kwota
                if i[0]==str(nrOdbiorcy):
                    i[3]=int(i[3])+kwota

            with open(plikklienci, 'a',newline='') as f:
                    writer = csv.writer(f)
                    for i in pom:
                        writer.writerow(i)
            print('pieniazki przelane')
            x=datetime.datetime.now()
            Bank.zapislog([datetime.datetime.timestamp(x),x,nr,'przelew',kwota, nrOdbiorcy],pliklog)
        elif(Bank.czywystarczypieniedzy(nr,kwota,plikklienci)==False):
            print('nie ma tyle pieniazkow')
            raise NieWystarczyZebyPrzelacException()

    
    def zapislog(tablica,pliklog):
        with open(pliklog, 'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(tablica)
        f.close()
    def historia(nr, poczatek, koniec,pliklog):
        with open(pliklog, 'r') as f:
            datareader = csv.reader(f)
            for row in datareader:
                if(row[2]==str(nr) and float(row[0])>=float(poczatek) and float(row[0])<=float(koniec)):
                    print(row)
                if(len(row)==6):
                    if(row[5]==str(nr) and float(row[0])>=float(poczatek) and float(row[0])<=float(koniec)):
                        print(row)
        f.close()
    def czywystarczypieniedzy(nr,kwota,plikklienci):
        spr=False
        with open(plikklienci, 'r') as f:
            datareader = csv.reader(f)
            for row in datareader:
                if int(row[0])==nr and int(row[3])>=kwota:
                    spr=True
                elif int(row[0])==nr and int(row[3])<kwota:
                    pass
        f.close()
        return spr

plikklienci='klienci.csv'
pliklog='log.csv'


def main():
    print('~~~~~~Witaj w banku~~~~~~\nCo chcesz zrobic?')
    print('|1|-Wplata   |2|-Wyplata    |3|-Przelew      |4|-Nowe konto  |5|-Historia konta  |6|-Wyjscie')
    x=input()
    if(int(x)==1):
        print('Podaj numer konta, a potem kwote ktora chcesz wplacic')
        a=int(input())
        b=int(input())
        if(b<0):
            raise MniejNizZeroException()
        elif(b>=0): Bank.wplata(a,b,plikklienci,pliklog)
    if(int(x)==2):
        print('Podaj numer konta, a potem kwote ktora chcesz wyplacic')
        a=int(input())
        b=int(input())
        if(b<0):
            raise MniejNizZeroException()
        elif(b>=0): Bank.wyplata(a,b,plikklienci,pliklog)
    if(int(x)==3):
        print('Podaj numer konta, a potem kwote ktora chcesz przelac, a pozniej numer odbiorcy')
        a=int(input())
        b=int(input())
        c=int(input())
        if(b<0):
            raise MniejNizZeroException()
        elif(b>=0): Bank.przelew(a,b,c,plikklienci,pliklog)
    if(int(x)==4):
        print('Podaj numer konta, potem imie, a potem nazwisko')
        a=input()
        b=input()
        c=input()
        k0=Bank(a,b,c,plikklienci)
    if(int(x)==5):
        print('Podaj numer konta, poczatek i koniec przedzialu czasu w formacie YYYY/mm/dd HH:MM')
        a=input()
        b=input()
        x=datetime.datetime.strptime(b, "%Y/%m/%d %H:%M").timestamp()
        c=input()
        y=datetime.datetime.strptime(c, "%Y/%m/%d %H:%M").timestamp()
        Bank.historia(a,x,y,pliklog)

if __name__ == '__main__':
    main()