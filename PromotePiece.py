import ValueLookup as vl

class PromotePiece:

    soft_break = vl.ValueLookup().soft_break
    player_names = vl.ValueLookup().player_names

    # ------------------------------------------------------------------------
    def __init__(self) -> None:
        pass

    # ------------------------------------------------------------------------
    def main(self, player_color):

        print(f"{PromotePiece.soft_break}\nPROMOTION CHOICES:\nQUEEN\nKNIGHT\nBISHOP\nROOK\n{PromotePiece.soft_break}")

        letter_val = ''
        valid_input = False
        while valid_input == False:
            input_move = input(f'{PromotePiece.soft_break}\nPLAYER {PromotePiece.player_names[player_color]}, PROMOTE PAWN TO: ')
            print(PromotePiece.soft_break)
            match input_move.lower():
                case 'queen':
                    letter_val = 'Q'
                    valid_input = True
                case 'knight':
                    letter_val = 'N'
                    valid_input = True
                case 'bishop':
                    letter_val = 'B'
                    valid_input = True
                case 'rook':
                    letter_val = 'R'
                    valid_input = True       
                case _:
                    pass       
        
        return letter_val