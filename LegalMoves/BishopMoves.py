from LegalMoves import RBQ

class BishopMoves(RBQ.RBQ):

    piece_value = 'B'

    # ------------------------------------------------------------------------
    def get_rbq_value(self):

        return BishopMoves.piece_value

    # ------------------------------------------------------------------------  
    def findMoves(self):

        valid_move_index_list = self.findRBQmoves()

        return valid_move_index_list