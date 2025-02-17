import Piece as p


class GameBoard:

    board_size = 8

    def __init__(self):
        self.board = []

    def initializeBoard(self): # Creates and fills new board

        self.buildGrid()
        self.fillBoard()

    def buildGrid(self): # Creates empty grid

        self.board = [[[] for x in range(GameBoard.board_size)] for x in range(GameBoard.board_size)]

    def fillBoard(self): # Fills entire board with piece objects in starting positions

        self.fillPawns('w')
        self.fillPieces('w')
        self.fillPawns('b')
        self.fillPieces('b')

    def fillRow(self, row_index, row_list, bw):
        for i in range(len(self.board[row_index])):
            new_piece = p.Piece(bw, row_list[i])
            new_piece.set_values()
            self.board[row_index][i] = new_piece

    def fillPawns(self, bw): # Fills a row with pawns

        pawnRowIndexMap = {
            'w':1,
            'b':6
        }

        self.fillRow(pawnRowIndexMap[bw], ['P' for x in range(8)], bw)

    def fillPieces(self, bw): # Fills a row of minor and major pieces

        piecePositionIndex = ['R','N','B','Q','K','B','N','R']

        if bw == 'b':
            piecePositionIndex.reverse()

        pieceRowIndexMap = {
            'w':0,
            'b':7
        }

        self.fillRow(pieceRowIndexMap[bw], piecePositionIndex, bw)
        