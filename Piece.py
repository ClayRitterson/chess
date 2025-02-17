import PieceValues as pv


class Piece:

    def __init__(self, black_or_white, piece_type):
        self.black_or_white = black_or_white
        self.piece_type = piece_type
        self.system_value = 0
        self.display_value = ''

    def set_values(self):

        self.set_display_value()
        self.set_system_value()

    def set_display_value(self):

        self.display_value = self.black_or_white + self.piece_type

    def set_system_value(self):

        self.system_value = pv.PieceValues().systemValueMap(self.piece_type)

        if self.black_or_white == 'b':
            self.system_value = self.system_value * -1