from copy import deepcopy
from CPUPlayer import MoveSelector as ms

class CPUMover:

    # ------------------------------------------------------------------------
    def __init__(self, cpu_color, cpu_board) -> None:
        self.cpu_color = cpu_color
        self.cpu_board = cpu_board

    # ------------------------------------------------------------------------
    def main(self):

        board_copy = deepcopy(self.cpu_board)
        best_move_node = ms.get_cpu_move(self.cpu_color, board_copy)     

        return best_move_node