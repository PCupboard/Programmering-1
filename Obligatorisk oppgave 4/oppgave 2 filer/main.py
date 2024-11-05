from os import system
from time import sleep
import character
import deck
import game_instances
import settings as sett

player_object_list = []
#player_list = []

def hit_or_stand():
    while True:
        print("Choose one of the following:")
        print("1) hit\n"
              "2) stand")
        player_choice = input("")
        if player_choice in "1" or player_choice.lower() in "hit":
            player.hit()
            system('cls')
            player.draw_card_deck()
            if player.hand_value_check():
                sleep(2)
                break

        elif player_choice in "2" or player_choice.lower() in "stand":
            print("You stand")
            print()
            break

        else:
            print("Input not recognized, try again")
            continue

def add_new_players():
    while True:
        game_running_instance.new_player()
        if game_running_instance.player_name.strip() in '':
            if len(player_object_list) >= 1:
                break

            else:
                print("You need atleast one player to play Blackjack!\n")
                continue

        elif len(game_running_instance.player_name) > 64:
            print("This name is too long!\n")
            continue

        elif game_running_instance.player_name.isalpha():
            player_object_list.append(character.Player(your_deck, game_running_instance.player_name))
            #player_list.append(game_running_instance.player_name)
            print(f"{sett.green_color}Name added to list of participating players{sett.reset_color}\n")
            sleep(1)
            continue

        else:
            print("Name rejected!\n")
            continue

game_start_instance = game_instances.StartingGameInstance()
your_deck = deck.Deck()
your_deck.build()
your_deck.shuffle()

dealer = character.Dealer(your_deck)


while True:
    # This is where the pre-main game loop is stationed
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

    if player_query in '1':
        break


game_running_instance = game_instances.RunningGameInstance()


while True:
    # This is where the main game loop is stationed
    # Adding new players
    if not player_object_list:
        add_new_players()

    number_of_players = len(player_object_list)

    # Each player bets their chips
    # TODO: Her er ingenting gjort ennå, men skal komme senere. Fokuserer på selve spillet for nå.

    # The Blackjack game begins from here
    system('cls')

    dealer.hit()
    dealer.first_draw()
    dealer.draw_card_deck()
    dealer.hand_value_check()
    print()


    for player_number, player in enumerate(player_object_list, start=1):
        sleep(1.5)
        system('cls')
        print(f"{sett.blue_color}{player.character_name}'s{sett.reset_color} turn to draw")
        hit_or_stand()
        if number_of_players < player_number:
            print("Next player's turn:")

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
        dealer.draw_card_deck()
        dealer.hand_value_check()
        sleep(1)
        if dealer.dealer_hit_limit():
            break

        sleep(1)
        system('cls')

    system('cls')
    print("THE GAME HAS FINISHED")
    sleep(1)
    system('cls')
    sleep(1)

    for player_number, player in enumerate(player_object_list, start=1):
        print(player.print_end_score(player_number))
        sleep(1)

    for i in range(40):
        sleep(0.075)
        print(sett.thick_horizontal_line, end='')

    sleep(1)
    dealer.dealer_after_game()

    print(sett.up_line * (number_of_players + 3), end="")
    for player_number, player in enumerate(player_object_list, start=1):
        sleep(1.5)
        print(player.calculate_end_result(dealer.deck_value))

    sleep(5)
    system('cls')

    if game_running_instance.play_again_query():
        continue

    else:
        player_object_list.clear()
        continue