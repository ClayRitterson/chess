import GameBoard as gb

         
class InitGame:

    def gameSetup(self):

        game_board = gb.GameBoard()

        game_board.initializeBoard()

        return game_board