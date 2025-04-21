import ValueLookup as vl
from LegalMoves import ValidMoves as vm
from LegalMoves import CheckCastle as cc
from CheckLogic import CheckForCheck as cfc
import sys

class PlayerInput:

    players = vl.ValueLookup().players
    player_names = vl.ValueLookup().player_names
    soft_break = vl.ValueLookup().soft_break
    column_index = vl.ValueLookup().column_index

    # ------------------------------------------------------------------------
    def __init__(self, pi_board, pi_player) -> None:
        self.pi_board = pi_board
        self.pi_player = pi_player

    # ------------------------------------------------------------------------
    def checkInput(self, check_sys_move):

        invalid_move = False
        msg = ''
        
        if all(0 <= x <= 7 for x in check_sys_move) == False:
            invalid_move = True
            msg = "NOT WITHIN BOARD PARAMETERS"
            return invalid_move, msg

        if self.pi_board.board[check_sys_move[1]][check_sys_move[0]] == None:
            invalid_move = True
            msg = "EMPTY SPACE"
            return invalid_move, msg

        if self.pi_board.board[check_sys_move[1]][check_sys_move[0]].system_value * self.pi_player < 0:
            invalid_move = True
            msg = "CANNOT MOVE OPPONENTS PIECE"
            return invalid_move, msg

        legal_moves = vm.ValidMoves(self.pi_board.board, check_sys_move, self.pi_player).getValidMoves()
        if [check_sys_move[3],check_sys_move[2]] not in legal_moves:
            invalid_move = True
            msg = "ILLEGAL MOVE"
            return invalid_move, msg

        # IF CheckForCheck == True: (if Player in Check after move)
        #   invalid_move = True
        check_obj = cfc.CheckForCheck(self.pi_board, check_sys_move, PlayerInput.players[self.pi_player])
        check_obj.check_main()

        if check_obj.check_bool == True:
            invalid_move = True
            msg = "PLAYER IN CHECK"
            return invalid_move, msg

        return invalid_move, msg

    # ------------------------------------------------------------------------
    def getMoveInput(self, player_color):

        input_move = input(f'{PlayerInput.soft_break}\nPLAYER {PlayerInput.player_names[player_color]}, ENTER MOVE: ')
        print(PlayerInput.soft_break)

        if input_move == 'quit':
            sys.exit()

        return input_move

    # ------------------------------------------------------------------------
    def evalMoveInput(self, user_move):

        try:
            system_move = [ 
                            PlayerInput.column_index[user_move[0].upper()], 
                            int(user_move[1])-1, 
                            PlayerInput.column_index[user_move[2].upper()], 
                            int(user_move[3])-1
                            ]
        except:
            system_move = [-1,-1,-1,-1]

        return system_move

    # ------------------------------------------------------------------------
    def get_player_move(self, player_color, msg = ''):

        user_move = self.getMoveInput(player_color)

        castle_status = False
        if user_move.upper() == 'CASTLE LEFT' or user_move.upper() == 'CASTLE RIGHT':
            castle_status = cc.CheckCastle(user_move.upper(), player_color, self.pi_board).main()
            if castle_status == True:
                invalid_move = False
            else:
                invalid_move = True
                msg = 'INVALID CASTLE'
            system_move = None
        else:
            system_move = self.evalMoveInput(user_move)
            invalid_move, msg = self.checkInput(system_move) 

        return invalid_move, msg, castle_status, system_move
