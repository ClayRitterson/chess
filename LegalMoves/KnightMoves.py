from LegalMoves import KN

class KnightMoves(KN.KN):

    piece_value = 'N'

    # ------------------------------------------------------------------------
    def get_kn_value(self):

        return KnightMoves.piece_value

    # ------------------------------------------------------------------------   
    def findMoves(self):

        valid_move_index_list = self.findKNmoves()

        return valid_move_index_list