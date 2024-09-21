"""
Patrick Jemieljanczyk
Obligatorisk oppgave 5
Leveringsfrist: 13. september, 23.59
"""

# Erklærer dictionaries som lagrer antall småkaker spist
# Erklærer også en variabel med antall personer
person_1 = {'småkaker spist': 5}
person_2 = {'småkaker spist': 9}
person_3 = {'småkaker spist': 2.5}
person_4 = {'småkaker spist': 21}
person_5 = {'småkaker spist': 0}
antall_personer = 5

# Lagrer gjennomsnittet i en variabel med datatypen int
gjennomsnitt_smaakaker_spist = int(
                                   (
                                    person_1['småkaker spist'] +
                                    person_2['småkaker spist'] +
                                    person_3['småkaker spist'] +
                                    person_4['småkaker spist'] +
                                    person_5['småkaker spist']
                                   )
                                    / antall_personer
                                  )

# Printer ut antall småkaker spist
print(f"Det gjennomsnittlige antallet småkaker spist over en uke er: {gjennomsnitt_smaakaker_spist}")
