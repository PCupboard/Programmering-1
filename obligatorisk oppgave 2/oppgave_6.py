"""
Patrick Jemieljanczyk
Oblig 2
Oppgave 6
Leveringsfrist: 29. september, 23.59
"""

import time

user_quit = False
legge_til = ['add', 'ad', 'a']
ta_vekk = ['remove', 'remov', 'remo', 'rem', 're', 'r']
print_liste = ['show list', 'show', 'list', 'sl', 's']
packing_list = []

def add_list(packing_list_a):
    print("Hvilken gjenstand har du lyst å legge til  i pakkelisten?")
    user_add_item = input("")

    for element in packing_list_a:
        if user_add_item == element:
            print("Denne gjenstanden eksisterer allerede i pakkelisten din!")
            return packing_list_a

    else:
        packing_list_a.append(user_add_item)

    return packing_list_a


def remove_list(packing_list_r):
    print("Hvilken gjenstand har du lyst å slette fra pakkelisten?")
    user_remove_item = input("")

    for element in packing_list_r:
        if user_remove_item == element:
         packing_list_r.remove(user_remove_item)

    else:
        print("Denne gjenstanden eksisterer ikke i pakkelisten din!")

    return packing_list_r


print("Dette er et program som hjelper deg med å lage en pakkeliste!\n\n",
      "Du kan skrive følgende kommandoer: \n",
      "    'add'     |  for å legge noe til listen\n",
      "'remove item' |  for å slette noe fra listen\n",
      " 'show list'  |  for å printe ut pakkelisten din\n",
      "   'quit'     |  for å gå ut av programmet og lagre pakkelisten\n"
     )

while True:

    bruker_kommando = input("Skriv en av kommandoene: ").lower()

    match bruker_kommando:
        case bruker_kommando if bruker_kommando in legge_til:
            packing_list = add_list(packing_list)

        case bruker_kommando if bruker_kommando in ta_vekk:
            packing_list = remove_list(packing_list)

        case bruker_kommando if bruker_kommando in print_liste:
            for item in packing_list:
                print(item)
            print()

        case 'q':
            user_quit = True
            print()

        case _:
            print("Gjenkjenner ikke inputen, prøv igjen\n")

    if user_quit:
        with open("pakkeliste.txt", "a") as packing_list_file:
            for item in packing_list:
                packing_list_file.write(f"{item}\n")
        print("Lagret pakkelisten din!\n")
        packing_list_file.close()

        break

print("Avslutter programmet om 4 sekunder")
time.sleep(4)
quit()
