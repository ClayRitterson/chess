
"""
------------------------------------------------------------------------------------------------------------
## IDEAS
------------------------------------------------------------------------------------------------------------
1) Change adjustments based on phase of game (ie: early, middle, end)
   game phase determined by total piece value thresholds & num pieces?
2) King safety -- get points for castling, having protection around the king
3) Bishop lines -- clear lines good for bishops -- to intensive to check so maybe count # of pawns of own on same color sq as a negative?
4) Check -- add big score adjustment if opponent is in check -- may lead to some forced lines than computer cannot see
5) Checkmate -- the goal of the game, so provide "infinite" score for Checkmate -- basically any value greater than 
   what can be achieved otherwise
------------------------------------------------------------------------------------------------------------
"""

class Evalboard:

    players = {
        -1 : 'b',
        1  : 'w'
    }

    piece_start_row_index = {
        1 : 0,
        -1 : 7
    }

    pawn_start_row_index = {
        1 : 1,
        -1 : 6
    }

    piece_score_value_map= {
        1 :  10,  # Pawn
        2 :  35,  # Bishop
        3 :  35,  # Knight
        4 :  53,  # Rook 
        5 :  100, # Queen
        6 :  0    # King
    }

    directions = [-1,1]

    center_value_map = {
        0 : {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0},
        1 : {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0},
        2 : {0 : 0, 1 : 0, 2 : 1, 3 : 1, 4 : 1, 5 : 1, 6 : 0, 7 : 0},
        3 : {0 : 0, 1 : 0, 2 : 1, 3 : 2, 4 : 2, 5 : 1, 6 : 0, 7 : 0},
        4 : {0 : 0, 1 : 0, 2 : 1, 3 : 2, 4 : 2, 5 : 1, 6 : 0, 7 : 0},
        5 : {0 : 0, 1 : 0, 2 : 1, 3 : 1, 4 : 1, 5 : 1, 6 : 0, 7 : 0},
        6 : {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0},
        7 : {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0},
    }

    # ------------------------------------------------------------------------
    def __init__(self, in_eval_board, current_player, player_color) -> None:
        self.in_eval_board = in_eval_board
        self.board_obj = in_eval_board.board
        self.current_player = current_player
        self.player_color = player_color

        # Scores
        # ------------------------
        self.combined_score = 0

        # Component Scoring
        # ------------------------
        self.value_score = 0
        #self.position_score = 0
        #self.king_safety_score = 0
        self.pawn_file_score = 0
        self.center_score = 0
        self.development_score = 0
        self.pawn_structure_score = 0
        self.pawn_advacement_score = 0
        self.pawn_files = {
            1  : {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0},
            -1 : {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
        }

        # Component Weights
        # ------------------------        
        self.value_adjustment = 2
        #self.position_adjustment = 1
        #self.king_safety_adjustment = 1
        self.pawn_file_adjustment = 0.5
        self.center_adjustment = 2
        self.development_adjustment = 3
        self.pawn_advacement_adjustment = 1
        self.pawn_structure_adjustment = 1
        self.opponent_adjustment = 1

    # ------------------------------------------------------------------------
    def main(self):

        own_piece_map = self.in_eval_board.piece_locations[Evalboard.players[self.current_player]]
        own_scores = self.eval(own_piece_map, 1)
        self.apply_scores(own_scores)

        opp_piece_map = self.in_eval_board.piece_locations[Evalboard.players[self.current_player * -1]]
        opp_scores = self.eval(opp_piece_map, -1)
        self.apply_scores(opp_scores, opp=True)
        
        # combined_score
        self.combined_score += self.value_score
        self.combined_score += self.pawn_advacement_score
        self.combined_score += self.pawn_file_score
        self.combined_score += self.center_score
        self.combined_score += self.development_score
        self.combined_score += self.pawn_structure_score

        return self.combined_score

    # ------------------------------------------------------------------------
    def apply_scores(self, scores, opp=False):
        
        if opp == True:
            opp_adj = self.opponent_adjustment
            score_direction = -1
        else:
            opp_adj = 1
            score_direction = 1

        #eval_value_score
        self.value_score += score_direction * (scores[0] * opp_adj * self.value_adjustment)
        #eval_pawn_advancement_score
        self.pawn_advacement_score += score_direction * (scores[1] * opp_adj * self.pawn_advacement_adjustment)
        #eval_pawn_file_score
        self.pawn_file_score += score_direction * (scores[2] * opp_adj * self.pawn_file_adjustment)
        #eval_center_score
        self.center_score += score_direction * (scores[3] * opp_adj * self.center_adjustment)
        #eval_development_score
        self.development_score += score_direction * (scores[4] * opp_adj * self.development_adjustment)
        #eval_pawn_structure_score
        self.pawn_structure_score += score_direction * (scores[4] * opp_adj * self.pawn_structure_adjustment)

    # ------------------------------------------------------------------------
    def eval(self, piece_map, multiplier):

        eval_player = self.current_player * multiplier
        eval_value_score = 0
        eval_pawn_advancement_score = 0
        eval_pawn_file_score = 0
        eval_center_score = 0
        eval_development_score = 0
        eval_pawn_structure_score = 0

        piece_start_row = Evalboard.piece_start_row_index[self.current_player * multiplier]
        pawn_start_row = Evalboard.pawn_start_row_index[self.current_player * multiplier]

        piece_ids = list(piece_map.keys())

        for i in range(len(piece_ids)):
            piece_location = piece_map[piece_ids[i]]
            piece_from_loc = self.board_obj[piece_location[0]][piece_location[1]]
            system_value = piece_from_loc.system_value
            
            # Piece values based on piece type
            eval_value_score += (Evalboard.piece_score_value_map[abs(system_value)])

            # Add to center score based on center map
            eval_center_score += Evalboard.center_value_map[piece_location[0]][piece_location[1]]

            match abs(system_value):
                # ------------------------   
                case 1: # Pawn
                    eval_pawn_advancement_score += abs(piece_location[0] - pawn_start_row)
                    self.pawn_files[eval_player][piece_location[1]] = 1 # Pawn exists on file

                    # check pawn structure
                    row_behind = piece_location[0] - eval_player
                    for dir in range(2):
                        try:
                            check_file = piece_location[1] + Evalboard.directions[dir]
                            if check_file >= 0:
                                check_sq = self.board_obj[row_behind][piece_location[1] + Evalboard.directions[dir]]
                                if check_sq.system_value * eval_player == 1:
                                    eval_pawn_structure_score +=1
                        except:
                            pass

                    pass
                # ------------------------   
                case 2: # Bishop
                    if piece_location[0] != piece_start_row:
                        eval_development_score += 1 
                    pass
                # ------------------------   
                case 3: # Knight
                    if piece_location[0] != piece_start_row:
                        eval_development_score += 1 
                    pass
                # ------------------------   
                case 4: # Rook
                    pass
                # ------------------------   
                case 5: # Queen
                    if piece_location[0] != piece_start_row:
                        eval_development_score += 1 
                    pass
                # ------------------------   
                case _: # Default
                    pass

        # tally pawn file score:
        for i in range(8):
            eval_pawn_file_score += self.pawn_files[eval_player][i]

        return [
        eval_value_score,
        eval_pawn_advancement_score,
        eval_pawn_file_score,
        eval_center_score,
        eval_development_score,
        eval_pawn_structure_score
        ]


