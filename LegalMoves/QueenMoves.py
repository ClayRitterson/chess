from LegalMoves import RBQ

class QueenMoves(RBQ.RBQ):

    piece_value = 'Q'

    # ------------------------------------------------------------------------
    def get_rbq_value(self):

        return QueenMoves.piece_value

    # ------------------------------------------------------------------------   
    def findMoves(self):

        valid_move_index_list = self.findRBQmoves()

        return valid_move_index_list