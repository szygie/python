import decimal


class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({self.wiek} lat)'

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat')

    def jest_pelnoletnia(self):
        return self.wiek >= 18


class Produkt:
    def __init__(self, nazwa,cena ,ilosc):
        from decimal import Decimal
        self.nazwa = nazwa
        self.cena = Decimal(cena)
        self.ilosc=ilosc



class Sklep:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.cennik = {}
        self.kasa = 0

    def zdefiniuj_produkt(self, produkt):
        # informację o produkcie zapamiętujemy w słowniku "cennik", który został utworzony w init
        self.cennik[produkt.nazwa] = produkt

    def usun_z_asortymentu(self, art):
        if art not in self.cennik:
            print(f'Nieznany produkt: {art}')
        else:
            self.cennik.pop(art)

    def zmien_cene(self, art):
        produkt = art.split(" ")[0]
        cena = art.split(" ")[1]
        if produkt not in self.cennik:
            print(f'Nieznany produkt: {produkt}')
        else:
            self.cennik[produkt].cena = cena

    def pokaz_cennik(self):
        lista = ""
        for i in self.cennik.keys():
            lista = f'{self.cennik[i].nazwa} : {round(self.cennik[i].cena,2)} : {self.cennik[i].ilosc} ---- {lista} '
        return lista

    def sprzedaj(self, produkt, klient, sztuk=1):
        if produkt not in self.cennik:
            print(f'Nieznany produkt: {produkt}')
        elif produkt in {'piwo'} and not klient.jest_pelnoletnia():
            print(f'Osobom niepełnoletnim nie sprzedajemy {produkt}')
        elif self.cennik[produkt].ilosc < sztuk:
            print(f'Niestety nie mamy tyle: {produkt}')
        else:
            koszt = self.cennik[produkt].cena * sztuk
            self.cennik[produkt].ilosc -= sztuk
            print(f'Kliencie {klient.imie}, za swoje zakupy płacisz {koszt}')
            self.kasa += koszt

    def dostawa(self, produkt, ilosc):
        if produkt not in self.cennik:
            print(f'Nieznany produkt: {produkt}')
        else:
            self.cennik[produkt].ilosc += ilosc

    def zapisz_stany(self):
        dump = open("stan.txt", "w")
        for i in self.cennik.keys():
            dump.write(f' {self.cennik[i].nazwa};{self.cennik[i].cena};{self.cennik[i].ilosc} \n')
        dump.close()

    def odczytaj_stany(self):
        self.cennik ={} #dropujemy stare ceny i stany magazynowe
        dump = open("stan.txt", "r")
        for line in dump:
            nazwa = line.split(";")[0]
            cena = line.split(";")[1]
            ilosc = line.split(";")[2]
            self.zdefiniuj_produkt(Produkt(nazwa,cena,ilosc))
        print("Zakończono import danych...")
        dump.close()


ala = Osoba('Ala', 'Kowalska', 30)

zabka = Sklep(nazwa='Żabka')

cola=Produkt('cola', 6.00, 100)
piwo=Produkt('piwo', 10.50, 100)
woda=Produkt('woda', 16.47, 100)
czosnek =Produkt('czosnek', 60.10, 100)

zabka.zdefiniuj_produkt(cola)
zabka.zdefiniuj_produkt(piwo)
zabka.zdefiniuj_produkt(woda)
zabka.zdefiniuj_produkt(czosnek)


print('Produkty dostępne w Żabce:', zabka.pokaz_cennik())




while True:
    print()
    print('Produkty dostępne w Żabce:', zabka.pokaz_cennik())
    operacje = input("Co chcesz zrobić? \n Q - zakończ \n Z - zakupy \n C - zmien cene produktu \n U - usun produkt \n D - dostawa towaru  \n R - odczyt z pliku stanu magazynowego \n W - zapis do pliku stanu magazynowego"  )
    if operacje=="Q":
        exit(0)
    if operacje=="Z":
        art = input("Co kupujesz? Muisz wybrac z listy po spacji ilosc...Wpisz Q by zakończyć")
        if art=="Q":
            continue
        else:
            zabka.sprzedaj(art.split(" ")[0], ala, int(art.split(" ")[1]))
    if operacje=="C":
        art = input("Ktory produkt checesz edytowacm, podaj jego nazwe i nową cene po spacji!  ")
        while not art.__contains__(" "):
            art = input("Ktory produkt checesz edytowacm, podaj jego nazwe i nową cene po spacji!  ")
        zabka.zmien_cene(art)

    if operacje=="U":
        art = input("Ktory produkt chcesz usunac z asortymentu?")
        zabka.usun_z_asortymentu(art)

    if operacje=="D":
        art = input("Dostawa jakiego towaru? Podaj ilość po spacji... ")
        while not art.__contains__(" "):
            art = input("Nie podałeś ilosc po spacji...")
        zabka.dostawa(art.split(" ")[0], int(art.split(" ")[1]))

    if operacje == "R":
        zabka.odczytaj_stany()

    if operacje == "W":
        zabka.zapisz_stany()