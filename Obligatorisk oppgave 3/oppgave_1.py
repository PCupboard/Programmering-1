"""
Patrick Jemieljanczyk
Oblig 3
Oppgave 1
Leveringsfrist: 18. oktober, 23.59
"""

student = {
    "first name": "Ola",
    "last name": "Nordmann",
    "favourite course": "Programmering 1",
    }

# 1. Skriver ut studentens fullstendige navn
print(student["first name"], student["last name"])

# 2. Programmatisk endrer studentens favorittkurs til kursets emnekode: "ITF10219 Programmering 1"
student["favourite course"] = "ITF 10219 Programmering 1"

# 3. Programmatisk legg til en alder for studenten i dictionarien. Du kan selv velge hva alderen skal være
student["age"] = 24
print(student["age"])