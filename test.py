from board import Board
from ai import find_best_move, minimax

board_l = [["X", "X", "O"],
           ["O", " ", "X"],
           ["O", " ", "X"]]

my_board = Board(board_l, "O")

best_move = find_best_move(my_board, "O", 8)
for line in board_l:
    print(line)
print("The best move for O is:")
print(best_move)
