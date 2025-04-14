import ValueLookup as vl

class PromotePiece:

    line_break = vl.ValueLookup().line_break
    player_names = vl.ValueLookup().player_names

    def __init__(self) -> None:
        pass

    def main(self, player_color):

        print(f"{PromotePiece.line_break}\nPROMOTION CHOICES:\nQUEEN\nKNIGHT\nBISHOP\nROOK\n{PromotePiece.line_break}")

        letter_val = ''
        valid_input = False
        while valid_input == False:
            input_move = input(f'{PromotePiece.line_break}\nPLAYER {PromotePiece.player_names[player_color]}, PROMOTE PAWN TO: ')
            print(PromotePiece.line_break)
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