import os
import time
import settings as sett
import character
import deck


class GameInstance:
    def __init__(self):
        self.user_query = 0
        self.game_name = "Blackjack"

        print()
        print("|----------------------|")
        print("<                      >")
        print("|----------------------|")
        time.sleep(1)
        print(f"{sett.up_line + sett.up_line}< Welcome              >", end='\r')
        time.sleep(0.5)
        print("< Welcome To           >", end='\r')
        time.sleep(0.5)
        print(f"< Welcome To {sett.red_color + self.game_name + sett.white_color} \n\n")
        time.sleep(1)
        print(f"A Program made by Patrick Jemieljanczyk")
        time.sleep(2)
        os.system('cls')

    def introduction(self):
        pass

    def game_start(self):
        pass

    def game_logic(self):
        pass


#game_instance = GameInstance()
your_deck = deck.Deck()
your_deck.build()
your_deck.shuffle()
your_deck.debug_show_cards()

player1 = character.Player(your_deck)

print()

for i in range(6):
    player1.hit()
    busted_bool = player1.busted_check()
    if busted_bool:
        break

player1.draw_card_deck()


while True:
    # This is where the PRE-GAME loop is stationed
    pass


while True:
    # This is where the MAIN GAME loop is stationed
    pass
