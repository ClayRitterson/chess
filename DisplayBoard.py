
import BoardPrinter as bp

class DisplayBoard:

    def __init__(self, display_board, player_color) -> None:
        self.display_board = display_board
        self.player_color = player_color

    def display_main(self):

        match self.player_color:
            case 'b':
                reverse_board_val = False
            case 'w':
                reverse_board_val = True

        bp.BoardPrinter(self.display_board, reverse_board=reverse_board_val).printBoard()