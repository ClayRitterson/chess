class ValueLookup:

    piece_val_map= {
        'P':1,
        'B':2,
        'N':3,
        'R':4,
        'Q':5,
        'K':6
    }

    bw_val_map = {
        'w' :  1,
        'b' :  -1
    }

    def bw_to_system_val(self, bw_val):
     
        return ValueLookup.bw_val_map[bw_val]

    def systemPieceValueMap(self,piece_type_val):

        return ValueLookup.piece_val_map[piece_type_val]


        