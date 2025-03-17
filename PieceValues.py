class PieceValues:

    def systemValueMap(self,piece_type_val):

        val_map= {
            'P':1,
            'B':2,
            'N':3,
            'R':4,
            'Q':5,
            'K':6
        }

        return PieceValues.val_map[piece_type_val]