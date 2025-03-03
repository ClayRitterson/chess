from LegalMoves import RookMoves as lrm 
from LegalMoves import PawnMoves as lpm 
from LegalMoves import BishopMoves as lbm 
from LegalMoves import KnightMoves as lnm 
from LegalMoves import QueenMoves as lqm 
from LegalMoves import KingMoves as lkm 

class ValidMoves:

    pieceMoveFactory = {
        1: lpm.PawnMoves,
        2: lbm.BishopMoves,
        3: lnm.KnightMoves,
        4: lrm.RookMoves,
        5: lqm.QueenMoves,
        6: lkm.KingMoves
    }

    def __init__(self, game_board, system_move_data, current_player) -> None:
        self.game_board = game_board
        self.system_move_data = system_move_data
        self.current_player = current_player


    def getValidMoves(self):

        piece_to_move = self.game_board[self.system_move_data[1]][self.system_move_data[0]]

        move_obj = ValidMoves.pieceMoveFactory[abs(piece_to_move.system_value)](self.system_move_data, self.current_player, self.game_board)

        valid_move_list = move_obj.findMoves()

        return valid_move_list


