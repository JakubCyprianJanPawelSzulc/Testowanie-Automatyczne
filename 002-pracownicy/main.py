from listaPracownikow import ListaPracownikow


mojaLista = ListaPracownikow()

mojaLista.dodajKilku([1,1,2,2,3],[[1,'Jan', 'Kowalski', 31, 10, ['Kwiatowa', 2, 1, 'Warszawa'],99, 90],[2, 'Adam', 'Nowak', 25, 5, ['Kwiatowa', 1, 2, 'Warszawa'],98,150],[3, 'Adrian', 'Nowak', 30, 10, ['Polna', 2, 1, 'Żalno'],50],[4, 'Mariusz', 'Pudzianowski', 40, 15, ['Kwiatowa', 1, 1, 'Warszawa'],100],[5, 'Paweł', 'Golec', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa 2'],'WYSOKA', 50]])
# mojaLista.wyswietl()
mojaLista.dodaj(3,[6, 'Łukasz', 'Golec', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],'WYSOKA', 100])


# print(mojaLista.wyswietlPosortowanych())

# print('---------------------')

# # print(mojaLista.wyswietl())
# print(mojaLista.wyswietlZMiastem('Warszawa'))

# # print(mojaLista.wyswietlZWartoscia())

# mojaLista.dodaj(1,[10, 'Łukasz', 'Mielewczyk', 30, 10, ['Marszałkowska', 1, 1, 'Warszawa'],99, 100])
# print(mojaLista.wyswietl())

print('---------------------')
# mojaLista.usun(1)