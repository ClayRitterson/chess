
import ValueLookup as vl
from LegalMoves import ValidMoves as vm
from CheckLogic import CheckForCheck as cfc

class CheckForCheckmate:

    players = vl.ValueLookup().players
    player_names = vl.ValueLookup().player_names
    game_break = vl.ValueLookup().game_break

    # ------------------------------------------------------------------------
    def __init__(self, cm_board, cm_player) -> None:
        self.cm_board = cm_board
        self.cm_player = cm_player

    # ------------------------------------------------------------------------
    def cfcm_main(self):

        cfcm_status = False

        player_check_obj = cfc.CheckForCheck(self.cm_board, None, CheckForCheckmate.players[self.cm_player])
        player_check_obj.check_main()

        # if player in check
        if player_check_obj.check_bool == True:
            check_mate_obj = self.checkForCheckmate()

            # if player in checkmate
            if check_mate_obj == True:
                winning_player = CheckForCheckmate.player_names[CheckForCheckmate.players[self.cm_player*-1]]
                print(f"""\n\n{CheckForCheckmate.game_break}\nCHECKMATE! PLAYER {winning_player} WINS!
                            GAME OVER...\n{CheckForCheckmate.game_break}\n""")
                cfcm_status =  True
        
        return cfcm_status

    # ------------------------------------------------------------------------
    def checkForCheckmate(self):

        checkmate_bool = True

        # Check King moves first
        player_color = CheckForCheckmate.players[self.cm_player]
        player_king_loc = self.cm_board.king_locations[player_color]
        checkmate_bool = self.iterCheckmate(player_king_loc)
        if checkmate_bool == False:
            return checkmate_bool

        # Iterate over all other pieces and check
        own_piece_dict = self.cm_board.piece_locations[player_color]
        own_piece_id_keys = list(own_piece_dict.keys())
        for pid in range(len(own_piece_id_keys)):
            player_piece_loc = own_piece_dict[own_piece_id_keys[pid]]
            checkmate_bool = self.iterCheckmate(player_piece_loc)
            if checkmate_bool == False:
                return checkmate_bool

        return checkmate_bool   

    # ------------------------------------------------------------------------
    def iterCheckmate(self, player_piece_loc):

        iterCheckmateBool = True

        legal_pid_moves = vm.ValidMoves(self.cm_board.board, 
                                        [player_piece_loc[1], 
                                        player_piece_loc[0]], 
                                        self.cm_player).getValidMoves()
        for lmp in range(len(legal_pid_moves)):
            check_piece_obj = cfc.CheckForCheck(self.cm_board, 
                                        [player_piece_loc[1], 
                                        player_piece_loc[0], 
                                        legal_pid_moves[lmp][1], 
                                        legal_pid_moves[lmp][0]], 
                                        CheckForCheckmate.players[self.cm_player])
            check_piece_obj.check_main()
            if check_piece_obj.check_bool == False:
                return check_piece_obj.check_bool
        
        return iterCheckmateBool