import GameSetup.InitGame as ig
from Display import BoardPrinter as bp
from Display import DisplayBoard as db
from CheckLogic import CheckForCheckmate as cfcm
import PlayerInput as pi
import PromotePiece as pp
import ValueLookup as vl
import EvalBoard as eb

class Game:

    actual_board = None
    continue_game = True
    line_break = vl.ValueLookup().line_break
    soft_break = vl.ValueLookup().soft_break
    players = vl.ValueLookup().players
    player_names = vl.ValueLookup().player_names
    column_index = vl.ValueLookup().column_index
    bw_val_map = vl.ValueLookup().bw_val_map

    current_player = 0

    en_passant = {
        1 :  None,
        -1 : None
    }

    # ------------------------------------------------------------------------
    def runGame(self):

        Game.en_passant = {
        1 :  None,
        -1 : None
        }

        Game.actual_board = ig.InitGame().gameSetup()

        Game.current_player = 1
        while Game.continue_game:

            return_game_status = self.makeMove(Game.players[Game.current_player])
            if return_game_status == False:
                Game.continue_game = False

            Game.current_player = Game.current_player * -1

    # ------------------------------------------------------------------------
    def showBoard(self):
        
        bp.BoardPrinter(Game.actual_board.board).printBoard()
        bp.BoardPrinter(Game.actual_board.board, display_or_system='system').printBoard()

    # ------------------------------------------------------------------------
    def reset_passant(self, player_color):

        # Reset En Passant (Only valid for 1 turn)
        if Game.en_passant[Game.bw_val_map[player_color]] != None:
            un_passant_piece = Game.actual_board.board[Game.en_passant[Game.bw_val_map[player_color]][0]][Game.en_passant[Game.bw_val_map[player_color]][1]]
            Game.en_passant[Game.bw_val_map[player_color]] = None
            if un_passant_piece != None:
                un_passant_piece.en_passant = False

    # ------------------------------------------------------------------------
    def performMove(self, player_color, system_move):

        # If non-King piece moved, update piece location
        moved_piece = Game.actual_board.board[system_move[1]][system_move[0]]
        if abs(moved_piece.system_value) != 6:
            Game.actual_board.piece_locations[player_color][moved_piece.piece_id] = [system_move[3], system_move[2]]

        # If King moved, update King location
        if abs(moved_piece.system_value) == 6:
            Game.actual_board.king_locations[player_color] = [system_move[3], system_move[2]]
        elif abs(moved_piece.system_value) == 1:

            # Promote Pawn
            if system_move[3] == vl.ValueLookup().promote_map[player_color]:
                new_piece = pp.PromotePiece().main(player_color)
                moved_piece.system_value = (vl.ValueLookup().piece_val_map[new_piece])*Game.bw_val_map[player_color]
                moved_piece.display_value = f'{player_color}{new_piece}'
            
            # Set En Passant Viability
            elif abs(system_move[3] - system_move[1]) == 2:
                moved_piece.en_passant = True
                Game.en_passant[Game.bw_val_map[player_color]] = [system_move[3], system_move[2]]
            
            # Perform En Passant Capture
            elif system_move[2] != system_move[0] and Game.actual_board.board[system_move[3]][system_move[2]] == None:
                captured_piece = Game.actual_board.board[system_move[1]][system_move[2]] # piece captured not where piece moved to!!
                captured_piece_id = captured_piece.piece_id
                Game.actual_board.piece_locations[Game.players[Game.current_player * -1]].pop(captured_piece_id)
                Game.actual_board.board[system_move[1]][system_move[2]] = None
                
        # Make actual move
        check_for_capture = Game.actual_board.board[system_move[3]][system_move[2]]
        if check_for_capture != None:
            captured_piece = Game.actual_board.board[system_move[3]][system_move[2]]
            captured_piece_id = captured_piece.piece_id
            Game.actual_board.piece_locations[Game.players[Game.current_player * -1]].pop(captured_piece_id)
        Game.actual_board.board[system_move[3]][system_move[2]] = Game.actual_board.board[system_move[1]][system_move[0]]
        Game.actual_board.board[system_move[1]][system_move[0]] = None

        # Used For Castling
        if moved_piece.system_value in [4,6] and moved_piece.has_moved == False:
            moved_piece.has_moved = True

    # ------------------------------------------------------------------------
    def makeMove(self, player_color):

        print(f'\n{Game.line_break}\nCURRENT TURN: {Game.player_names[Game.players[Game.current_player]]}')

        # Board Strength Evaluation for current player
        board_score = eb.Evalboard(Game.actual_board, Game.bw_val_map[player_color], player_color).main()
        print("BOARD SCORE = ", board_score)

        db.DisplayBoard(Game.actual_board.board, player_color).display_main()

        # CheckForCheckmate upon the start of each turn
        checkmate_status = cfcm.CheckForCheckmate(Game.actual_board, Game.current_player).cfcm_main()
        if checkmate_status == True:
            return False

        # Reset Player En Passant Status
        self.reset_passant(player_color)

        valid_input=False

        # Loop until valid move provided. Perform Move within
        while valid_input==False:
            
            # Get player move data
            invalid_move, msg, castle_status, system_move = pi.PlayerInput(Game.actual_board, Game.current_player).get_player_move(player_color)
            
            if invalid_move:
                print(f'{Game.soft_break}\nINVALID MOVE, {msg}\n{Game.soft_break}\n')
            elif castle_status == False:
                self.performMove(player_color, system_move)
                valid_input = True
            elif castle_status == True:
                valid_input = True
        
        return True



        
        





