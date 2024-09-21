"""
Patrick Jemieljanczyk
Obligatorisk oppgave 3
Leveringsfrist: 13. september, 23.59
"""

# Erklærer variabler
a = True
b = 0

# Fra linje 6 til linje 30 så befinner det seg kode for å tvinge brukeren til å skrive inn et tall
while a:
    bruker_tall0 = str(input("Skriv inn det første tallet: "))

    if bruker_tall0 == 'q':
        quit()

    bruker_tall1 = str(input("Skriv inn det andre tallet: "))

    bruker_tall = [bruker_tall0, bruker_tall1]

    for x in bruker_tall:
        try:
            float(x)
        except ValueError:
            print("Du må skrive inn et tall!\n")
            b = 0
            break

        b += 1

    if b == 2:
        a = False
        bruker_tall_0 = float(bruker_tall[0])
        bruker_tall_1 = float(bruker_tall[1])
        print("-----------------------------------------------")

# Her begynner koden som printer ut de matematiske operasjonene
if bruker_tall_1 == 0:
    print("Du kan ikke dele på 0!\n"
          "Du får ikke noe divisjon eller rest!"
          )
else:
    print(f"Tallene dine dividert: {bruker_tall_0} / {bruker_tall_1} = {round(bruker_tall_0 / bruker_tall_1, 2)}\n"
          f"Tallene får: {bruker_tall_0} % {bruker_tall_1} = {bruker_tall_0 % bruker_tall_1} i rest fra divisjon\n"
          f"Tallene dine rundet ned til nærmeste heltall blir: {bruker_tall_0 // bruker_tall_1}"
          )

print(f"Tallene dine multiplisert blir: {bruker_tall_0} * {bruker_tall_1} = {bruker_tall_0 * bruker_tall_1}   \n"
      f"Tallene dine addert blir: {bruker_tall_0} + {bruker_tall_1} = {bruker_tall_0 + bruker_tall_1}    \n"
      f"Tallene dine subtrahert blir: {bruker_tall_0} - {bruker_tall_1} = {bruker_tall_0 - bruker_tall_1}\n"
      f"Tallene dine opphøyd blir: {bruker_tall_0}^{bruker_tall_1} = {bruker_tall_0 ** bruker_tall_1}    \n"
      )
