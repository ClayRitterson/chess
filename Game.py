import InitGame as ig
import BoardPrinter as bp


class Game:

    actual_board = None

    def runGame(self):

        Game.actual_board = ig.InitGame().gameSetup()

    def showBoard(self):
        
        bp.BoardPrinter(Game.actual_board.board).print_board()
        bp.BoardPrinter(Game.actual_board.board).print_board('system')


