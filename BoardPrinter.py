class BoardPrinter:

    def __init__(self, board_to_print) -> None:
        self.board_to_print = board_to_print

    def print_board(self, reverse_board=True, display_or_system='display'): # Prints the board state in human readable format
        
        rows = [1,2,3,4,5,6,7,8]
        print_cols = '    A  B  C  D  E  F  G  H '
        print_board = self.board_to_print[:]
        if reverse_board:
            print_board.reverse()
            rows.reverse()
        print(f'\n{display_or_system.upper()} BOARD')
        print(print_cols)
        for i in range(len(print_board)):
            print('  -------------------------')
            print_row = f'{str(rows[i])} '
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
            print_row += f'| {str(rows[i])} '
            print(print_row)
        print('  -------------------------')
        print(f'{print_cols}\n')

            