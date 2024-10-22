import random


class Game:
    def __init__(self):
        pass

# -------- DECK CLASS -------- #
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

        # Etter de tre for-løkkene er ferdig så eksisterer det en list of lists
        # I hvert element i listen ligger det en liste som har 3 elementer i seg
        # 'suit', 'rank', og 'value'
        #  [0]      [1]        [2]      for å hente denne informasjonen
        #
        # EN EXCEPTION. 'ace' kortet har two values som en kan hente ved [2] og [3]
        #                                                                 11  og 1 er valuen
        # Happy drawing ;D

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

# -------- PLAYER CLASS -------- #
class Player:
    def __init__(self, deck) -> None:
        self.deck = deck
        self.player_deck = []

        self.chips = {
                      "white": 20,
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

    def kill_player(self) -> None:
        self.player_deck.clear()

# -------- DEALER CLASS -------- #
class Dealer:
    def __init__(self, deck) -> None:
        self.deck = deck
        self.dealer_deck = []
        self.cards_value = 0
        self.cards_count = -1

    def hit(self) -> None:
        self.dealer_deck.append(self.deck.draw())
        self.cards_count += 1

        current_card = self.dealer_deck[self.cards_count]
        self.cards_value = self.cards_value + int(current_card[2])
        print(f"Dealer's hand value: {self.cards_value}")


    def calculate(self) -> None:
        if self.cards_value >= 21:
            print("Jæværn busta")
        elif self.cards_value >= 17:
            print("Jæværn står")
        else:
            print("Jæværn trekker")

    def kill_dealer(self) -> None:
        self.dealer_deck.clear()
        self.cards_count = 0
        self.cards_value = 0


your_deck = Deck()
your_deck.build()
your_deck.shuffle()
your_deck.debug_show_cards()

dealer = Dealer(your_deck)
dealer.hit()
dealer.calculate()
dealer.hit()
dealer.calculate()
dealer.hit()
dealer.calculate()

#player = Player(your_deck)
#player.hit()
#your_deck.debug_draw_card()
#player.hit()
#your_deck.debug_draw_card()

while True:
    # This is where the MAIN GAME loop will appear
    pass

# Trenger å legge til en 'value' deck for både dealeren og spilleren
# Denne vil lagre alle kortene i hånden til begge klassene og skrive ut verdien av hånden til spilleren og dealeren.
# Viktig er å unngå duplikat av kort, slik at verdien kan bli hentet enkelt og greit
#



