from LegalMoves import KN

class KingMoves(KN.KN):

    piece_value = 'K'

    # ------------------------------------------------------------------------
    def get_kn_value(self):

        return KingMoves.piece_value

    # ------------------------------------------------------------------------
    def findMoves(self):

        valid_move_index_list = self.findKNmoves()

        return valid_move_index_list