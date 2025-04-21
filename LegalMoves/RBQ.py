class RBQ:

    system_move_piece_index = {
        'R':[[1, 0],[-1, 0],[0, -1],[0, 1]],
        'B':[[1, 1],[-1, -1],[1, -1],[-1, 1]],
        'Q':[[1, 0],[-1, 0],[0, -1],[0, 1],[1, 1],[-1, -1],[1, -1],[-1, 1]]
    }

    # ------------------------------------------------------------------------
    def __init__(self, system_move_data, current_player, game_board) -> None:
        self.system_move_data = system_move_data
        self.current_player = current_player
        self.game_board = game_board
        self.system_directions = RBQ.system_move_piece_index[self.get_rbq_value()]
        self.valid_move_index_list = []

    # ------------------------------------------------------------------------
    def get_rbq_value(self):

        return None

    # ------------------------------------------------------------------------
    def checkCurrentSquare(self, current_position):

        keep_checking = False

        # is square in bounds?
        if all(0 <= x <= 7 for x in current_position) == True: 

            check_square = self.game_board[current_position[0]][current_position[1]]
            # is square in empty?
            if check_square == None: 
                self.valid_move_index_list.append(current_position[:])
                keep_checking = True
            else: 
                keep_checking = False
                # is square occupied by opposing player's piece?
                if check_square.system_value * self.current_player < 0: 
                    self.valid_move_index_list.append(current_position[:])

        return keep_checking

    # ------------------------------------------------------------------------
    def checkDirection(self, path_index):

        continue_path = True
        current_position = [self.system_move_data[1], self.system_move_data[0]]
        current_directions = self.system_directions[path_index]
        while continue_path == True:
            
            current_position[0] += current_directions[0]
            current_position[1] += current_directions[1]

            keep_checking = self.checkCurrentSquare(current_position)

            if keep_checking == False:
                continue_path = False

    # ------------------------------------------------------------------------ 
    def findRBQmoves(self):
        
        for i in range(len(self.system_directions)):
            self.checkDirection(i)
            

        return self.valid_move_index_list