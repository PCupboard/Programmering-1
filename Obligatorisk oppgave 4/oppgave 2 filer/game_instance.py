import settings as sett
from time import sleep
from os import system

# ----- GAME INSTANCE CLASS ----- #
class GameInstance:
    def __init__(self):
        self.user_query = ""
        self.player_name = ""
        self.game_name = "Blackjack"
        self.user_query_bool = False

        print("|----------------------|")
        print("<                      >")
        print("|----------------------|")
        sleep(1)
        print(f"{sett.up_line + sett.up_line}< Welcome              >", end='\r')
        sleep(0.5)
        print("< Welcome To           >", end='\r')
        sleep(0.5)
        print(f"< Welcome To {sett.red_color + self.game_name + sett.reset_color} \n\n")
        sleep(1)
        print(f"A Program made by Patrick Jemieljanczyk")
        sleep(1)
        system('cls')

    def start_query(self) -> str:
        print("\nYou have four options:")
        print(f"1) Start Game -- Starts {self.game_name}")
        print(f"2) Information -- Gives additional information on {self.game_name}")
        print(f"3) Settings -- Opens the settings menu for {self.game_name}")
        print(f"4) Quit Game -- Exits {self.game_name}\n")

        self.user_query = input("Which option will you choose: ")
        return self.user_query

    def start_game(self) -> None:
        print(f"Starting {self.game_name}.", sett.up_line)
        sleep(0.5)
        print(f"Starting {self.game_name}..", sett.up_line)
        sleep(0.5)
        print(f"Starting {self.game_name}...\n")
        sleep(1)
        system('cls')

    def introduction(self) -> None:
        system('cls')
        print(f"{self.game_name} is a casino banking game. It is the most widely played casino banking game in the world.\n"
               "It uses a standard deck of 52 cards and is played by around 5 to 9 players at a time.\n"
               "A dealer is facing these players and plays against them.\n"
               "At the start of each round, each player place a bet which represents the player's money.\n"
               "The dealer gets initially one card which all players can see the value of.\n"
               "This program plays more after European casinos, therefore the dealer's second card is drawn\n"
               "only after the players have played their hand.\n"
               "Each player gets two choices, to either hit or stand. If the player chooses to hit, they will draw a card.\n"
               "if the player chooses to stand, they will pass their turn to the next player.\n"
               "Each drawn card includes a value, each drawn card will increase the value of your hand.\n"
               "If the value of your hand ends up being higher than 21.\n"
             )

        print("Go back to main menu:")
        self.user_query = input("")


    def settings(self):
        print(f"WIP feature for {self.game_name}\n")

    def quit_game(self) -> None:
        print(f"Quitting {self.game_name}")
        sleep(0.2)
        exit()

    def new_player(self) -> None:
        self.player_name = input("Enter name for the new player: ")

    def play_again_query(self) -> bool:
        print("Do you want to play again? (y/n)")
        self.user_query = input("")
        sleep(0.5)
        system('cls')
        if self.user_query.lower() in "y" or "yes":
            print("Do you want to play the game with the same characters? (y/n)")
            self.user_query = input("")
            print()

        else:
            exit()

        if self.user_query.lower() in "y" or "yes":
            self.user_query_bool = True
            return self.user_query_bool

        else:
            return self.user_query_bool

def check_for_int(player_input) -> bool:
    try:
        player_input = int(player_input)

    except ValueError:
        print("This is not a number, try again\n\n")

    else:
        if 0 < player_input < 5:
            return True
        else:
            print("Number not recognized, try again\n\n")
            return False