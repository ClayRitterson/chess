

class CheckPawn:

    # check wrapper
    # --------------------------------------------------------------------
    def check_pawn_wrapper(self):

        self.check_pawn_check(1)   # Check Right
        if self.check_bool == True:
            return
        self.check_pawn_check(-1)   # Check Left
        if self.check_bool == True:
            return

    # Check Pawn Logic
    # --------------------------------------------------------------------
    def check_pawn_check(self, lateral_direction):

        check_pawn_pos = self.current_player_king_location[:]
        
        check_pawn_pos[0] += self.system_player # One row "forward" depending on b/w 
        check_pawn_pos[1] += lateral_direction # check left or right 

        # is square in bounds? 
        if all(0 <= x <= 7 for x in check_pawn_pos) == True: 

            check_square = self.copy_of_board.board[check_pawn_pos[0]][check_pawn_pos[1]]

            # is square occupied by opposing player's piece and that piece is a pawn?
            if check_square != None:
                if check_square.system_value * self.system_player < 0 and abs(check_square.system_value) == self.pawn_value:
                    self.check_bool = True
                    return
