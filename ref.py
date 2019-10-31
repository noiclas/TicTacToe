# ref.py implemented by Nic Arnaud (https://github.com/noiclas)

def check_win(player, board_l):
    return check_row(player, board_l) or \
           check_column(player, board_l) or \
           check_diagonal(player, board_l)

def check_row(player, board_l):
    for row in board_l:
        if row.count(player) == 3:
            return True
    return False

def check_column(player, board_l):
    for col in zip(*board_l):
        if col.count(player) == 3:
            return True
    return False

def check_diagonal(player, board_l):
    if (board_l[0][0] == board_l[1][1] == board_l[2][2] == player) or \
       (board_l[0][2] == board_l[1][1] == board_l[2][0] == player):
        return True
    return False
