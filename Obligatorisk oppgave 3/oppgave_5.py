"""
Patrick Jemieljanczyk
Oblig 3
Oppgave 5
Leveringsfrist: 18. oktober, 23.59
"""

# Oppgave 5.1 - Dictionaries og Funksjoner
# Deloppgave A
film_01 = {
    'name': 'Inception',
    'year': 2010,
    'rating': 9.7
}

film_02 = {
    'name': 'Inside Out',
    'year': 2015,
    'rating': 8.1
}

film_03 = {
    'name': 'Con Air',
    'year': 1997,
    'rating': 6.9
}


film_list = [
    film_01,
    film_02,
    film_03
]


# Deloppgave B
def add_film(film_list_f, film_name, film_year, film_rating=5.0):
    film_f = {
        'name': film_name,
        'year': film_year,
        'rating': film_rating
    }

    film_list_f.append(film_f)

    return film_list_f


add_film(film_list_f=film_list, film_name='Interstellar', film_year=2014, film_rating=8.7)
add_film(film_list_f=film_list, film_name='Arrival', film_year=2016, film_rating=7.9)
add_film(film_list_f=film_list, film_name='Cloverfield', film_year=2008, film_rating=7.0)

print("Printer ut lagt til filmene fra oppgave 5.1 deloppgave B")
for film in film_list:
    print(film)

print("\n")


# Deloppgave C
add_film(film_list_f=film_list, film_name='Annihilation', film_year=2018)

print("Printer ut default-ratingen til filmene fra oppgave 5.1 deloppgave C")
for film in film_list:
    print(film)

print("\n")

# --------------------------------------------------------------------------------------------

# Oppgave 5.2 - Mer funksjoner
# Utvid forrige oppgave med noen funksjoner og benytt dem i koden din.


# Deloppgave A
print("Printer ut alle filmene med fin utskrift fra Oppgave 5.2 Deloppgave A:")
def print_film_information(film_list_f):
    for film_f in film_list_f:
        print(f"{film_f['name']} - {film_f['year']} har en vurdering på {film_f['rating']}")

    return film_list_f

print_film_information(film_list_f=film_list)
print("\n")


# Deloppgave B
def average_film_rating(film_list_f):
    average = []
    for film_f in film_list_f:
        average.append(film_f['rating'])

    return sum(average) / len(average)

average_rating = average_film_rating(film_list_f=film_list)

print("Oppgave 5.2 Deloppgave B:")
print(f"Gjennomsnits ratingen til alle filmene er: {round(average_rating, 2)}\n\n")


# Deloppgave C
def print_film_by_year(film_list_f, year_number):
    release_year_list = []
    for film_f in film_list_f:
        if year_number <= film_f['year']:
            release_year_list.append(film_f)

    return release_year_list

print("Skriv inn et heltall som skal være årstallet for alle filmene i listen fra og med det årstallet")
while True:
    user_ask_year = input("Årstall her: ")
    if not user_ask_year.isdigit():
        print("Dette er ikke et heltall!")
        continue
    else:
        year_film_list = print_film_by_year(film_list_f=film_list, year_number=int(user_ask_year))
        break

# Bruker en tidligere funksjon for printe ut filmene
print_film_information(year_film_list)
print("\n\n")

# -------------------------------------------------------------------------------------------------------

# Oppgave 5.3 - Skrive/lese til fil
# Utvid forrige oppgave med noen funksjoner og benytt dem i koden din


# Deloppgave A
def create_movie_file(film_list_f, file_name_f):
    film_file = open(f"{file_name_f}" + ".txt", "w")
    for film_f in film_list_f:
        film_file.write(f"{film_f['name']} - {film_f['year']} har en vurdering på {film_f['rating']}\n")
    film_file.close()


user_file_name = input("Legg til et navn for filen som film listen skal printes ut til: ")

create_movie_file(film_list_f=film_list, file_name_f=user_file_name)
print("\n")

# Deloppgave B
def read_move_file(file_name_f):
    film_file = open(f"{file_name_f}" + ".txt", "r")
    print(film_file.read())

read_move_file(file_name_f=user_file_name)
