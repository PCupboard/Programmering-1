import os
import random
import time
import settings as sett

# Drawing symbols for cards
hearts = '\u2665'
diamonds = '\u2666'
clubs = '\u2663'
spades = '\u2660'
top_left_corner = "\u250C"
top_right_corner = "\u2510"
horizontal_line = "\u2500"
vertical_line = "\u2502"
bottom_left_corner = "\u2514"
bottom_right_corner = "\u2518"

# Misc
up_line = "\033[A"


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


# ---------- DECK CLASS ---------- #
class Deck:
    def __init__(self) -> None:
        self.suits = ['hearts', 'diamonds', 'spades', 'clubs']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'joker', 'queen', 'king', 'ace']
        self.deck = []
        self.draw_card = 0

    def build(self) -> None:
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append([suit, rank])

        for card in self.deck:
            if card[1].isnumeric():
                card.append(card[1])

            elif card[1] == 'ace':
                card.extend([11, 1])

            else:
                card.append(10)

        # Etter de tre for-løkkene er ferdig så eksisterer det en list of lists.
        # I hvert element i listen ligger det en liste som har 3 elementer i seg;
        # 'suit', 'rank', og 'value'
        #  [0]      [1]        [2]      for å hente denne informasjonen
        #
        # EN EXCEPTION. 'ace' kortet har two values som en kan hente ved [2] og [3]
        #                                                                 11  og 1 er valuen
        # Happy gambling ;D

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw(self) -> list:
        self.draw_card = (self.deck[0])
        self.deck.pop(0)

        return self.draw_card

    def destroy_deck(self) -> None:
        self.deck.clear()

    def debug_show_cards(self) -> None:
        print(self.deck[:4])


# -------- CHARACTER PARENT CLASS -------- #
class Character:
    def __init__(self, deck) -> None:
        self.deck = deck
        self.character_deck = []
        self.card_rank = 0
        self.card_suit = 0

        self.busted = False

        self.deck_value = 0
        self.deck_length = 0

        self.ace_card_count = 0

        self.character_name = "character"

    def hit(self) -> None:
        self.character_deck.append(self.deck.draw())
        self.deck_length = len(self.character_deck) - 1

        current_card = self.character_deck[self.deck_length]
        self.deck_value = self.deck_value + int(current_card[2])

        if current_card[1] == 'ace':
            self.ace_card_count += 1
        else:
            pass

        print(f"{self.character_name} hand value: {self.deck_value}")

    def busted_check(self) -> bool:
        if self.deck_value > 21:
            if self.ace_card_count >= 1:
                self.deck_value -= 10
                self.ace_card_count -= 1
                print("Changed the value of the ace in your hand from 11 to 1.")
                print(self.deck_value, "\n")

            else:
                print("YOU HAVE BUSTED! EMPTY THEM POCKETS!")
                self.busted = True
                return self.busted


    def draw_card_deck(self):
        self.deck_length = len(self.character_deck) - 1

        for card in self.character_deck[::-1]:
            if card[0] in 'hearts':
                self.card_suit = hearts
            elif card[0] in 'diamonds':
                self.card_suit = diamonds
            elif card[0] in 'clubs':
                self.card_suit = clubs
            else:
                self.card_suit = spades

            if card[1] in 'joker':
                self.card_rank = 'J'
            elif card[1] in 'queen':
                self.card_rank = 'Q'
            elif card[1] in 'king':
                self.card_rank = 'K'
            elif card[1] in 'ace':
                self.card_rank = 'A'
            else:
                self.card_rank = card[1]

            card_map = [
                    [top_left_corner,
                     horizontal_line, horizontal_line, horizontal_line,
                     horizontal_line, horizontal_line, horizontal_line,
                     horizontal_line, horizontal_line, horizontal_line,
                     top_right_corner],

                    [vertical_line, self.card_rank, 0, 0, 0, 0, 0, 0, 0, self.card_rank, vertical_line],
                    [vertical_line, self.card_suit, 0, 0, 0, 0, 0, 0, 0, self.card_suit, vertical_line],
                    [vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, vertical_line],
                    [vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, vertical_line],
                    [vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, vertical_line],
                    [vertical_line, self.card_suit, 0, 0, 0, 0, 0, 0, 0, self.card_suit, vertical_line],
                    [vertical_line, self.card_rank, 0, 0, 0, 0, 0, 0, 0, self.card_rank, vertical_line],

                    [bottom_left_corner,
                     horizontal_line, horizontal_line, horizontal_line,
                     horizontal_line, horizontal_line, horizontal_line,
                     horizontal_line, horizontal_line, horizontal_line,
                     bottom_right_corner],
                    ]

            if self.card_rank in '10':
                card_map[1].pop(7)
                card_map[1].pop(7)
                card_map[7].pop(7)
                card_map[7].pop(7)

            for row in card_map:
                print(" " * 12 * self.deck_length, end='')
                for element in row:
                    if element != 0:
                        print(element, end='')
                    else:
                        print(end=' ')
                print()

            self.deck_length -= 1
            print(up_line * 10)

        print("\n" * 9)
        print(self.deck_length)

    def kill(self) -> None:
        self.character_deck.clear()
        self.deck_length = 0
        self.deck_value = 0


# -------- PLAYER CHILD CLASS -------- #
class Player(Character):
    def __init__(self, deck) -> None:
        super().__init__(deck)
        self.character_name = "player"
        self.chips = {
            "white": 20,
            "blue": 20,
            "green": 15,
            "black": 10,
            "pink": 5
        }


# -------- DEALER CHILD CLASS -------- #
class Dealer(Character):
    def __init__(self, deck) -> None:
        super().__init__(deck)
        self.character_name = "dealer"


#game_instance = GameInstance()
your_deck = Deck()
your_deck.build()
your_deck.shuffle()
your_deck.debug_show_cards()
player1 = Player(your_deck)

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
