import GameSetup.InitGame as ig
from Display import BoardPrinter as bp
from Display import DisplayBoard as db
from LegalMoves import ValidMoves as vm
from LegalMoves import CheckCastle as cc
from CheckLogic import CheckForCheck as cfc 
import PromotePiece as pp
import ValueLookup as vl
import sys

class Game:

    actual_board = None
    continue_game = True

    line_break = vl.ValueLookup().line_break
    players = vl.ValueLookup().players
    player_names = vl.ValueLookup().player_names
    column_index = vl.ValueLookup().column_index
    bw_val_map = vl.ValueLookup().bw_val_map

    current_player = 0

    en_passant = {
        1 :  None,
        -1 : None
    }

    def runGame(self):

        Game.en_passant = {
        1 :  None,
        -1 : None
        }

        Game.actual_board = ig.InitGame().gameSetup()

        Game.current_player = 1
        while Game.continue_game:

            self.makeMove(Game.players[Game.current_player])
            
            Game.current_player = Game.current_player * -1
            
            # until checkmate or quit

    def showBoard(self):
        
        bp.BoardPrinter(Game.actual_board.board).printBoard()
        bp.BoardPrinter(Game.actual_board.board, display_or_system='system').printBoard()


    def checkInput(self, check_sys_move):

        invalid_move = False
        msg = ''
        
        check_input = True

        while check_input == True:
            if Game.actual_board.board[check_sys_move[1]][check_sys_move[0]] == None:
                invalid_move = True
                msg = "EMPTY SPACE"
                return invalid_move, msg

            if all(0 <= x <= 7 for x in check_sys_move) == False:
                invalid_move = True
                msg = "NOT WITHIN BOARD PARAMETERS"
                return invalid_move, msg

            if Game.actual_board.board[check_sys_move[1]][check_sys_move[0]].system_value * Game.current_player < 0:
                invalid_move = True
                msg = "CANNOT MOVE OPPONENTS PIECE"
                return invalid_move, msg
            check_input = False

        legal_moves = vm.ValidMoves(Game.actual_board.board, check_sys_move, Game.current_player).getValidMoves()
        if [check_sys_move[3],check_sys_move[2]] not in legal_moves:
            invalid_move = True
            msg = "ILLEGAL MOVE"
            return invalid_move, msg

        # IF CheckForCheck == True: (if Player in Check after move)
        #   invalid_move = True
        check_obj = cfc.CheckForCheck(Game.actual_board, check_sys_move, Game.players[Game.current_player])
        check_obj.check_main()

        if check_obj.check_bool == True:
            invalid_move = True
            msg = "PLAYER IN CHECK"
            return invalid_move, msg

        return invalid_move, msg

    def getMoveInput(self, player_color):

        input_move = input(f'{Game.line_break}\nPLAYER {Game.player_names[player_color]}, ENTER MOVE: ')
        print(Game.line_break)

        if input_move == 'quit':
            sys.exit()

        return input_move

    def evalMoveInput(self, user_move):

        try:
            system_move = [ 
                            Game.column_index[user_move[0].upper()], 
                            int(user_move[1])-1, 
                            Game.column_index[user_move[2].upper()], 
                            int(user_move[3])-1
                            ]
        except:
            system_move = [-1,-1,-1,-1]

        return system_move

    
    def makeMove(self, player_color):

        db.DisplayBoard(Game.actual_board.board, player_color).display_main()

        # Reset En Passant (Only valid for 1 turn)
        if Game.en_passant[Game.bw_val_map[player_color]] != None:
            un_passant_piece = Game.actual_board.board[Game.en_passant[Game.bw_val_map[player_color]][0]][Game.en_passant[Game.bw_val_map[player_color]][1]]
            Game.en_passant[Game.bw_val_map[player_color]] = None
            if un_passant_piece != None:
                un_passant_piece.en_passant = False

        valid_input=False

        while valid_input==False:
            
            user_move = self.getMoveInput(player_color)

            castle_status = False
            if user_move.upper() == 'CASTLE LEFT' or user_move.upper() == 'CASTLE RIGHT':
                castle_status = cc.CheckCastle(user_move.upper(), player_color, Game.actual_board).main()
                if castle_status == True:
                    invalid_move = False
                    valid_input = True
                else:
                    invalid_move = True
                    msg = 'INVALID CASTLE'
            else:
                system_move = self.evalMoveInput(user_move)
                invalid_move, msg = self.checkInput(system_move) 
            
            if invalid_move:
                print(f'{Game.line_break}\nINVAID MOVE, {msg}\n{Game.line_break}\n')
            elif castle_status == False:

                # If King moved, update King location
                moved_piece = Game.actual_board.board[system_move[1]][system_move[0]]
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
                        Game.actual_board.board[system_move[1]][system_move[2]] = None
                        
                # Make actual move
                Game.actual_board.board[system_move[3]][system_move[2]] = Game.actual_board.board[system_move[1]][system_move[0]]
                Game.actual_board.board[system_move[1]][system_move[0]] = None

                # Used For Castling
                if moved_piece.system_value in [4,6] and moved_piece.has_moved == False:
                    moved_piece.has_moved = True

                valid_input = True




