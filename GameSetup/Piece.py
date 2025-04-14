import ValueLookup as vl


class Piece:

    def __init__(self, black_or_white, piece_type):
        self.black_or_white = black_or_white
        self.piece_type = piece_type
        self.system_value = 0
        self.display_value = ''
        self.has_moved = False
        self.en_passant = False

    def setValues(self):

        self.setDisplayValue()
        self.setSystemValue()

    def setDisplayValue(self):

        self.display_value = self.black_or_white + self.piece_type

    def setSystemValue(self):

        self.system_value = vl.ValueLookup().systemPieceValueMap(self.piece_type)

        if self.black_or_white == 'b':
            self.system_value = self.system_value * -1
