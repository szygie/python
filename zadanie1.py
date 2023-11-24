###
### zad 1
###

day_of_week = ("poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela")
day = int(input("w jaki dzien oddales buty?"))
day_of_return = int(input("ile bedzie trwala naprawa w dniach?"))

while day not in range(1, 8):
    day = int(input("Podaj prawidlowy dzien tygodnia od 1 - 7 ..."))

kiedy_zwrot = day_of_return + day

if kiedy_zwrot > 7:
    while (kiedy_zwrot > 7):
        kiedy_zwrot -= 7

day_of_week_string = day_of_week.__getitem__(kiedy_zwrot - 1)

print("Oddalej buty w ", day_of_week.__getitem__(day), ". Zwrot bedzie w", day_of_week_string)
