import settings as sett

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

    def busted_check(self) -> bool:
        if self.deck_value > 21:
            if self.ace_card_count >= 1:
                self.deck_value -= 10
                self.ace_card_count -= 1
                print("Changed the value of the ace in your hand from 11 to 1.")

            else:
                print("YOU HAVE BUSTED! EMPTY THEM POCKETS!")
                self.busted = True
                return self.busted

    def draw_card_deck(self) -> None:
        self.deck_length = len(self.character_deck) - 1

        for card in self.character_deck[::-1]:
            if card[0] in 'hearts':
                self.card_suit = sett.hearts
            elif card[0] in 'diamonds':
                self.card_suit = sett.diamonds
            elif card[0] in 'clubs':
                self.card_suit = sett.clubs
            else:
                self.card_suit = sett.spades

            if card[1] in 'queen':
                self.card_rank = 'Q'
            elif card[1] in 'king':
                self.card_rank = 'K'
            elif card[1] in 'ace':
                self.card_rank = 'A'
            else:
                self.card_rank = card[1]

            card_map = [
                    [sett.top_left_corner,
                     sett.horizontal_line, sett.horizontal_line, sett.horizontal_line,
                     sett.horizontal_line, sett.horizontal_line, sett.horizontal_line,
                     sett.horizontal_line, sett.horizontal_line, sett.horizontal_line,
                     sett.top_right_corner],

                    [sett.vertical_line, self.card_rank, 0, 0, 0, 0, 0, 0, 0, self.card_rank, sett.vertical_line],
                    [sett.vertical_line, self.card_suit, 0, 0, 0, 0, 0, 0, 0, self.card_suit, sett.vertical_line],
                    [sett.vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, sett.vertical_line],
                    [sett.vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, sett.vertical_line],
                    [sett.vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, sett.vertical_line],
                    [sett.vertical_line, self.card_suit, 0, 0, 0, 0, 0, 0, 0, self.card_suit, sett.vertical_line],
                    [sett.vertical_line, self.card_rank, 0, 0, 0, 0, 0, 0, 0, self.card_rank, sett.vertical_line],

                    [sett.bottom_left_corner,
                     sett.horizontal_line, sett.horizontal_line, sett.horizontal_line,
                     sett.horizontal_line, sett.horizontal_line, sett.horizontal_line,
                     sett.horizontal_line, sett.horizontal_line, sett.horizontal_line,
                     sett.bottom_right_corner],
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
            print(sett.up_line * 10)

        print("\n" * 9)
        print(f"{self.character_name} hand value: {self.deck_value}")

    def kill(self) -> None:
        self.character_deck.clear()
        self.deck_length = 0
        self.deck_value = 0


# -------- PLAYER CHILD CLASS -------- #
class Player(Character):
    def __init__(self, deck, player_name) -> None:
        super().__init__(deck)
        self.character_name = player_name
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