import math
from copy import deepcopy
from CPUPlayer import CPUMoveGen as cpu_mg
from CPUPlayer import SimulateMove as sm
from CPUPlayer import EvalBoard as eb
import ValueLookup as vl
import time

DEPTH = vl.ValueLookup().DEPTH

bw_val_map = {
    'w' :  1,
    'b' :  -1
}

# ------------------------------------------------------------------------
def get_cpu_move(best_color, best_board):

    traverse_moves = cpu_mg.CPUMoveGen(best_color, best_board).main()
    best_move = None
    max_eval = -math.inf
    for move in traverse_moves:
        deep_fb_board = deepcopy(best_board)
        deep_fb_board = sm.SimulateMove(deep_fb_board, best_color, move.move_spec).performSimulatedMove()
        if best_color == 'w':
            next_best_color = 'b'
        elif best_color == 'b':
            next_best_color = 'w'
        eval = minimax(0, deep_fb_board, next_best_color, alpha=-math.inf, beta=math.inf, maximize=False )
        if eval > max_eval:
            max_eval = eval
            best_move = move

    return best_move

# ------------------------------------------------------------------------
def minimax(depth, sim_board, player_color, alpha, beta, maximize):
    #print('player_color=',player_color, 'maximize=',maximize, 'depth=',depth)
    #time.sleep(1)

    '''
    cm_bool = False ## CheckForCheckMate #TODO
    if cm_bool == True:
        if maximize == True:
            return -math.inf
        elif maximize == False:
            return math.inf
    '''
    if depth == DEPTH: 
        board_score = eb.Evalboard(sim_board, bw_val_map[player_color], player_color).main()
        return board_score

    ## if len of traverse_moves == 0 , more efficient way to determine checkmate?? #TODO
    traverse_moves = cpu_mg.CPUMoveGen(player_color, sim_board).main()
    
    if len(traverse_moves) == 0:
        if maximize == True:
            return math.inf
        elif maximize == False:
            return -math.inf

    if maximize == True:
        max_eval = -math.inf
        for cur_move in traverse_moves:
            deep_board = deepcopy(sim_board)
            sim_obj = sm.SimulateMove(deep_board, player_color, cur_move.move_spec)
            next_board = sim_obj.performSimulatedMove()
            if player_color == 'w':
                next_player_color = 'b'
            elif player_color == 'b':
                next_player_color = 'w'
            eval = minimax(depth + 1, next_board, next_player_color, alpha, beta, maximize = False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    elif maximize == False:
        min_eval = math.inf
        for cur_move in traverse_moves:
            deep_board = deepcopy(sim_board)
            sim_obj = sm.SimulateMove(deep_board, player_color, cur_move.move_spec)
            next_board = sim_obj.performSimulatedMove()
            if player_color == 'w':
                next_player_color = 'b'
            elif player_color == 'b':
                next_player_color = 'w'
            eval = minimax(depth + 1, next_board, next_player_color, alpha, beta, maximize = True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

