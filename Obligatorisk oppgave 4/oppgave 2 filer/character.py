import settings as sett
from time import sleep
from random import randrange

# -------- CHARACTER PARENT CLASS -------- #
class Character:
    def __init__(self, deck) -> None:
        self.deck = deck
        self.character_deck = []
        self.card_rank = 0
        self.card_suit = 0

        self.busted = False
        self.blackjack = False

        self.deck_value = 0
        self.deck_length_index = 0

        self.chips = 0

        self.ace_card_count = 0

        self.character_name = "character"

    def hit(self) -> None:
        self.character_deck.append(self.deck.draw())
        self.deck_length_index = len(self.character_deck) - 1

        current_card = self.character_deck[self.deck_length_index]
        self.deck_value = self.deck_value + int(current_card[2])

        if current_card[1] == 'ace':
            self.ace_card_count += 1

    def hand_value_check(self) -> bool:
        if self.character_name.lower() != 'the dealer':
            character_name_string = f"{sett.blue_color}{self.character_name}{sett.reset_color}"
        else:
            character_name_string = f"{sett.red_color}{self.character_name}{sett.reset_color}"

        if self.deck_value == 21 and len(self.character_deck) == 2:
            self.blackjack = True
            blackjack_string = f"{sett.green_color}blackjack{sett.reset_color}"

            match randrange(1, 7):
                case 1:
                    print(f"{character_name_string} has been blessed with a {blackjack_string}!")
                case 2:
                    print(f"{character_name_string} has been endowed with a {blackjack_string}!")
                case 3:
                    print(f"{character_name_string} has been sanctified with a {blackjack_string}!")
                case 4:
                    print(f"Comet sighted, fortunately it brought a {blackjack_string} to {character_name_string}!")
                case 5:
                    print(f"A {blackjack_string} has been delievered to {character_name_string}!")
                case 6:
                    print(f"A {blackjack_string} has been shipped to {character_name_string}!")

            return True

        elif self.deck_value > 21:
            if self.ace_card_count >= 1:
                self.deck_value -= 10
                self.ace_card_count -= 1
                print("Changed the value of the ace in your hand from 11 to 1.")

            else:
                self.busted = True
                busted_string = f"{sett.red_color}busted{sett.reset_color}"
                busts_string = busted_string.replace("busted", "busts")

                if self.deck_value >= 29:
                    print(f"{character_name_string} {busted_string} with a hand value"
                          f" of {sett.magenta_color}{self.deck_value}{sett.reset_color}, impressive!")

                else:
                    match randrange(1, 8):
                        case 1:
                            print(f"{character_name_string} lost their wagered chips because of a {busted_string.replace("busted", "bust")}!")
                        case 2:
                            print(f"Comet sighted, unfortunately it {busted_string} {character_name_string}!")
                        case 3:
                            print(f"{character_name_string} lamentably {busts_string}!")
                        case 4:
                            print(f"{character_name_string} woefully {busts_string}!")
                        case 5:
                            print(f"{character_name_string} tragically {busts_string}!")
                        case 6:
                            print(f"{character_name_string} disastrously {busts_string}!")
                        case 7:
                            print(f"'I am a hitter not a quitter' is not always the best mantra to live by,"
                                  f" as {character_name_string} has {busted_string}!")
                return True

        if self.deck_value == 21:
            print(f"{character_name_string} has achieved a hand value of {sett.green_color}21{sett.reset_color}!")
            return True

        print(f"{character_name_string}'s hand value is now {self.deck_value}")


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

    def kill(self) -> bool:
        self.character_deck.clear()
        self.deck_length_index = 0
        self.deck_value = 0
        self.ace_card_count = 0
        self.busted = False
        self.blackjack = False

        if self.chips == 0:
            return True



# -------- PLAYER CHILD CLASS -------- #
class Player(Character):
    def __init__(self, deck, player_name) -> None:
        super().__init__(deck)
        self.character_name = player_name.title()
        self.character_name = f"{sett.blue_color}{self.character_name}{sett.reset_color}"
        self.end_score_print = ""
        self.wagered_chips = 0

    def starting_chips(self) -> None:
        if self.chips == 0:
            self.chips = randrange(100, 201, 5)

    def bet_chips(self) -> None:
        print(f"{self.character_name} currently has {sett.cyan_color}{self.chips}{sett.reset_color} chips!\n"
              f"how many chips would {self.character_name} like to bet?")
        while True:
            self.wagered_chips = input("").strip()
            print(sett.up_line, end='\r')

            try:
                self.wagered_chips = int(self.wagered_chips)

            except ValueError:
                self.wagered_chips = str(self.wagered_chips)
                print("This is not a valid number, try again", end='\r')
                sleep(1.5)
                print("                                     ", end='\r')
                print(sett.up_line, end='\r')
                print(" " * len(self.wagered_chips), end='\r')
                continue

            else:
                if 0 < self.wagered_chips <= self.chips:
                    if self.chips == self.wagered_chips:
                        print(f"{sett.blue_color}{self.character_name}{sett.reset_color} went {sett.red_color}all in!{sett.reset_color}")

                    else:
                        print(f"{self.character_name} has wagered {sett.cyan_color}{self.wagered_chips}{sett.reset_color} chips!")

                    self.chips -= self.wagered_chips
                    sleep(1.5)
                    break

                else:
                    self.wagered_chips = str(self.wagered_chips)
                    print(f"{self.character_name} does not possess this amount of chips, try again", end='\r')
                    sleep(1.5)
                    print("                                                                       ", end='\r')
                    print(sett.up_line, end='\r')
                    print(" " * len(self.wagered_chips), end='\r')
                    continue


    def print_end_score(self, player_number) -> str:
        self.end_score_print = (f"Player nr.{player_number} {sett.horizontal_line} {self.character_name} "
                     f"{sett.thick_horizontal_line} final hand value: {self.deck_value}")
        return self.end_score_print

    def calculate_end_result(self, dealer_hand_value,  dealer_busted_bool, dealer_blackjack_bool) -> str:
        if self.deck_value > 21:
            self.end_score_print = self.end_score_print.replace(f"final hand value: {self.deck_value}", f"{sett.red_color}BUSTED{sett.reset_color} "
                                                                                                        f"| {sett.red_color}-{self.wagered_chips}"
                                                                                                        f"{sett.reset_color} chips            ")
        elif self.deck_value == dealer_hand_value and not self.blackjack and not dealer_blackjack_bool:
            self.chips += self.wagered_chips
            self.end_score_print = self.end_score_print.replace(f"final hand value: {self.deck_value}", f"{sett.yellow_color}TIE{sett.reset_color} "
                                                                                                        f"| {sett.yellow_color}0"
                                                                                                        f"{sett.reset_color} chips            ")
        elif self.deck_value < dealer_hand_value and not dealer_busted_bool or dealer_blackjack_bool:
            self.end_score_print = self.end_score_print.replace(f"final hand value: {self.deck_value}", f"{sett.red_color}LOST{sett.reset_color} "
                                                                                                        f"| {sett.red_color}-{self.wagered_chips}"
                                                                                                        f"{sett.reset_color} chips               ")
        elif self.blackjack:
            self.chips += self.wagered_chips * 3
            self.end_score_print = self.end_score_print.replace(f"final hand value: {self.deck_value}", f"{sett.green_color}BLACKJACK{sett.reset_color}! "
                                                                                                        f"| {sett.green_color}+{self.wagered_chips * 2}"
                                                                                                        f"{sett.reset_color} chips                     ")
        else:
            self.chips += self.wagered_chips * 2
            self.end_score_print = self.end_score_print.replace(f"final hand value: {self.deck_value}", f"{sett.green_color}WON{sett.reset_color} "
                                                                                                        f"| {sett.green_color}+{self.wagered_chips * 2}"
                                                                                                        f"{sett.reset_color} chips                     ")
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

    def dealer_final_print(self):
        pass