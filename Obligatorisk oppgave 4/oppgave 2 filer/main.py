from os import system
from time import sleep

import character
import deck
import game_instance
import settings as sett

player_object_list = []

def add_new_players():
    while True:
        game_instance_object.new_player()
        if game_instance_object.player_name.strip() in '':
            if len(player_object_list) >= 1:
                break

            else:
                print(f"{sett.magenta_color}You need atleast one player to play Blackjack!{sett.reset_color}\n")
                continue

        elif len(game_instance_object.player_name) > 64:
            print(f"{sett.magenta_color}This name is too long!{sett.reset_color}\n")
            continue

        elif game_instance_object.player_name.isalpha():
            player_object_list.append(character.Player(deck, game_instance_object.player_name))
            print(f"{sett.green_color}Name added to list of participating players{sett.reset_color}\n")
            sleep(0.5)
            continue

        else:
            print(f"{sett.red_color}Name rejected!{sett.reset_color}\n")
            continue

def hit_or_stand() -> None:
    for counting_variable in range(2):
        player.hit()

    player.draw_card_deck()
    sleep(1)

    if player.hand_value_check():
        sleep(2)
        return

    sleep(1)
    print()

    while True:
        print("Choose one of the following:")
        print("1) hit\n"
              "2) stand\n"
              "3) dealer hand value")

        player_choice = input("")
        print(sett.up_line, end='\r')
        if player_choice.lower() in ["1", "hit"]:
            player.hit()
            system('cls')
            sleep(0.5)
            print()
            player.draw_card_deck()
            sleep(1)
            if player.hand_value_check():
                sleep(1.5)
                print("\nPress enter to continue...")
                input()
                break
            else:
                sleep(1)
                print()

        elif player_choice.lower() in ["2", "stand"]:
            print("You stand")
            break

        elif player_choice.lower() in ["3", "dealer hand value"]:
            print(f"The {sett.red_color}{dealer.character_name}{sett.reset_color}'s hand possesses "
                  f"{sett.red_color + dealer.character_deck[0][1] + sett.reset_color} of "
                  f"{sett.red_color + dealer.character_deck[0][0] + sett.reset_color}", end='\r')

            sleep(2)
            print("                                                  ", end='')
            print(sett.up_line * 4, end='\r')
            continue

        else:
            print(" " * len(player_choice), end='\r')
            print("Input not recognized, try again", end='\r')
            sleep(1.5)
            print("                               ", end='\r')
            print(sett.up_line * 4, end='\r')
            continue

game_instance_object = game_instance.GameInstance()
deck = deck.Deck()
dealer = character.Dealer(deck)


while True:
    # This is where the pre-main game loop is stationed
    game_instance_object.menu_message()
    player_query = input("")

    match player_query:
        case "1" | "start game":
            game_instance_object.start_game()
            break
        case "2" | "introduction":
            game_instance_object.introduction()
        case "3" | "settings":
            game_instance_object.settings()
        case "4" | "quit game":
            game_instance_object.quit_game()
        case _:
            print("Input not recognized, try again", end='\r')
            sleep(1)
            system('cls')
            continue

    if player_query.lower() != ["1", "start game"]:
        system('cls')


while True:
    # This is where the main game loop is stationed

    # Building and shuffling the card deck
    deck.build()
    deck.shuffle()

    # If player_object_list is empty
    if not player_object_list:
        # Add players
        add_new_players()

        # Give each player their starting amount of chips
        for player in player_object_list:
            player.starting_chips()

    sleep(0.5)
    system('cls')

    # Storing the amount of players in the game
    number_of_players = len(player_object_list)

    # Each player bets their chips
    for player in player_object_list:
        player.bet_chips()
        system('cls')

    # The Blackjack game begins from here
    dealer.hit()
    dealer.first_draw()
    dealer.draw_card_deck()
    dealer.hand_value_check()
    sleep(1)
    print()

    # THE PLAYERS PLAY THEIR TURNS
    for player in player_object_list:
        system('cls')
        print(f"{sett.blue_color}{player.character_name}'s{sett.reset_color} turn to draw")
        sleep(1)
        hit_or_stand()

    sleep(1)
    system('cls')
    print("All players have completed each of their turns!\n")
    sleep(1.5)
    system('cls')
    print(f"{sett.red_color}{dealer.character_name}{sett.reset_color} will now draw the rest of their cards")
    sleep(1)

    # THE DEALER PLAYS THEIR TURN
    while True:
        sleep(1)
        dealer.hit()
        print()
        dealer.draw_card_deck()
        dealer.hand_value_check()
        sleep(1)
        if dealer.dealer_hit_limit():
            break

        system('cls')

    system('cls')
    sleep(0.5)
    print(f"{dealer.character_name} has finished drawing their cards!", end='\r')
    sleep(2)
    print("The end result will now be shown!                          ")
    sleep(1.5)
    system('cls')

    for player_number, player in enumerate(player_object_list, start=1):
        print(player.print_end_score(player_number))
        sleep(1)

    sleep(1)
    for line in range(40):
        sleep(0.05)
        print(sett.thick_horizontal_line, end='')

    sleep(1)
    dealer.dealer_after_game()
    sleep(2)

    # Sender nåværende linje til å være den første linjen i terminalen.
    print(sett.up_line * (number_of_players + 3), end='')

    for player_number, player in enumerate(player_object_list, start=1):
        sleep(1.5)
        print(player.calculate_end_result(dealer.deck_value, dealer.busted))

    print("\n")
    sleep(4)
    input("")
    system('cls')

    deck.destroy_deck()
    dealer.kill()

    # If the if-statement evaluates to true, the game restarts with the same players and their updated chips
    # If false, the game restarts and asks for new players. (The chips do not save)
    if game_instance_object.play_again_query():
        for player in player_object_list:
            player.kill()
        continue

    else:
        player_object_list.clear()
        system('cls')
        continue
