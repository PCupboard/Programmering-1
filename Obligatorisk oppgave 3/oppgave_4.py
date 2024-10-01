"""
Patrick Jemieljanczyk
Oblig 3
Oppgave 4
Leveringsfrist: 18. oktober, 23.59
"""
import random

def find_volume(length_f, width_f, height_f):
    volume = length_f * width_f * height_f
    return volume


for i in range(3):
    length = random.randrange(1, 21)
    width =  random.randrange(1, 21)
    height = random.randrange(1, 21)

    volume_calculation = find_volume(length, width, height)
    print(f"lengde = {length} \nbredde = {width} \nhøyde = {height} \nVolumet er {volume_calculation}\n")
