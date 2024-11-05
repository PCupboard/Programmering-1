import settings as sett
from time import sleep

# -------- CHARACTER PARENT CLASS -------- #
class Character:
    def __init__(self, deck) -> None:
        self.deck = deck
        self.character_deck = []
        self.card_rank = 0
        self.card_suit = 0

        self.busted = False

        self.deck_value = 0
        self.deck_length_index = 0

        self.ace_card_count = 0
        self.value_print_check = 0

        self.character_name = "character"

    def hit(self) -> None:
        self.character_deck.append(self.deck.draw())
        self.deck_length_index = len(self.character_deck) - 1

        current_card = self.character_deck[self.deck_length_index]
        self.deck_value = self.deck_value + int(current_card[2])

        if current_card[1] == 'ace':
            self.ace_card_count += 1
        else:
            pass

    def hand_value_check(self) -> bool:
        if self.deck_value > 21:
            if self.ace_card_count >= 1:
                self.value_print_check = 1
                self.deck_value -= 10
                self.ace_card_count -= 1
                print("Changed the value of the ace in your hand from 11 to 1.")
                if self.character_name.lower() in 'the dealer':
                    print(sett.red_color, end='\r')
                else:
                    print(sett.blue_color, end='\r')

                print(f"{self.character_name}'s{sett.reset_color} hand value is now {self.deck_value}")

            else:
                if self.character_name.lower() in 'the dealer':
                    print(f"{self.character_name} has busted!\n\n")
                    return self.busted

                print(f"{self.character_name} has busted! Your wagered chips are now forfeit \n\n")
                self.busted = True
                return self.busted

        if self.value_print_check == 0:
            if self.character_name.lower() in 'the dealer':
                print(sett.red_color, end='\r')
            else:
                print(sett.blue_color, end='\r')

            print(f"{self.character_name}'s{sett.reset_color} hand value is now {self.deck_value}")

        self.value_print_check = 0

    def draw_card_deck(self) -> None:
        self.deck_length_index = len(self.character_deck) - 1

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
                print(" " * 13 * self.deck_length_index, end='')
                for element in row:
                    if element != 0:
                        print(element, end='')
                    else:
                        print(end=' ')
                print()

            self.deck_length_index -= 1
            print(sett.up_line * 10)

        print("\n" * 8)

        if self.character_name.lower() in 'the dealer':
            sleep(1)

    def chips(self) -> None:
        pass


    def kill(self) -> None:
        self.character_deck.clear()
        self.deck_length_index = 0
        self.deck_value = 0
        self.ace_card_count = 0


# -------- PLAYER CHILD CLASS -------- #
class Player(Character):
    def __init__(self, deck, player_name) -> None:
        super().__init__(deck)
        self.character_name = player_name.title()
        self.end_score_print = ""
        self.chips = {
            "white": 20,
            "blue": 20,
            "green": 15,
            "black": 10,
            "pink": 5
        }

    def print_end_score(self, player_number):
        self.end_score_print = (f"Player nr.{player_number} {sett.horizontal_line} {self.character_name} "
                     f"{sett.thick_horizontal_line} final hand value: {self.deck_value}")
        return self.end_score_print

    def calculate_end_result(self, dealer_hand_value):
        if self.deck_value > 21:
            self.end_score_print = self.end_score_print.replace(f"final hand value: {self.deck_value}", f"{sett.red_color}BUSTED{sett.reset_color}"
                                                                                                         "                                        ")

        elif self.deck_value == dealer_hand_value:
            self.end_score_print = self.end_score_print.replace(f"final hand value: {self.deck_value}", f"{sett.yellow_color}TIE{sett.reset_color}"
                                                                                                         "                                        ")

        elif self.deck_value < dealer_hand_value:
            self.end_score_print = self.end_score_print.replace(f"final hand value: {self.deck_value}", f"{sett.magenta_color}LOST{sett.reset_color}"
                                                                                                         "                                      ")

        else:
            self.end_score_print = self.end_score_print.replace(f"final hand value: {self.deck_value}", f"{sett.green_color}WON{sett.reset_color}"
                                                                                                         "                                       ")

        return self.end_score_print


# -------- DEALER CHILD CLASS -------- #
class Dealer(Character):
    def __init__(self, deck) -> None:
        super().__init__(deck)
        self.character_name = "The dealer"

    def first_draw(self):
        print(f"{self.character_name} draws his first card", end='\r')
        sleep(0.5)
        print(f"{self.character_name} draws his first card..", end='\r')
        sleep(0.5)
        print(f"{self.character_name} draws his first card...", end='\r')
        sleep(1)
        print(f"{sett.red_color}{self.character_name}'s{sett.reset_color} first card:            ")

    def dealer_hit_limit(self):
        if self.deck_value >= 17:
            return True

    def dealer_after_game(self):
        print("")
        print(f"{sett.red_color}{self.character_name}'s{sett.reset_color} final hand value is "
              f"{sett.magenta_color}{self.deck_value}{sett.reset_color}\n")