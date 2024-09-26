"""
Patrick Jemieljanczyk
Oblig 2
Oppgave 1
Leveringsfrist: 29. september, 23.59
"""

while True:
    ask_user = input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall.")

    try:
        ask_user = int(ask_user)

    except ValueError:
        print("FEIL!\n")

    else:
        if ask_user == 42:
            print("Det stemmer, meningen med livet er 42!")
            break

        if 30 < ask_user < 50:
            print("Nærme, men feil.")

        else:
            print("FEIL!\n")
