"""
Patrick Jemieljanczyk
Oblig 2
Oppgave 2
Leveringsfrist: 29. september, 23.59
"""

print("For løkke:")
for oddetall in range(9, 102):
    if oddetall % 2 != 0:
        print(oddetall)

print("\nWhile løkke:")
oddetall = 9
while oddetall <= 101:
    if oddetall % 2 != 0:
        print(oddetall)
    oddetall += 1