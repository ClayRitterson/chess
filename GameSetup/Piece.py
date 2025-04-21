import ValueLookup as vl
import copy

class Piece:

    piece_counter = 0

    # ------------------------------------------------------------------------
    def __init__(self, black_or_white, piece_type):
        self.black_or_white = black_or_white
        self.piece_type = piece_type
        self.system_value = 0
        self.display_value = ''
        self.has_moved = False
        self.en_passant = False
        self.piece_id = 0

    # ------------------------------------------------------------------------
    def setValues(self):

        self.setDisplayValue()
        self.setSystemValue()
        self.setIDValue()

    # ------------------------------------------------------------------------
    def setIDValue(self):

        Piece.piece_counter += 1
        self.piece_id = copy.copy(Piece.piece_counter)

    # ------------------------------------------------------------------------
    def setDisplayValue(self):

        self.display_value = self.black_or_white + self.piece_type

    # ------------------------------------------------------------------------
    def setSystemValue(self):

        self.system_value = vl.ValueLookup().systemPieceValueMap(self.piece_type)

        if self.black_or_white == 'b':
            self.system_value = self.system_value * -1
