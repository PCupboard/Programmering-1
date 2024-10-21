import random


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

        # Etter de to nesta for-løkkene er ferdig så eksisterer det en list of lists
        # I hvert element i listen ligger det en liste som har 3 elementer i seg
        # 'suit', 'rank', og 'value'
        #  [0]      [1]        [2]      for å hente denne informasjonen
        #
        # EN EXCEPTION. 'ace' kortet har two values som en kan hente ved [2] og [3]

            #print(card)

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw(self) -> list:
        self.draw_deck = (self.deck[0])
        self.deck.pop(0)

        return self.draw_deck

    def destroy_deck(self) -> None:
        self.deck.clear()

    def debug_draw_card(self) -> None:
        print(self.deck[:4])


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

    def hit(self) -> None:
        self.player_deck.append(self.deck.draw())
        print(self.player_deck)


    def stand(self):
        pass


class Dealer:
    def __init__(self) -> None:
        pass



your_deck = Deck()
your_deck.build()
your_deck.shuffle()
your_deck.debug_draw_card()

player = Player(your_deck)
player.hit()
your_deck.debug_draw_card()
player.hit()
your_deck.debug_draw_card()




