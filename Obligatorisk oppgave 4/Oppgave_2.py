import random


class Dealer:
    def __init__(self) -> None:
        self.suits = ['hearts', 'diamonds', 'spades', 'clubs']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'joker', 'queen', 'king', 'ace']
        self.deck = []


    def build(self) -> None:
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append((suit, rank))

    def shuffle(self) -> None:
        random.shuffle(self.deck)


class Player:
    def __init__(self):
        self.chips = {"white": 20,
                      "red": 20,
                      "blue": 20,
                      "green": 15,
                      "black": 10,
                      "pink": 5
                     }

    def hit(self):
        pass

    def stand(self):
        pass