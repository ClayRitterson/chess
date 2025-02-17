import InitGame as ig
import BoardPrinter as bp


class Game:

    actual_board = None
    continue_game = True

    players = {
        -1 : 'b',
        1  : 'w'
    }

    player_names =  {

        'b': 'BLACK',
        'w': 'WHITE'
    }

    column_index = {
        'A':0,
        'B':1,
        'C':2,
        'D':3,
        'E':4,
        'F':5,
        'G':6,
        'H':7
    }

    current_player = 0

    def runGame(self):

        Game.actual_board = ig.InitGame().gameSetup()

        Game.current_player = 1
        while Game.continue_game:

            self.makeMove(Game.players[Game.current_player])
            
            Game.current_player = Game.current_player * -1
            pass

    def showBoard(self):
        
        bp.BoardPrinter(Game.actual_board.board).print_board()
        bp.BoardPrinter(Game.actual_board.board).print_board(display_or_system='system')

    
    def makeMove(self, player_color):

        line_break = '*' * 35

        match player_color:
            case 'b':
                reverse_board_val = False
            case 'w':
                reverse_board_val = True

        bp.BoardPrinter(Game.actual_board.board).print_board(reverse_board=reverse_board_val)

        user_move = input(f'{line_break}\nPLAYER {Game.player_names[player_color]}, ENTER MOVE: ')
        print(line_break)

        try:
            system_move = [Game.column_index[user_move[0].upper()], int(user_move[1])-1, Game.column_index[user_move[2].upper()], int(user_move[3])-1]
        except:
            system_move = [-1,-1,-1,-1]

        invalid_move = False
        if all(0 <= x <= 7 for x in system_move) == False:
            invalid_move = True
            msg = "NOT WITHIN BOARD PARAMETERS"

        if Game.actual_board.board[system_move[1]][system_move[0]].system_value * Game.current_player < 0:
            invalid_move = True
            msg = "CANNOT MOVE OPPONENTS PIECE"
            
        if invalid_move:
            print(f'{line_break}\nINVAID MOVE, {msg}\n{line_break}\n')
        else:
            Game.actual_board.board[system_move[3]][system_move[2]] = Game.actual_board.board[system_move[1]][system_move[0]]
            Game.actual_board.board[system_move[1]][system_move[0]] = None




