import ValueLookup as vl
from CheckLogic import CheckForCheck as cfc
from Display import DisplayBoard as db


class CheckCastle:

    castle_rook_file_map = {
        'CASTLE LEFT': {1: 0, -1: 7},
        'CASTLE RIGHT': {1: 7, -1: 0}
    }

    check_lane_direction_map = {
        'CASTLE LEFT': {1: -1, -1: 1},
        'CASTLE RIGHT': {1: 1, -1: -1}
    }

    bw_val_map = vl.ValueLookup().bw_val_map
    castle_map = vl.ValueLookup().castle_map
    piece_val_map = vl.ValueLookup().piece_val_map
    players = vl.ValueLookup().players

    # ------------------------------------------------------------------------
    def __init__(self, castle_move, player_color, game_board) -> None:
        self.castle_move = castle_move
        self.player_color = player_color
        self.game_board = game_board
        self.king_pos = []
        self.rook_pos = []
        self.direction = 0
        self.distance = 0

    # ------------------------------------------------------------------------
    def main(self):

        valid_castle = True

        # Check that niether piece has moved
        self.king_pos =  [CheckCastle.castle_map[self.player_color], 4]
        self.rook_pos =  [CheckCastle.castle_map[self.player_color], 
                        CheckCastle.castle_rook_file_map[self.castle_move][CheckCastle.bw_val_map[self.player_color]]]

        # Set Distance and Direction
        self.direction = CheckCastle.check_lane_direction_map[self.castle_move][CheckCastle.bw_val_map[self.player_color]]
        self.distance = abs(self.rook_pos[1] - self.king_pos[1]) - 1
        
        # Check King
        valid_castle = self.check_has_moved(self.king_pos, CheckCastle.piece_val_map['K'], valid_castle)
        
        # Check Rook
        valid_castle = self.check_has_moved(self.rook_pos, CheckCastle.piece_val_map['R'], valid_castle)

        # Check that lane is clear
        valid_castle, eval_check_sqaures = self.check_lane(valid_castle)

        # Check that lane doesn't cause check
        for i in range(len(eval_check_sqaures)):
            move_index = [self.king_pos[1], self.king_pos[0], eval_check_sqaures[i][1], eval_check_sqaures[i][0]]
            check_obj = cfc.CheckForCheck(self.game_board, move_index, self.player_color)
            check_obj.check_main()

            if check_obj.check_bool == True:
                valid_castle = False
        
        if valid_castle == True:
            self.perform_castle()

        return valid_castle

    # ------------------------------------------------------------------------
    def perform_castle(self):

        move_king_to_file = self.king_pos[1] + (self.direction * 2)

        self.game_board.board[self.king_pos[0]][move_king_to_file] = self.game_board.board[self.king_pos[0]][self.king_pos[1]]
        self.game_board.board[self.king_pos[0]][self.king_pos[1]] = None

        move_rook_to_file = self.rook_pos[1] + (self.direction * self.distance * -1)

        self.game_board.board[self.rook_pos[0]][move_rook_to_file] = self.game_board.board[self.rook_pos[0]][self.rook_pos[1]]
        self.game_board.board[self.rook_pos[0]][self.rook_pos[1]] = None

    # ------------------------------------------------------------------------
    def check_lane(self, valid_castle):

        return_squares = []
        
        for i in range(self.distance):
            check_square = self.game_board.board[self.king_pos[0]][self.king_pos[1] + ((i + 1) * self.direction)]
            return_squares.append([self.king_pos[0],self.king_pos[1] + ((i + 1) * self.direction)])
            if check_square != None:
                valid_castle = False
        
        return valid_castle, return_squares

    # ------------------------------------------------------------------------       
    def check_has_moved(self, pos, check_system_val, valid_castle):
        if self.game_board.board[pos[0]][pos[1]] != None:
            potential_castle_piece = self.game_board.board[pos[0]][pos[1]]
            if abs(potential_castle_piece.system_value) != check_system_val:
                valid_castle = False
            elif potential_castle_piece.has_moved == True:
                valid_castle = False
        else:
            valid_castle = False

        return valid_castle
