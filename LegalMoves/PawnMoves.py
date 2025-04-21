
class PawnMoves:

    pawn_start_row = {
        1  : 1,  # white pawns start on row_index 1
        -1 : 6 # black pawns start on row index 6
    }

    # ------------------------------------------------------------------------
    def __init__(self, system_move_data, current_player, game_board) -> None:
        self.system_move_data = system_move_data
        self.current_player = current_player
        self.game_board = game_board
        self.valid_move_index_list = []

    # ------------------------------------------------------------------------
    def findMoves(self):

        start_position = [self.system_move_data[1], self.system_move_data[0]]

        # one forward space empty
        one_forward_empty_bool = self.checkForward(start_position[:], 1)

        # two space move on initial move
        if PawnMoves.pawn_start_row[self.current_player] == self.system_move_data[1]: # Pawn is on start row
            if one_forward_empty_bool == True:
                two_forward_empty_bool = self.checkForward(start_position[:], 2)

        # diagonal captures
        self.checkDiagCaptures(start_position[:], 1)   # Check Right
        self.checkDiagCaptures(start_position[:], -1)  # Check Left

        #TODO
        # ------------------------------------------
        # en passant

        return self.valid_move_index_list

    # ------------------------------------------------------------------------
    def checkDiagCaptures(self, current_position, lateral_direction):

        current_position[0] += self.current_player # One row "forward" depending on b/w 
        current_position[1] += lateral_direction # check left or right 

        # is square in bounds? 
        if all(0 <= x <= 7 for x in current_position) == True: 

            check_square = self.game_board[current_position[0]][current_position[1]]

            # is square occupied by opposing player's piece or en_passant is valid?
            if check_square != None:
                if check_square.system_value * self.current_player < 0: 
                    self.valid_move_index_list.append(current_position[:])
            if 0 <= current_position[0] + (self.current_player * -1) <= 7:
                en_passant_squre = self.game_board[current_position[0] + (self.current_player * -1)][current_position[1]]
                if en_passant_squre != None:
                    if en_passant_squre.system_value * self.current_player < 0 and en_passant_squre.en_passant == True:
                            self.valid_move_index_list.append(current_position[:])

    # ------------------------------------------------------------------------
    def checkForward(self, current_position, mult):

        current_position[0] += (self.current_player * mult) # One row "forward" depending on b/w 

        empty_sq = False
        # is square in bounds? probably always true for pawn, 
        # otherwise would have been promoted / always valid from start_row
        if all(0 <= x <= 7 for x in current_position) == True: 

            check_square = self.game_board[current_position[0]][current_position[1]]
            # is square in empty?
            if check_square == None: 
                self.valid_move_index_list.append(current_position[:])
                empty_sq = True
        
        return empty_sq



    

