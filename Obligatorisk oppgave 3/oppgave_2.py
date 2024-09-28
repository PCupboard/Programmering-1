"""
Patrick Jemieljanczyk
Oblig 3
Oppgave 2
Leveringsfrist: 18. oktober, 23.59
"""
import random


def print_random_number():
    rand_number = random.randrange(0,101)

    if len(str(rand_number)) == 1:
        # Printer ut en liten bil til tallet
        print("|'¨'|\n" +
              f"| {rand_number} |   vroom\n" +
              "|'¨'|\n"
              )

    elif len(str(rand_number)) == 2:
        # Printer ut en mellom stor bil til tallet
        print("|'¨¨'|\n" +
              f"| {rand_number} |   VROOM\n" +
              "|'--'|\n"
              )

    elif len(str(rand_number)) == 3:
        # Printer ut en stor bil til tallet
        print("|'¨¨¨'|\n" +
              f"| {rand_number} |   VROOM VROOM\n" +
              "|'---'|\n"
              )

for i in range(3):
    print_random_number()

