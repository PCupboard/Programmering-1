import random

# ---------- DECK CLASS ---------- #
class Deck:
    def __init__(self) -> None:
        self.suits = ['hearts', 'diamonds', 'spades', 'clubs']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'queen', 'king', 'ace']
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