"""
Patrick Jemieljanczyk
Obligatorisk oppgave 4
Leveringsfrist: 13. september, 23.59
"""

# Erklærer variabler
a = 6
b = 3
c = 2

start_underline = "\033[4m"
end_underline = "\033[0m"

# Printer ut variablene som ble erklært i de første tre linjene
print(f"Følgende variabler har blitt erklært:\n"
      f"| a = {a} | "
      f"b = {b} |   "
      f"c = {c} | \n"
      ">--------------------------------------<"
      )

# Printer ut fire matematiske operasjoner med strek under svaret
print(f"Oppgave a)\n"
      f"a + b * c = {a} + {b} * {c} = {start_underline}{a + b * c}{end_underline}     \n\n"
    
      f"Oppgave b)\n"
      f"(a + b) * c = ({a} + {b}) * {c} = {start_underline}{(a + b) * c}{end_underline}\n\n"
      
      f"Oppgave c)\n"
      f"a / b / c = {a} / {b} / {c} = {start_underline}{a / b / c}{end_underline}      \n\n"
      
      f"Oppgave d)\n"
      f"a / (b / c) = {a} / ({b} / {c}) = {start_underline}\033[4m{a / (b / c)}{end_underline}"
      )

