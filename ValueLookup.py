class ValueLookup:

    line_break = '*' * 35
    soft_break = '-' * 35
    game_break = '#' * 35

    players = {
        -1 : 'b',
        1  : 'w'
    }

    player_names =  {

        'b': 'BLACK',
        'w': 'WHITE'
    }

    column_index = {
        'A':0,
        'B':1,
        'C':2,
        'D':3,
        'E':4,
        'F':5,
        'G':6,
        'H':7
    }

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

    promote_map = {
        'w' : 7,
        'b' : 0
    }

    castle_map = {
        'w' : 0,
        'b' : 7
    }

    def bw_to_system_val(self, bw_val):
     
        return ValueLookup.bw_val_map[bw_val]

    def systemPieceValueMap(self,piece_type_val):

        return ValueLookup.piece_val_map[piece_type_val]


        