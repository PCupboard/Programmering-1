"""
Patrick Jemieljanczyk
Oblig 2
Oppgave 6
Leveringsfrist: 29. september, 23.59
"""

import time

user_quit = False
add_item = ['add', 'ad', 'a']
remove_item = ['remove item', 'remove' 'remov', 'remo', 'rem', 're', 'r']
show_list = ['show list', 'show', 'list', 'sl', 'show l']
show_commands = ['show commands', 'show command', 'show com', 'show c', 'sc']
quit_program = ['exit program', 'quit program', 'quit', 'exit', 'q']
packing_list = []

def command_list():
    print(
        "Du kan skrive følgende kommandoer: \n",
        "     'add'     |  for å legge noe til listen\n",
        " 'remove item' |  for å slette noe fra listen\n",
        "  'show list'  |  for å printe ut pakkelisten din\n",
        "'show commands'|  for å skrive ut alle kommandoene du kan bruke\n",
        "    'quit'     |  for å gå ut av programmet og lagre pakkelisten\n"
        )

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
        if element == user_remove_item:
         packing_list_r.remove(user_remove_item)
         print(f"Slettet {user_remove_item} fra pakkelisten!")

        else:
            print("Denne gjenstanden eksisterer ikke i pakkelisten din!\n")

    return packing_list_r


print("Dette er et program som hjelper deg med å lage en pakkeliste!\n")

command_list()

while True:

    bruker_kommando = input("\nSkriv en kommando: ").lower()

    match bruker_kommando:
        case bruker_kommando if bruker_kommando in add_item:
            packing_list = add_list(packing_list)

        case bruker_kommando if bruker_kommando in remove_item:
            packing_list = remove_list(packing_list)

        case bruker_kommando if bruker_kommando in show_list:
            print("Printer ut alle gjenstandene i pakkelisten:")
            for item in packing_list:
                print(item)
            print()

        case bruker_kommando if bruker_kommando in show_commands:
            command_list()

        case bruker_kommando if bruker_kommando in quit_program:
            user_quit = True
            print()

        case _:
            print("Gjenkjenner ikke inputen, prøv igjen\n")

    if user_quit:
        with open("pakkeliste.txt", "a") as packing_list_file:
            for item in packing_list:
                packing_list_file.write(f"{item}\n")
        print("Pakkelisten din er lagret i samme mappe som filen du kjører programmet fra!\n")
        packing_list_file.close()

        break

print("Avslutter programmet om 4 sekunder")
time.sleep(4)
quit()
