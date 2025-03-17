import ValueLookup as vl

class CheckRBQ:

    system_move_piece_index_RBQ = {
        'R':[[1, 0],[-1, 0],[0, -1],[0, 1]],
        'B':[[1, 1],[-1, -1],[1, -1],[-1, 1]],
        'Q':[[1, 0],[-1, 0],[0, -1],[0, 1],[1, 1],[-1, -1],[1, -1],[-1, 1]]
    }


    # check wrapper
    # --------------------------------------------------------------------
    def check_RBQ_wrapper(self):

        self.check_RBQ_lines('R')
        if self.check_bool == True:
            return
        self.check_RBQ_lines('B')
        if self.check_bool == True:
            return

    # Check RBQ Logic
    # --------------------------------------------------------------------
    def check_RBQ_lines(self, line_type):

        lines_to_check = CheckRBQ.system_move_piece_index_RBQ[line_type]

        for i in range(len(lines_to_check)):
            self.check_current_RBQ_line(lines_to_check[i], line_type)
            if self.check_bool == True:
                return

    def check_current_RBQ_line(self, current_line_direction, line_type):

        rbq_lookup_value = vl.ValueLookup().systemPieceValueMap(line_type)

        check_rbq_pos = self.current_player_king_location[:]
        ## Continue path
        continue_path = True
        current_position = [check_rbq_pos[0], check_rbq_pos[1]]
        while continue_path == True:
            
            current_position[0] += current_line_direction[0]
            current_position[1] += current_line_direction[1]

            keep_checking = self.checkCurrentSquare(current_position, rbq_lookup_value)
            if self.check_bool == True:
                return

            if keep_checking == False:
                continue_path = False
        

    def checkCurrentSquare(self, current_position, rbq_lookup_value):

            keep_checking = False

            # is square in bounds?
            if all(0 <= x <= 7 for x in current_position) == True: 

                check_square = self.copy_of_board.board[current_position[0]][current_position[1]]
                # is square in empty?
                if check_square == None: 
                    keep_checking = True
                else: 
                    keep_checking = False
                    # is square occupied by opposing player's piece that is either Q or [R/B]?

                    if check_square.system_value * self.system_player < 0 and abs(check_square.system_value) in [self.queen_value, rbq_lookup_value]:
                        self.check_bool = True
                        return

            return keep_checking
