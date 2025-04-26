import PromotePiece as pp
import ValueLookup as vl

class SimulateMove:

    players = {
        -1 : 'b',
        1  : 'w'
    }

    bw_val_map = {
        'w' :  1,
        'b' :  -1
    }

    def __init__(self, p_sim_board, player_color, system_move) -> None:
        self.p_sim_board = p_sim_board
        self.player_color = player_color
        self.system_move = system_move
        self.en_passant = {
        1 :  None,
        -1 : None
        }

    # ------------------------------------------------------------------------
    def performSimulatedMove(self):

        # If non-King piece moved, update piece location
        moved_piece = self.p_sim_board.board[self.system_move[1]][self.system_move[0]]
        if abs(moved_piece.system_value) != 6:
            self.p_sim_board.piece_locations[self.player_color][moved_piece.piece_id] = [self.system_move[3], self.system_move[2]]

        # If King moved, update King location
        if abs(moved_piece.system_value) == 6:
            self.p_sim_board.king_locations[self.player_color] = [self.system_move[3], self.system_move[2]]
        elif abs(moved_piece.system_value) == 1:

            # Promote Pawn
            if self.system_move[3] == vl.ValueLookup().promote_map[self.player_color]:
                new_piece = pp.PromotePiece().main(self.player_color)
                moved_piece.system_value = (vl.ValueLookup().piece_val_map[new_piece])*SimulateMove.bw_val_map[self.player_color]
                moved_piece.display_value = f'{self.player_color}{new_piece}'
            
            # Set En Passant Viability
            elif abs(self.system_move[3] - self.system_move[1]) == 2:
                moved_piece.en_passant = True
                self.en_passant[SimulateMove.bw_val_map[self.player_color]] = [self.system_move[3], self.system_move[2]]
            
            # Perform En Passant Capture
            elif self.system_move[2] != self.system_move[0] and self.p_sim_board.board[self.system_move[3]][self.system_move[2]] == None:
                captured_piece = self.p_sim_board.board[self.system_move[1]][self.system_move[2]] # piece captured not where piece moved to!!
                captured_piece_id = captured_piece.piece_id
                self.p_sim_board.piece_locations[SimulateMove.players[SimulateMove.bw_val_map[self.player_color] * -1]].pop(captured_piece_id)
                self.p_sim_board.board[self.system_move[1]][self.system_move[2]] = None

        # Make actual move
        check_for_capture = self.p_sim_board.board[self.system_move[3]][self.system_move[2]]
        if check_for_capture != None:
            captured_piece = self.p_sim_board.board[self.system_move[3]][self.system_move[2]]
            captured_piece_id = captured_piece.piece_id
            self.p_sim_board.piece_locations[SimulateMove.players[SimulateMove.bw_val_map[self.player_color] * -1]].pop(captured_piece_id)
        self.p_sim_board.board[self.system_move[3]][self.system_move[2]] = self.p_sim_board.board[self.system_move[1]][self.system_move[0]]
        self.p_sim_board.board[self.system_move[1]][self.system_move[0]] = None

        # Used For Castling
        if moved_piece.system_value in [4,6] and moved_piece.has_moved == False:
            moved_piece.has_moved = True

        return self.p_sim_board



