from math import inf
from board import Board

def minimax(board, player, max_depth, current_depth):
    if board.is_game_over() or current_depth == max_depth:
        return board.evaluate(player), None

    best_move = None
    best_score = -inf if board.current_player == player else inf

    for move in board.get_moves():
        new_board = board.make_move(move)
        current_score, current_move = minimax(new_board, player, max_depth, current_depth+1)

        if board.current_player == player:
            if current_score > best_score:
                best_score = current_score
                best_move = move
        else:
            if current_score < best_score:
                best_score = current_score
                best_move = move

    return best_score, best_move

def find_best_move(board, player, max_depth):
    score, move = minimax(board, player, max_depth, 0)
    return move
