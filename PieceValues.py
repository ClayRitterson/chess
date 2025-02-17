class PieceValues:

    val_map= {
            'P':1,
            'B':2,
            'N':3,
            'R':4,
            'Q':5,
            'K':6
        }

    def systemValueMap(self,piece_type_val):

        return PieceValues.val_map[piece_type_val]