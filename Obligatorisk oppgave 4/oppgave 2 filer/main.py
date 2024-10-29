import os
import character
import deck
import game_instances


player_object_list = []
player_list = []

def hit_or_stand():
    while True:
        print("What do you want to do?")
        print("1) hit\n"
              "2) stand\n")
        player_choice = input("")
        if player_choice == "1":
            player.hit()
            player.draw_card_deck()
            if player.busted_check():
                break

        elif player_choice == "2":
            print("You stand")
            break

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

    #if player_query != "1":
     #   continue

    # This is code after the game has begun
    game_running_instance = game_instances.RunningGameInstance()

    # Adding new players
    while True:
        game_running_instance.new_player()
        if game_running_instance.player_name in '':
            break

        elif game_running_instance.player_name.isalpha():
            player_object_list.append(character.Player(your_deck, game_running_instance.player_name))
            player_list.append(game_running_instance.player_name)
            print("Name added to list of participating players\n")
            continue

        else:
            print("Name rejected")
            continue

    for player in player_object_list:
        print(player.character_name)
    print()

    # Hver spiller satser sine chips
    # TODO: Her er ingenting gjort ennå, men skal komme senere. Fokuserer på selve spillet for nå.

    # Blackjack spillet begynner herfra;
    os.system('cls')
    dealer.hit()
    print("The dealer's card")
    dealer.draw_card_deck()

    for player in player_object_list:
        print(f"{player.character_name}'s turn to draw")
        hit_or_stand()

    print("All players have done their turn.")
    input("")
