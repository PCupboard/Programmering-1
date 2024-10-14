"""
Patrick Jemieljanczyk
Oblig 2
Oppgave 5
Leveringsfrist: 29. september, 23.59
"""

# Gjør oppgave 5, 1. og 2. sammen.

from random import randrange
import time

player_count = 0
max_name_length = 2**6
players_list = []
players_objects = []
score_list = []

color_red = '\u001b[31m'
color_yellow = '\u001b[33m'
color_blue = '\u001b[34m'
reset_color = '\u001b[0m'


class Player:
    def __init__(self,
                 name: str,
                 number: int
                 ) -> None:

        self.score = 0
        self.dart_throws = 1
        self.name = name.title()
        self.number = number

    def throw(self):
        print(f"\n{self.name} kaster dartpilene sine!")
        time.sleep(1)

        while self.dart_throws < 4:
            self.dart_throws += 1
            score = randrange(0, 61)
            self.score += score


        print(f"{self.name} fikk {self.score} poeng!\n")
        time.sleep(1)

        return self.score

print("Skriv inn 'avbryt' for å ikke legge til flere spillere")

while True:
    player_name = input("Legg inn navn til ny spiller: ").lower().strip()

    if player_name == 'avbryt' or player_name == '':
        if player_count < 2:
            print("Du må legge til minst 2 spillere\n")
            continue

        break

    elif player_name.lower() in players_list:
        print("Denne spilleren er allerede lagt inn i spillet!")
        continue

    elif player_name.isalpha():

        if len(player_name) <= max_name_length:
            player_count = player_count + 1
            players_list.append(player_name)
            players_objects.append(Player(player_name, player_count))

        else:
            print("Dette navnet er for langt! Prøv med et annet navn.\n")

    else:
        print("Error, dette kan da ikke være et navn. Prøv igjen.\n")
        continue

# ---------------------------------------------------------------------------

print("\nDeltagere i dartspillet:\n",
      "----------------------------------")

for player in players_objects:
    print(f"Spiller nr.{player.number} -- {player.name}")

print()

while True:
    player_throw_ask = input("Skriv inn nummeret til spilleren som skal kaste først: ")

    try:
        player_throw_int = int(player_throw_ask)

    except ValueError:
        print("Legg inn et tall, prøv igjen\n")
        continue

    else:
        player_throw_int -= 1

        if player_throw_int in range(len(players_objects)):
            score_list.append(players_objects[player_throw_int].throw())

            player_first_throw = players_list.pop(player_throw_int)
            players_list.insert(0, player_first_throw)

            players_objects.pop(player_throw_int)

            for player in players_objects:
                score_list.append(player.throw())
            break

        else:
            print("Ingen spillere har dette nummeret, prøv igjen.\n")
            continue

for score_index in range(len(score_list)):
    if score_list[score_index] == max(score_list):
        for i in range(3):
            print("- ")
            time.sleep(1)

        print(f"{players_list[score_index].title()} vant med {color_red}{score_list[score_index]}{reset_color} poeng!\n")
        time.sleep(1)
        if player_count > 2:
            print(f"{players_list[score_index+1].title()} kom på andre plass med {color_blue}{score_list[score_index+1]}{reset_color} poeng!\n")
            time.sleep(1)
            if player_count > 3:
                print(f"{players_list[score_index+2].title()} kom på tredje plass med {color_yellow}{score_list[score_index+2]}{reset_color} poeng!\n")

print(players_list)
print(score_list)
