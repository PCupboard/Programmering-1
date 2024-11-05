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
            player_object_list.append(character.Player(your_deck, game_instance_object.player_name))
            print(f"{sett.green_color}Name added to list of participating players{sett.reset_color}\n")
            sleep(0.5)
            continue

        else:
            print(f"{sett.red_color}Name rejected!{sett.reset_color}\n")
            continue

def hit_or_stand():
    for counting_variable in range(2):
        player.hit()
    player.draw_card_deck()
    sleep(1)
    player.hand_value_check()
    sleep(1)
    print()

    while True:
        print("Choose one of the following:")
        print("1) hit\n"
              "2) stand")
        player_choice = input("")
        if player_choice in "1" or player_choice.lower() in "hit":
            player.hit()
            system('cls')
            sleep(1)
            player.draw_card_deck()
            sleep(1)
            if player.hand_value_check():
                sleep(2)
                break
            else:
                sleep(1)
                print()

        elif player_choice in "2" or player_choice.lower() in "stand":
            print("You stand")
            print()
            break

        else:
            print("Input not recognized, try again")
            continue

game_instance_object = game_instance.GameInstance()
your_deck = deck.Deck()

while True:
    dealer = character.Dealer(your_deck)
    # This is where the pre-main game loop is stationed
    player_query = game_instance_object.start_query()

    if game_instance.check_for_int(player_query):
        match player_query:
            case "1":
                game_instance_object.start_game()
            case "2":
                game_instance_object.introduction()
            case "3":
                game_instance_object.settings()
            case "4":
                game_instance_object.quit_game()
    else:
        continue

    if player_query in '1':
        break


while True:
    # This is where the main game loop is stationed
    your_deck.build()
    your_deck.shuffle()

    print(player_object_list)

    # Adding new players
    if not player_object_list:
        add_new_players()

    number_of_players = len(player_object_list)

    # Each player bets their chips
    # TODO: Her er ingenting gjort ennå, men skal komme senere. Fokuserer på selve spillet for nå.

    # The Blackjack game begins from here
    #system('cls')

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
    print("")
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

    print(sett.up_line * (number_of_players + 3), end='')
    for player_number, player in enumerate(player_object_list, start=1):
        sleep(1.5)
        print(player.calculate_end_result(dealer.deck_value, dealer.busted))

    print("\n")
    sleep(4)
    input("")
    system('cls')

    your_deck.destroy_deck()
    dealer.clear_hand()

    # If the if-statement evaluates to true, the game restarts with the same players and their updated chips
    # If false, the game restarts and asks for new players. (The chips do not save)
    if game_instance_object.play_again_query():
        for player in player_object_list:
            player.clear_hand()
        continue

    else:
        del player_object_list
        player_object_list = []
        continue
