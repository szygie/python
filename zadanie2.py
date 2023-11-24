from math import sqrt

bok1 = int(input("podaj pierwszy bok trójkąta"))
bok2 = int(input("podaj drugi bok trójkąta"))
bok3 = int(input("podaj trzeci bok trójkąta"))

if (bok1 + bok2 < bok3 or bok2 + bok3 < bok1 or bok3 + bok1 < bok2):
    print(
        "Z takiego zestawu nie da się ułożyć trójkąta...pamietaj suma dwóch boków trójkąta musi być większa niż długość trzeciego boku.")
    exit(99)
p = (bok1 + bok2 + bok3) / 2

pole_trojkata = sqrt(p*(p - bok1) * (p - bok2) * (p - bok3))

print(f'{pole_trojkata:.2f}')