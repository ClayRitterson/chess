import random

class GameSettings:

    play_again_map = {
        0: "QUIT",
        1: "PLAY CHESS"
    }

    play_again_msg = "\n\nSELECT OPTION\n--------------------------\n1 = PLAY CHESS\n0 = QUIT\n--------------------------"

    cpu_player_msg = "\n--------------------------\nSELECT # OF CPU PLAYERS:\n--------------------------\n[0,1,2]\n--------------------------"

    welcome_msg = "\n\n--------------------------\nWELCOME TO CHESS!\n--------------------------"

    # ------------------------------------------------------------------------
    def __init__(self) -> None:
        self.player_white = None
        self.player_black = None
        self.game_status = None
        self.cpu_status = None

    # ------------------------------------------------------------------------
    def main(self):

        self.print_welcome_msg()

        self.user_game_input()

        if self.game_status == 0:
            return False
        elif self.game_status == 1:
            self.user_cpu_player()
        else:
            return False

        self.set_human_cpu_players()

        return True

    # ------------------------------------------------------------------------
    def print_welcome_msg(self):
        
        print(GameSettings.welcome_msg)

    # ------------------------------------------------------------------------
    def set_human_cpu_players(self):

        if self.cpu_status == 2:
            self.player_white = 'cpu'
            self.player_black = 'cpu'
        elif self.cpu_status == 1:
            randomize = random.random()
            if randomize >= 0.5:
                self.player_white = 'human'
                self.player_black = 'cpu'
            else:
                self.player_white = 'cpu'
                self.player_black = 'human'
        else:
            self.player_white = 'human'
            self.player_black = 'human'

    # ------------------------------------------------------------------------
    def user_cpu_player(self):

        valid_input = False
        print(GameSettings.cpu_player_msg)
        while valid_input == False:

            user_input = input("ENTER: ")

            match user_input:
                case '0':
                    self.cpu_status = 0
                    valid_input = True
                case '1':
                    self.cpu_status = 1
                    valid_input = True
                case '2':
                    self.cpu_status = 2
                    valid_input = True
                case _:
                    print("INVALID INPUT, TRY AGAIN!")

        return  

    # ------------------------------------------------------------------------
    def user_game_input(self):

        valid_input = False
        print(GameSettings.play_again_msg)
        while valid_input == False:

            user_input = input("ENTER: ")

            match user_input:
                case '0':
                    self.game_status = 0
                    valid_input = True
                case '1':
                    self.game_status = 1
                    valid_input = True
                case _:
                    print("INVALID INPUT, TRY AGAIN!")

        return