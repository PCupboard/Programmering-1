import settings as sett
from time import sleep
from os import system, listdir
import json

player_information_dict = []


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
        print(f"2) Load Game -- Loads player data if there is an available json file")
        print(f"3) Information -- Gives additional information on {self.game_name}")
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


    def load_game(self):
        system('cls')
        json_files = []

        for file in listdir():
            if file.endswith(".json"):
                json_files.append(file)

        if not json_files:
            print("There are no files to load data from!")
            return

        sleep(1)

        print("Available files in the current working directory:")
        for file in json_files:
            sleep(0.5)
            print(file)

        sleep(1.5)
        print()
        print("When writing the file name, the extension is not needed,\n"
              "only the name with no symbols or spaces is needed.\n")
        sleep(2)

        while True:
            file_name = input("Enter file name: ").lower()
            sleep(1)
            print(sett.up_line, end='\r')
            print("                 ", end='')
            print(" " * len(file_name), end='\r')
            if file_name.isalpha():
                file_name = file_name.lower() + ".json"

            else:
                print("This is not a valid file name!", end='\r')
                sleep(1)
                print("                              ", end='\r')
                continue

            try:
                read_file = open(file_name, "r")

            except FileNotFoundError:
                print("File not found! Try again", end='\r')
                sleep(1)
                print("                         ", end='\r')
                continue

            else:
                player_information = json.load(read_file)
                print(f"{sett.green_color}File successfully loaded!{sett.reset_color}")
                sleep(1.5)
                system('cls')

                print("Press enter to go back to the main menu")
                self.user_query = input("")
                return player_information



    def quit_game(self) -> None:
        print(f"Quitting {self.game_name}")
        sleep(0.2)
        exit()

    def new_player(self) -> None:
        self.player_name = input("Enter name for the new player: ").lower()
        print(sett.up_line," " * 30 + " " * len(self.player_name) , end='\r')

    def play_again_query(self) -> bool:
        print("Do you want to play again? (y/n)")
        while True:
            self.user_query = input("")
            sleep(0.5)
            if self.user_query.lower() in "yes":
                return True

            elif self.user_query.lower() in 'no':
                return False

            else:
                print(sett.up_line, end='\r')
                print(" " * len(self.user_query), end='\r')
                print("Input not recognized, try again...", end='\r')
                sleep(1)
                print("                                  ", end='\r')
                continue



def players_information_dict(player_name, player_chips):
    new_player_information = {"name": player_name, "chips": player_chips}
    player_information_dict.append(new_player_information)


def save_game():
    # Save each of the players name and chips in a dictionary?
    # Then use a different function to load them in?
    # That function can only be used each time you start the program
    # So settings will be replaced with load game function
    # Load game function will be used to load in the dictionary that contains player names and player chips

    print("When writing the file name, the extension is not needed,\n"
          "only the name with no symbols or spaces is needed.")
    sleep(1)

    while True:
        file_name = input("Enter file name: ")

        if file_name.isalpha():
            file_name = file_name.lower() + ".json"
            print("File saved!")
            sleep(1.5)
            break
        else:
            print(sett.up_line, end='\r')
            print(" " * len(file_name), end='\r')
            print("Please enter a valid file name.")
            sleep(0.5)
            continue

    with open(file_name, 'w') as write_file:
        json.dump(player_information_dict, write_file, indent=3)

def load_game():
    pass