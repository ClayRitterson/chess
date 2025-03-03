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

        #print(piece_to_move.system_value, " --> ", piece_to_move.display_value)

        move_obj = ValidMoves.pieceMoveFactory[abs(piece_to_move.system_value)](self.system_move_data, self.current_player, self.game_board)

        valid_move_list = move_obj.findMoves()

        return valid_move_list

        """
        # Testing
        # ----------------------------------------------
        print("current_player: ", self.current_player)
        print("system_move_data: ", self.system_move_data)
   
        print("game_board")
        for i in range(len(self.game_board)):
            game_row = ''
            for k in range(len(self.game_board)):
                game_row += f'|{str(i)}:{str(k)}'
                '''
                if self.game_board[i][k] == None:
                    game_row += ' 0'
                else:
                    if self.game_board[i][k].system_value > 0:
                        game_row += ' '
                    game_row += str(self.game_board[i][k].system_value)
               '''
            print(game_row)
        # ----------------------------------------------
        """



