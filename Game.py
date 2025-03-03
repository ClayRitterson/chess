import InitGame as ig
import BoardPrinter as bp
import ValidMoves as vm

class Game:

    actual_board = None
    continue_game = True

    line_break = '*' * 35

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
        
        bp.BoardPrinter(Game.actual_board.board).printBoard()
        bp.BoardPrinter(Game.actual_board.board, display_or_system='system').printBoard()


    def checkInput(self, check_sys_move):

        invalid_move = False
        msg = ''
        
        check_input = True
        while check_input == True:
            if Game.actual_board.board[check_sys_move[1]][check_sys_move[0]] == None:
                invalid_move = True
                msg = "EMPTY SPACE"
                break

            if all(0 <= x <= 7 for x in check_sys_move) == False:
                invalid_move = True
                msg = "NOT WITHIN BOARD PARAMETERS"
                break

            if Game.actual_board.board[check_sys_move[1]][check_sys_move[0]].system_value * Game.current_player < 0:
                invalid_move = True
                msg = "CANNOT MOVE OPPONENTS PIECE"
                break
            check_input = False

        legal_moves = vm.ValidMoves(Game.actual_board.board, check_sys_move, Game.current_player).getValidMoves()
        if [check_sys_move[3],check_sys_move[2]] not in legal_moves:
            invalid_move = True
            msg = "ILLEGAL MOVE"

        return invalid_move, msg

    def getMoveInput(self, player_color):

        input_move = input(f'{Game.line_break}\nPLAYER {Game.player_names[player_color]}, ENTER MOVE: ')
        print(Game.line_break)

        return input_move

    def evalMoveInput(self, user_move):

        try:
            system_move = [ 
                            Game.column_index[user_move[0].upper()], 
                            int(user_move[1])-1, 
                            Game.column_index[user_move[2].upper()], 
                            int(user_move[3])-1
                            ]
        except:
            system_move = [-1,-1,-1,-1]


        return system_move

    
    def makeMove(self, player_color):


        match player_color:
            case 'b':
                reverse_board_val = False
            case 'w':
                reverse_board_val = True

        bp.BoardPrinter(Game.actual_board.board, reverse_board=reverse_board_val).printBoard()

        valid_input=False

        while valid_input==False:
            
            user_move = self.getMoveInput(player_color)

            system_move = self.evalMoveInput(user_move)

            invalid_move, msg = self.checkInput(system_move) 
            
            if invalid_move:
                print(f'{Game.line_break}\nINVAID MOVE, {msg}\n{Game.line_break}\n')
            else:
                Game.actual_board.board[system_move[3]][system_move[2]] = Game.actual_board.board[system_move[1]][system_move[0]]
                Game.actual_board.board[system_move[1]][system_move[0]] = None
                valid_input = True




