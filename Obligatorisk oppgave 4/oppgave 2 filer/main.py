from os import system
from time import sleep

import character
import deck
import game_instance
import settings as sett

player_object_list = []
player_name_list = []
losing_player_list = []

def add_new_players():
    while True:
        system('cls')
        print("You can press enter to stop adding new players!\n"
              "Type 'players' to print all the players currently in the game!\n"
              f"You can add up to {sett.yellow_color}8{sett.reset_color} players to the game")

        if len(player_object_list) == 0:
            print(f"There are currently {sett.magenta_color}{len(player_object_list)}{sett.reset_color} players in the game.\n")

        elif len(player_object_list) == 1:
            print(f"There is currently {sett.yellow_color}{len(player_object_list)}{sett.reset_color} player in the game.\n")

        else:
            print(f"There are currently {sett.yellow_color}{len(player_object_list)}{sett.reset_color} players in the game.\n")

        sleep(0.5)
        removed_player = False

        game_instance_object.new_player()

        for player_name in player_name_list:
            if game_instance_object.player_name == player_name:
                print(f"{sett.magenta_color}This player is already participating in the game!{sett.reset_color}")
                sleep(1)
                removed_player = True

        if removed_player:
            continue

        if game_instance_object.player_name.strip() in '':
            if len(player_object_list) >= 1:
                sleep(0.5)
                system('cls')
                print(f"{sett.yellow_color}The game will now start!{sett.reset_color}")
                sleep(1)
                break

            else:
                print(f"{sett.magenta_color}You need atleast one player to play Blackjack!{sett.reset_color}")
                sleep(1)
                system('cls')
                continue

        elif len(game_instance_object.player_name) > 64:
            print(f"{sett.magenta_color}This name is too long!{sett.reset_color}")
            sleep(1)
            system('cls')
            continue

        elif game_instance_object.player_name.strip().lower() == 'players':
            if player_object_list:
                for player_f in player_object_list:
                    print(player_f.character_name)
                    sleep(1)
            else:
                print(f"{sett.magenta_color}There are currently no players in the game!{sett.reset_color}")

            sleep(1)

        elif game_instance_object.player_name.isalpha():
            player_object_list.append(character.Player(deck, game_instance_object.player_name))
            player_name_list.append(game_instance_object.player_name)

            print(f"{sett.green_color}Added {sett.blue_color}{game_instance_object.player_name.title()}{sett.green_color}"
                  f" to the list of participating players{sett.reset_color}", end='\r')
            sleep(1)

            if len(player_object_list) == 8:
                print(f"You have added the maximum amount of allowed players!")
                sleep(1.5)
                system('cls')
                print(f"{sett.yellow_color}The game will now start!{sett.reset_color}")
                sleep(1)
                break

            continue

        else:
            print(f"{sett.red_color}Name rejected!{sett.reset_color}")
            sleep(1)
            system('cls')
            continue

def load_players(players_info) -> None:
    for dictionary in players_info:
        player_object_list.append(character.Player(deck, str(dictionary['name']), int(dictionary['chips'])))



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
    user_query = input("")
    print(sett.up_line, end='\r')

    match user_query:
        case "1" | "start game":
            game_instance_object.start_game()
            break
        case "2" | "load game":
            if not player_object_list:
                players_dict = game_instance_object.load_game()
                if players_dict:
                    load_players(players_dict)
            else:
                print(f"{sett.yellow_color}You already have players in the game!{sett.reset_color}")
                sleep(2)
                system('cls')

        case "3" | "introduction":
            game_instance_object.introduction()
        case "4" | "quit game":
            game_instance_object.quit_game()
        case _:
            print("Input not recognized, try again", end='\r')
            sleep(1)
            system('cls')
            continue

    if user_query.lower() != ["1", "start game"]:
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
    sleep(1.5)

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

    print(sett.up_line * (number_of_players + 3), end='')

    for player in player_object_list:
        sleep(1.5)
        print(player.calculate_end_result(dealer.deck_value, dealer.busted, dealer.blackjack))


    sleep(3)
    print("\n\n\nPress enter to continue...")
    input("")
    system('cls')

    deck.destroy_deck()
    dealer.kill()

    # Check each player if they have zero chips, if they do, ask what to do about that specific player
    for player in player_object_list:
        if player.kill():
            print(
                f"{sett.blue_color}{player.character_name}{sett.reset_color} Has {sett.cyan_color}0{sett.reset_color} chips remaining!\n")
            print(f"what would you like to do?\n"
                  f"1) Remove {player.character_name} from the game\n"
                  f"2) Give {player.character_name} new chips")

            while True:
                user_query = input("")
                print(sett.up_line, end='\r')

                if user_query in "1":
                    losing_player_list.append(player)
                    print(
                        f"{sett.blue_color}{player.character_name}{sett.reset_color} has been removed from the game!\n")
                    sleep(1)
                    system('cls')
                    break

                elif user_query in "2":
                    player.starting_chips()
                    print(
                        f"{sett.blue_color}{player.character_name}{sett.reset_color} has been given a new set of chips!\n")
                    sleep(1)
                    system('cls')
                    break

                else:
                    print("Input not recognized, try again", end='\r')
                    print("                               ")
                    sleep(0.5)
                    continue

    for name in player_object_list:
        if name in losing_player_list:
            player_object_list.remove(name)
            losing_player_list.remove(name)

    # Ask the player if they want to play again
    if game_instance_object.play_again_query():
        print("Do you want to play the game with the same characters? (y/n)")
        user_query = input("")
        if user_query in "yes":
            sleep(0.5)
            for player in player_object_list:
                game_instance.players_information_dict(player.character_name, player.chips)
            game_instance.save_game()
            sleep(0.5)
            system('cls')
            sleep(1)
            print("Restarting the game!")
            sleep(1.5)

        if user_query in "no":
            # Players are saved here
            for player in player_object_list:
                game_instance.players_information_dict(player.character_name, player.chips)
            game_instance.save_game()

            # The players are removed after being saved
            player_object_list.clear()
            system('cls')
            continue

    else:
        # Players are saved here
        for player in player_object_list:
            game_instance.players_information_dict(player.character_name, player.chips)
        game_instance.save_game()

        # Quitting program
        exit()