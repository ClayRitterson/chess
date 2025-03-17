import ValueLookup as vl

class CheckKN:


    system_move_piece_index_KN = {
        'K' : [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]],
        'N' : [[2, 1],[2, -1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
    }


    # check wrapper
    # --------------------------------------------------------------------
    def check_KN_wrapper(self):

        self.check_KN_check('K')
        if self.check_bool == True:
            return
        self.check_KN_check('N')
        if self.check_bool == True:
            return

    # Check KN Logic
    # --------------------------------------------------------------------
    def check_KN_check(self, kn_val):

        kn_move_list = CheckKN.system_move_piece_index_KN[kn_val]
        lookup_value = vl.ValueLookup().systemPieceValueMap(kn_val)

        for i in range(len(kn_move_list)):
            self.checkStaticMoveKN(self.current_player_king_location[:], kn_move_list[i], lookup_value)

    def checkStaticMoveKN(self, current_position, move_values, lookup_value):
        
        current_position[0] += move_values[0]
        current_position[1] += move_values[1]
        
        # is square in bounds? 
        if all(0 <= x <= 7 for x in current_position) == True: 
            check_square = self.copy_of_board.board[current_position[0]][current_position[1]]

            # is square occupied by opponents piece and that piece is a [K/N]?
            if check_square != None:      
                if check_square.system_value * self.system_player < 0 and abs(check_square.system_value) == lookup_value: 
                    self.check_bool = True
                    return
