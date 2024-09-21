"""
Patrick Jemieljanczyk
Oblig 2
Oppgave 5
Leveringsfrist: 29. september, 23.59
"""

# Gjør oppgave 5, 1. og 2. sammen.

from random import randrange

player_count = 0
max_name_length = 2**6
players_list = []
players_objects = []
score_list = []


class Player:
    def __init__(self,
                 name: str,
                 number: int
                 ) -> None:

        self.score = 0
        self.dart_throws = 3
        self.name = name.title()
        self.number = number

    def throw(self):
        print(f"\n{self.name} kaster dartpilene sine!")

        while self.dart_throws != 0:
            self.dart_throws -= 1
            score = randrange(0, 60)
            self.score += score

        print(f"{self.name} fikk {self.score} poeng!\n")

        return self.score


print("Skriv 'nei' for å ikke legge til flere spillere")

while True:
    player_name = input("Legg inn navn til ny spiller: ").lower()

    if player_name == 'nei':
        if player_count < 2:
            print("Du må legge til minst 2 spillere\n")
            continue

        break

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
            break

        else:
            print("Ingen spillere har dette nummeret, prøv igjen.\n")
            continue

for player in players_objects:
    score_list.append(player.throw())

print(score_list)
print(players_list)
