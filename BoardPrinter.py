class BoardPrinter:

    def __init__(self, board_to_print) -> None:
        self.board_to_print = board_to_print

    def print_board(self, display_or_system='display'): # Prints the board state in human readable format

        print_board = self.board_to_print[:]
        print_board.reverse()
        print(f'\n{display_or_system.upper()} BOARD')
        for i in range(len(print_board)):
            print('-------------------------')
            print_row = ''
            for j in range(len(print_board[i])):
                print_row += '|'
                try:
                    match display_or_system:
                        case 'display':
                            print_row += print_board[i][j].display_value
                        case 'system':
                            if print_board[i][j].system_value > 0:
                                print_row += ' '
                            print_row += str(print_board[i][j].system_value)
                except:
                    print_row += '  '
            print_row += '|'
            print(print_row)
        print('-------------------------\n')

            