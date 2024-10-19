"""
Patrick Jemieljanczyk
Oblig 4
Oppgave 1 - Klasser og objekter
Leveringsfrist: 08. november, 23.59
"""

# A))
class Films:
    def __init__(self, film_title: str, film_release_year: int, film_rating: float) -> None:
        self.film_title = film_title
        self.film_release_year = film_release_year
        self.film_rating = film_rating

    def print_film_information(self) -> None:
        print(f"{self.film_title} was released in {self.film_release_year} and currently has a score of {self.film_rating}")


film_obj_1 = Films(film_title="Inception", film_release_year=2010, film_rating=8.8)
film_obj_2 = Films(film_title="The Martian", film_release_year=2015, film_rating=8.0)
film_obj_3 = Films(film_title="Joker", film_release_year=2019, film_rating=8.4)
film_list = [film_obj_1, film_obj_2, film_obj_3]

print("Printer ut filmene for oppgave A")
for film_obj in film_list:
    print(f"{film_obj.film_title} was released in {film_obj.film_release_year} and currently has a score of {film_obj.film_rating}")

print()

# ---------------------------------------------------------------------------------------------------------------- #

# B))
print("Printer ut filmene for oppgave B")
for film_obj in film_list:
    Films.print_film_information(film_obj)
