import settings as sett
from time import sleep
from os import system
import json

# ----- GAME INSTANCE CLASS ----- #
class GameInstance:
    def __init__(self):
        self.user_query = ""
        self.player_name = ""
        self.game_name = "Blackjack"

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

    def menu_message(self) -> None:
        print("You have four options:")
        print(f"1) Start Game -- Starts {self.game_name}")
        print(f"2) Information -- Gives additional information on {self.game_name}")
        print(f"3) Settings -- Opens the settings menu for {self.game_name}")
        print(f"4) Quit Game -- Exits {self.game_name}\n")

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

        print("Press enter to go back to the main menu")
        self.user_query = input("")


    def settings(self):
        print(f"WIP feature for {self.game_name}\n")
        print("Press enter to go back to the main menu")
        self.user_query = input("")

    def quit_game(self) -> None:
        print(f"Quitting {self.game_name}")
        sleep(0.2)
        exit()

    def new_player(self) -> None:
        self.player_name = input("Enter name for the new player: ").lower()
        print(sett.up_line," " * 30 + " " * len(self.player_name) , end='\r')

    def play_again_query(self) -> bool:
        print("Do you want to play again? (y/n)")
        self.user_query = input("")
        sleep(0.5)
        system('cls')
        if self.user_query.lower() in "yes":
            print("Do you want to play the game with the same characters? (y/n)")
            self.user_query = input("")
            print()

            if self.user_query.lower() in "yes":
                return True

            else:
                # PLayers should be saved here
                return False

        else:
            # players should be saved here
            exit()

def save_game(file_name, player_information):
    # Save each of the players name and chips in a dictionary?
    # Then use a different function to load them in?
    # That function can only be used each time you start the program
    # So settings will be replaced with load game function
    # Load game function will be used to load in the dictionary that contains player names and player chips



    with open(file_name, 'w') as write_file:
        json.dump(player_information, write_file, indent=3)

    pass