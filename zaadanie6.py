from random import randint

treasure_x = randint(1, 10)
treasure_y = randint(1, 10)

player_x = randint(1, 10)
player_y = randint(1, 10)

direction_x_begin = (treasure_x - player_x).__abs__()
direction_y_begin = (treasure_y - player_y).__abs__()

def hint_for_y(y):
    if ((y - treasure_y).__abs__() > direction_y_begin):
        print("Idziesz w złym kierunku Y")
    else:
        print("Idziesz w dobrym kierunku Y")

def hint_for_x(x):
    if ((x - treasure_x).__abs__() > direction_x_begin):
        print("Idziesz w złym kierunku X")
    else:
        print("Idziesz w dobrym kierunku X")


while (not (player_x == treasure_x and player_y == treasure_y)):

    print("Skarb X ", treasure_x, " Y", treasure_y) #debug
    print("Player X ", player_x, " Y", player_y) #debug

    komenda = input("Podaj kierunek ruchu: W S A D")
    if komenda == "W":
        player_y += 1
        hint_for_y(player_y)
    elif komenda == "S":
        player_y += -1
        hint_for_y(player_y)
    elif komenda == "A":
        player_x += -1
        hint_for_x(player_x)
    elif komenda == "D":
        player_x += 1
        hint_for_x(player_x)

    if (player_x > 10 or player_y > 10 or player_x <0 or player_y <0):
        print("Wyszedles poza plansze. Przegrywasz...")
        exit(99)


print("Hurra, trafiłeś na skarb")