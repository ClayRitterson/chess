class KN:
    
    system_move_piece_index = {
    'K' : [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]],
    'N' : [[2, 1],[2, -1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
    }

    def __init__(self, system_move_data, current_player, game_board) -> None:
        self.system_move_data = system_move_data
        self.current_player = current_player
        self.game_board = game_board
        self.system_moves_static = KN.system_move_piece_index[self.get_kn_value()]
        self.valid_move_index_list = []

    def get_kn_value(self):

        return 
        
    def findKNmoves(self):

        start_position = [self.system_move_data[1], self.system_move_data[0]]

        for i in range(len(self.system_moves_static)):
            self.checkStaticMove(start_position[:], self.system_moves_static[i])

        return self.valid_move_index_list

    def checkStaticMove(self, current_position, move_values):
        
        current_position[0] += move_values[0]
        current_position[1] += move_values[1]
        
        # is square in bounds? 
        if all(0 <= x <= 7 for x in current_position) == True: 
            check_square = self.game_board[current_position[0]][current_position[1]]

            # is squre empty?
            if check_square == None:
                self.valid_move_index_list.append(current_position[:])
            
            # is square occupied by opponents piece?
            elif check_square.system_value * self.current_player < 0:
                self.valid_move_index_list.append(current_position[:])