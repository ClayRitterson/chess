class BoardPrinter:

    # ------------------------------------------------------------------------
    def __init__(self, board_to_print, reverse_board = True,  display_or_system='display'):
        self.board_to_print = board_to_print
        self.reverse_board = reverse_board
        self.display_or_system = display_or_system
        self.row_numbers = [1,2,3,4,5,6,7,8]
        self.print_cols = ''

    # ------------------------------------------------------------------------
    def flipBoardHorizontal(self, board_to_flip):
        flipped_board = []
        for y in range(len(board_to_flip)):
            flipped_board.append(board_to_flip[y][::-1])
        return flipped_board

    # ------------------------------------------------------------------------
    def boardSetup(self):

        space = '    '
        column_letters = 'A  B  C  D  E  F  G  H'

        print_board = self.board_to_print[:] # Copy board

        if self.reverse_board == True: # White
            self.print_cols = space + column_letters
            print_board.reverse()
            self.row_numbers.reverse()
        else: # Black
            pass
            self.print_cols = space + column_letters[::-1]
            print_board = self.flipBoardHorizontal(print_board[:])
        
        return print_board

    # ------------------------------------------------------------------------
    def printBoard(self): # Prints the board state in human readable format
    
        print_board = self.boardSetup()

        print(f'\n{self.display_or_system.upper()} BOARD')
        print(self.print_cols)
        for i in range(len(print_board)):
            print('  -------------------------')
            print_row = f'{str(self.row_numbers[i])} '
            for j in range(len(print_board[i])):
                print_row += '|'
                try:
                    match self.display_or_system:
                        case 'display':
                            print_row += print_board[i][j].display_value
                        case 'system':
                            if print_board[i][j].system_value > 0:
                                print_row += ' '
                            print_row += str(print_board[i][j].system_value)
                except:
                    print_row += '  '
            print_row += f'| {str(self.row_numbers[i])} '
            print(print_row)
        print('  -------------------------')
        print(f'{self.print_cols}\n')

            