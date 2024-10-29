import os
import character
import deck
import game_instances
import settings as sett
import time

player_object_list = []
player_list = []

def hit_or_stand():
    while True:
        print("Choose one of the following:")
        print("1) hit\n"
              "2) stand")
        player_choice = input("")
        if player_choice in "1" or player_choice.lower() in "hit":
            player.hit()
            player.draw_card_deck()
            if player.busted_check():
                break

        elif player_choice in "2" or player_choice.lower() in "stand":
            print("You stand")
            print()
            break

        else:
            print("Input not recognized, try again")
            continue

game_start_instance = game_instances.StartingGameInstance()
your_deck = deck.Deck()
your_deck.build()
your_deck.shuffle()

dealer = character.Dealer(your_deck)


while True:
    # This is where the game loop is stationed

    # This is code before the game begins
    player_query = game_start_instance.start_query()

    if game_instances.check_for_int(player_query):
        match player_query:
            case "1":
                game_start_instance.start_game()
            case "2":
                game_start_instance.introduction()
            case "3":
                game_start_instance.settings()
            case "4":
                game_start_instance.quit_game()
    else:
        continue

    # This is code after the game has begun
    game_running_instance = game_instances.RunningGameInstance()

    # Adding new players
    while True:
        game_running_instance.new_player()
        if game_running_instance.player_name in '':
            if not len(player_list) >= 1:
                print("You need atleast one player to play Blackjack!\n")
                continue

            else:
                break

        elif game_running_instance.player_name.isalpha():
            player_object_list.append(character.Player(your_deck, game_running_instance.player_name))
            player_list.append(game_running_instance.player_name)
            print("Name added to list of participating players\n")
            continue

        else:
            print("Name rejected\n")
            continue

    print("Players participating in the Blackjack game:")
    for player_number, player in enumerate(player_object_list, start=1):
        player.print_player_name(player_number)

    # Hver spiller satser sine chips
    # TODO: Her er ingenting gjort ennå, men skal komme senere. Fokuserer på selve spillet for nå.

    # Blackjack spillet begynner herfra
    os.system('cls')

    dealer.hit()
    dealer.first_draw()
    dealer.draw_card_deck()
    dealer.busted_check()
    print()

    number_of_players = len(player_list)

    for player_number, player in enumerate(player_object_list, start=1):
        print(f"{sett.blue_color}{player.character_name}'s{sett.reset_color} turn to draw")
        hit_or_stand()
        if number_of_players < player_number:
            print("Next player's turn:")

    print("All players have completed each of their turns!\n")
    time.sleep(1)
    print(f"{sett.red_color}{dealer.character_name}{sett.reset_color} will now draw their cards")
    while True:
        dealer.hit()
        dealer.draw_card_deck()
        dealer.busted_check()
        print()
        if dealer.dealer_hit_limit():
            break


    print("THE GAME HAS FINISHED")
    input("")
    break