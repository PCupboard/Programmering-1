import os
import random
import time
import settings


class GameInstance:
    def __init__(self):
        self.user_query = 0
        self.game_name = "Blackjack"

        print()
        print("|----------------------|")
        print("<                      >")
        print("|----------------------|")
        time.sleep(1)
        print(f"{settings.up_line + settings.up_line}< Welcome              >", end='\r')
        time.sleep(0.5)
        print("< Welcome To           >", end='\r')
        time.sleep(0.5)
        print(f"< Welcome To {settings.red_color + self.game_name + settings.white_color} \n\n")
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
        self.ranks = ['2', '3', '3', '5', '6', '7', '8', '9', '10', 'joker', 'queen', 'king', 'ace']
        self.deck = []
        self.draw_deck = 0

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
        self.draw_deck = (self.deck[0])
        self.deck.pop(0)

        return self.draw_deck

    def destroy_deck(self) -> None:
        self.deck.clear()

    def debug_show_cards(self) -> None:
        print(self.deck[:4])


# ---------- DRAW CARD CLASS ---------- #
class DrawCard:
    def __init__(self):
        pass


# -------- CHARACTER PARENT CLASS -------- #
class Character:
    def __init__(self, deck) -> None:
        self.deck = deck
        self.character_deck = []
        self.cards_value = 0
        self.cards_count = -1
        self.character_name = "character"

    def hit(self) -> None:
        self.character_deck.append(self.deck.draw())
        self.cards_count += 1

        current_card = self.character_deck[self.cards_count]
        self.cards_value = self.cards_value + int(current_card[2])
        print(f"{self.character_name} hand: {self.character_deck}")
        print(f"{self.character_name} hand value: {self.cards_value}")

    def calculate(self) -> None:
        if self.cards_value >= 21:
            print(f"{self.character_name} busta")
        elif self.cards_value >= 17:
            print(f"{self.character_name} står")
        else:
            print(f"{self.character_name} trekker")

    def kill(self) -> None:
        self.character_deck.clear()
        self.cards_count = 0
        self.cards_value = 0


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


game_instance = GameInstance()
your_deck = Deck()
your_deck.build()
your_deck.shuffle()
player1 = Player(your_deck)
dealer = Dealer(your_deck)

dealer.hit()
dealer.hit()
print()
player1.hit()
player1.hit()

while True:
    # This is where the PRE-GAME loop is stationed
    pass


while True:
    # This is where the MAIN GAME loop is stationed
    pass

