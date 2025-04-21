
import copy
import ValueLookup as vl
from CheckLogic import CheckPawn as cp
from CheckLogic import CheckRBQ as crbq
from CheckLogic import CheckKN as ckn
from Display import BoardPrinter as bp 

class CheckForCheck(cp.CheckPawn, crbq.CheckRBQ, ckn.CheckKN):

    # ------------------------------------------------------------------------
    def __init__(self, game_board, system_move_data, current_player) -> None:
        self.system_move_data = system_move_data
        self.current_player = current_player
        self.copy_of_board = copy.deepcopy(game_board)
        self.current_player_king_location = [None, None]
        self.current_player_king_piece = None
        self.check_bool = False
        self.system_player = vl.ValueLookup().bw_to_system_val(self.current_player)
        self.queen_value = vl.ValueLookup().systemPieceValueMap('Q')
        self.pawn_value = vl.ValueLookup().systemPieceValueMap('P')

    # ------------------------------------------------------------------------
    def check_main(self):
        
        # --------------------------------------------------------------------
        # Simulate Move
        # --------------------------------------------------------------------
        if self.system_move_data != None:
            # If King moved, update King location
            moved_piece = self.copy_of_board.board[self.system_move_data[1]][self.system_move_data[0]]
            if abs(moved_piece.system_value) == 6:
                self.copy_of_board.king_locations[self.current_player] = [self.system_move_data[3], self.system_move_data[2]]

            # Update board to reflect desired move
            self.copy_of_board.board[self.system_move_data[3]][self.system_move_data[2]] = self.copy_of_board.board[self.system_move_data[1]][self.system_move_data[0]]
            self.copy_of_board.board[self.system_move_data[1]][self.system_move_data[0]] = None

        # Set King Piece and Location
        self.current_player_king_location = [self.copy_of_board.king_locations[self.current_player][0], self.copy_of_board.king_locations[self.current_player][1]]
        self.current_player_king_piece = self.copy_of_board.board[self.current_player_king_location[0]][self.current_player_king_location[1]]

        # --------------------------------------------------------------------
        # Check for all forms of Check from King POV
        # --------------------------------------------------------------------

        # Check for Pawn Check
        self.check_pawn_wrapper()
        if self.check_bool == True:
            return

        # Check for KN Check
        self.check_KN_wrapper()
        if self.check_bool == True:
            return
        
        # Check for RBQ Check
        self.check_RBQ_wrapper()
        if self.check_bool == True:
            return