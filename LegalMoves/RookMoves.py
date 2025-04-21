from LegalMoves import RBQ

class RookMoves(RBQ.RBQ):

    piece_value = 'R'

    # ------------------------------------------------------------------------
    def get_rbq_value(self):

        return RookMoves.piece_value

    # ------------------------------------------------------------------------    
    def findMoves(self):

        valid_move_index_list = self.findRBQmoves()

        return valid_move_index_list