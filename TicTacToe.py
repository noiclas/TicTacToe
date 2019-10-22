import os
import time

def play_game():
    board = [["1","2","3"],
             ["4","5","6"],
             ["7","8","9"]]
    player = "X"
    game_over = False

    os.system("cls" if os.name == "nt" else "clear")
    computer_playing = check_game_mode()

    while not game_over:
        show_board(board)
        print(player+"\'s turn")
        if player == "X" and computer_playing:
            input_ = computer_input(board)
            time.sleep(2)
            play(player, input_, board)
        else:
            input_ = player_input(player, board)
            play(player, input_, board)
        if check_win(player, board):
            show_board(board)
            print(player+" wins!")
            game_over = not game_over
        elif check_tie(board):
            print("Tie game.")
            game_over = not game_over
        player = "X" if player == "O" else "O"
        
def show_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    terminal_width = os.get_terminal_size().columns
    print("")
    counter = 0
    for row in board:
        print("   |   |   ".center(terminal_width))
        print((("%s | %s | %s") % (row[0], row[1], row[2])).center(terminal_width))
        if counter == 2:
            print("   |   |   ".center(terminal_width))
        else:
            print("___|___|___".center(terminal_width))
        counter += 1

def check_win(player, board):
    return check_row(player, board) or \
           check_column(player, board) or \
           check_diagonal(player, board)

def check_tie(board):
    return check_win("O", board) and check_win("X", board)

def check_row(player, board):
    for row in board:
        if row.count(player) == 3:
            return True
    return False

def check_column(player, board):
    for col in zip(*board):
        if col.count(player) == 3:
            return True
    return False

def check_diagonal(player, board):
    if (board[0][0] == board[1][1] == board[2][2] == player) or \
       (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False

def player_input(player, board):
    valid = False
    while not valid:
        position = input("Choose a position (1-9): ")
        if position in [str(i) for i in range(1,10)]:
                position = int(position) - 1
                if board[position//3][position%3] in [str(i) for i in range(1,10)]:
                    return position
                    valid = True
def play(player, position, board):
    board[position//3][position%3] = player

def computer_input(board):
    position = 3
    print("Choose a position (1-9): ", end = "")

    print(position)
    return 1

def check_game_mode():
    valid = False
    while not valid:
        game_mode = input("Play against computer or other player (c/p)?: ").strip().lower()
        if game_mode in ["computer", "c", "player", "p"]:
            if game_mode == "computer" or game_mode == "c":
                return True
            else:
                return False

play_game()
