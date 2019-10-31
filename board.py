from ref import check_win
from copy import deepcopy

class Board:
    def __init__(self, board_l, current_player):
        self.board_l = board_l
        self.current_player = current_player

    def get_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board_l[i][j] in [str(i) for i in range(1,9)]:
                    moves.append((i,j))
        return moves

    def make_move(self, move):
        board_l_copy = deepcopy(self.board_l)
        board_l_copy[move[0]][move[1]] = self.current_player
        new_player = "X" if self.current_player == "O" else "O"
        return Board(board_l_copy, new_player)

    def evaluate(self,player):
        if check_win(player, self.board_l):
            score = 1 if player != self.current_player else -1
        else:
            score = 0
        return score

    def is_game_over(self):
        state = self.get_moves == [] or check_win("X", self.board_l) or check_win("O", self.board_l)
        return state
