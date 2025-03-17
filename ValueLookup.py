class ValueLookup:

    def bw_to_system_val(self, bw_val):
        return_system_val = 0

        match bw_val:
            case 'w':
                return_system_val = 1
            case 'b':
                return_system_val = -1

        return return_system_val

    def systemPieceValueMap(self,piece_type_val):

        val_map= {
            'P':1,
            'B':2,
            'N':3,
            'R':4,
            'Q':5,
            'K':6
        }

        return val_map[piece_type_val]


        