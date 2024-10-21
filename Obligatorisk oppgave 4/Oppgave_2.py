import random


class Deck:
    def __init__(self) -> None:
        self.suits = ['hearts', 'diamonds', 'spades', 'clubs']
        self.ranks = ['2', '3', '3', '5', '6', '7', '8', '9', '10', 'joker', 'queen', 'king', 'ace']
        self.value = []
        self.deck = []
        self.draw_deck = []

    def build(self) -> list:
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append((suit, rank))

        for card in self.deck:
            print(card)
            if card.isnumeric():
                self.deck.append(card[1])
                print(self.deck)

        print(self.deck)

        return self.deck

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw(self) -> list:
        self.draw_deck.clear()
        self.draw_deck.append(self.deck[0])
        self.deck.pop(0)
        print(self.deck)

        return self.draw_deck

    def destroy_deck(self) -> None:
        self.deck.clear()


class Player:
    def __init__(self, deck) -> None:
        self.deck = deck
        self.player_deck = []

        self.chips = {"white": 20,
                      "red": 20,
                      "blue": 20,
                      "green": 15,
                      "black": 10,
                      "pink": 5
                     }

    def hit(self):
        self.player_deck = self.deck.draw()
        print(self.player_deck)


    def stand(self):
        pass


class Dealer:
    def __init__(self) -> None:
        pass


class DrawCards:
    def __init__(self) -> None:
        pass


your_deck = Deck()
your_deck.build()
your_deck.shuffle()
print(your_deck.deck)
player = Player(your_deck)
player.hit()
player.hit()
