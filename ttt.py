import os
from time import sleep
from ref import check_win
from ai import find_best_move
from board import Board
from random import choice

def play_game():
    board = [["1","2","3"],
             ["4","5","6"],
             ["7","8","9"]]
    player = "X"
    game_over = False

    os.system("cls" if os.name == "nt" else "clear")
    computer_playing = check_game_mode()
    turn = 0

    while not game_over:
        show_board(board)
        print(player+"\'s turn")
        if player == "X" and computer_playing:
            input_ = computer_input(board, turn)
            sleep(2)
            play(player, input_, board)
        else:
            input_ = player_input(player, board)
            play(player, input_, board)
        if check_win(player, board):
            show_board(board)
            print(player+" wins!")
            game_over = not game_over
        elif check_tie(board) and turn == 8:
            show_board(board)
            print("Tie game.")
            game_over = not game_over

        player = "X" if player == "O" else "O"
        turn +=1

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

def check_tie(board):
    return not check_win("O", board) and not check_win("X", board)

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

def computer_input(board, turn):
    if turn == 0:
        return choice([0, 2, 6, 8])
    else:
        b_obj = Board(board, "X")
        move = find_best_move(b_obj, "X", 8)
        return 3*move[0] + move[1]

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
