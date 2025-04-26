# Start program from here

import Game as g
import GameSettings as gs
import sys


class Main:

    def __init__(self) -> None:
        pass

    # ------------------------------------------------------------------------
    def main(self):
            
        play_again = True
        while play_again == True:

            gs_obj = gs.GameSettings()
            
            game_true = gs_obj.main()

            if game_true:
                current_game = g.Game(gs_obj)
                current_game.runGame()
            else:
                play_again = False

Main().main()
sys.exit()

                    

