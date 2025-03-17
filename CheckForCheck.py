
import copy
import ValueLookup as vl

class CheckForCheck:

    system_move_piece_index_KN = {
        'K' : [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]],
        'N' : [[2, 1],[2, -1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
    }

    system_move_piece_index_RBQ = {
        'R':[[1, 0],[-1, 0],[0, -1],[0, 1]],
        'B':[[1, 1],[-1, -1],[1, -1],[-1, 1]],
        'Q':[[1, 0],[-1, 0],[0, -1],[0, 1],[1, 1],[-1, -1],[1, -1],[-1, 1]]
    }

    def __init__(self, game_board, system_move_data, current_player) -> None:
        self.system_move_data = system_move_data
        self.current_player = current_player
        self.copy_of_board = copy.deepcopy(game_board)
        self.current_player_king_location = [None, None]
        self.current_player_king_piece = None
        self.check_bool = False
        self.system_player = vl.ValueLookup().bw_to_system_val(self.current_player)
        self.queen_value = vl.ValueLookup().systemPieceValueMap('Q')
        self.pawn_value = vl.ValueLookup().systemPieceValueMap('P')

    def check_main(self):
        
        # --------------------------------------------------------------------
        # Simulate Move
        # --------------------------------------------------------------------

        # If King moved, update King location
        moved_piece = self.copy_of_board.board[self.system_move_data[1]][self.system_move_data[0]]
        if abs(moved_piece.system_value) == 6:
            self.copy_of_board.king_locations[self.current_player] = [self.system_move_data[3], self.system_move_data[2]]

        # Update board to reflect desired move
        self.copy_of_board.board[self.system_move_data[3]][self.system_move_data[2]] = self.copy_of_board.board[self.system_move_data[1]][self.system_move_data[0]]
        self.copy_of_board.board[self.system_move_data[1]][self.system_move_data[0]] = None

        # Set King Piece and Location
        self.current_player_king_location = [self.copy_of_board.king_locations[self.current_player][0], self.copy_of_board.king_locations[self.current_player][1]]
        self.current_player_king_piece = self.copy_of_board.board[self.current_player_king_location[0]][self.current_player_king_location[1]]


        # --------------------------------------------------------------------
        # Check for all forms of Check from King POV
        # --------------------------------------------------------------------

        # Check for Pawn Check
        self.check_pawn_wrapper()
        if self.check_bool == True:
            return

        # Check for KN Check
        self.check_KN_wrapper()
        if self.check_bool == True:
            return
        
        # Check for RBQ Check
        self.check_RBQ_wrapper()
        if self.check_bool == True:
            return


    # Check type wrappers
    # --------------------------------------------------------------------
    def check_pawn_wrapper(self):

        self.check_pawn_check(1)   # Check Right
        if self.check_bool == True:
            return
        self.check_pawn_check(-1)   # Check Left
        if self.check_bool == True:
            return

    def check_KN_wrapper(self):

        self.check_KN_check('K')
        if self.check_bool == True:
            return
        self.check_KN_check('N')
        if self.check_bool == True:
            return

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

        lines_to_check = CheckForCheck.system_move_piece_index_RBQ[line_type]

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


    # Check KN Logic
    # --------------------------------------------------------------------
    def check_KN_check(self, kn_val):

        kn_move_list = CheckForCheck.system_move_piece_index_KN[kn_val]
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
