from LegalMoves import ValidMoves as vm
from CheckLogic import CheckForCheck as cfc
from CPUPlayer import MoveNode as mn

class CPUMoveGen:

    bw_val_map = {
        'w' :  1,
        'b' :  -1
    }

    # ------------------------------------------------------------------------
    def __init__(self, player_color, move_gen_board) -> None:
        self.move_gen_board = move_gen_board
        self.player_color = player_color
        self.return_moves = []
        self.move_id_counter = 0

    # ------------------------------------------------------------------------
    def main(self):
        
        #player_king_loc = self.move_gen_board.king_locations[CPUMoveGen.bw_val_map[self.player_color]]
        player_king_loc = self.move_gen_board.king_locations[self.player_color]
        self.getMoves(player_king_loc)

        # Iterate over all other pieces and check
        #own_piece_dict = self.move_gen_board.piece_locations[CPUMoveGen.bw_val_map[self.player_color]]
        own_piece_dict = self.move_gen_board.piece_locations[self.player_color]
        own_piece_id_keys = list(own_piece_dict.keys())
        for pid in range(len(own_piece_id_keys)):
            player_piece_loc = own_piece_dict[own_piece_id_keys[pid]]
            self.getMoves(player_piece_loc)
        
        return self.return_moves

    # ------------------------------------------------------------------------
    def getMoves(self, player_piece_loc):

        legal_pid_moves = vm.ValidMoves(self.move_gen_board.board, 
                                        [player_piece_loc[1], 
                                        player_piece_loc[0]], 
                                        CPUMoveGen.bw_val_map[self.player_color]).getValidMoves()
        for lmp in range(len(legal_pid_moves)):

            move_details = [player_piece_loc[1], 
                            player_piece_loc[0], 
                            legal_pid_moves[lmp][1], 
                            legal_pid_moves[lmp][0]]
                                               
            check_obj = cfc.CheckForCheck(self.move_gen_board,
                                        move_details, 
                                        self.player_color)
            check_obj.check_main()
            if check_obj.check_bool == False:
                self.move_id_counter += 1
                self.score = 0
                node_obj = mn.MoveNode(self.move_id_counter, self.score, move_details)
                self.return_moves.append(node_obj)