from random import randint


quess_what = randint(0,999)


user_input = int(input("zgadnij liczbe..."))
while user_input!=quess_what:
    if quess_what > user_input:
        user_input = int(input("Twoja liczba byla mniejsza...próbuj dalej"))
    else:
        user_input = int(input("Twoja liczba byla wieksza...próbuj dalej"))
print("W koncu sie udało. Prawidłowa odpowiedz to ", quess_what)