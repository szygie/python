gips = 100
malowanie = 30
panele = 50
listwy = 40

questions=("Czy gipsowac sciany? ", "Czy malowac?", "Czy ukladac panele?", "Czy klasc listwy?")

szerokosc = int(input("podaj szerokosc w metrach"))
dlugosc = int(input("podaj dlugosc w metrach"))
wysokosc = int(input("podaj wysokosc w metrach"))

if (szerokosc or dlugosc or wysokosc) < 1:
    print("zyjemy w wymiarach, wszystkie powinny byc wieksze od 0")
    exit(99)

sufit_podloga = szerokosc * dlugosc
sciany_1 = szerokosc * wysokosc * 2  # bo mamy dwie sciany
sciany_2 = dlugosc * wysokosc * 2  # j.w.
obwod = 2 * dlugosc + 2 * szerokosc

amount_gips = gips * (sciany_1 + sciany_2)
amount_malowanie = malowanie * (sciany_1 + sciany_2) + malowanie * sufit_podloga
amount_panele = panele * sufit_podloga
amount_listwy = listwy * obwod

amount_table = []

amount_table.append(amount_gips)
amount_table.append(amount_malowanie)
amount_table.append(amount_panele)
amount_table.append(amount_listwy)


print("za gipsowanie scian: ", amount_gips)
print("za malowanie scian i sufitu: ", amount_malowanie)
print("za polozenie paneli: ", amount_panele)
print("za listwy: ", amount_listwy)

final_amount =0
for question in questions:
    answer = input(question)
    if answer=="Y":
        final_amount += amount_table[(questions.index(question))]

print("TO bedzie: ", final_amount)