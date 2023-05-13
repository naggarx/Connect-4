import numpy as np
def create_board():
    board = np.zeros((6,7))
    return board
board = create_board()


def drop(board , row , col , player):
    board[row][col] = player
def is_valid(board , col):
    return board[5][col] == 0
def get_next(board,col):
    for r in range(6) :
        if board[r][col] == 0:
            return r
def print_board(board):
    print(np.flip(board , 0));
EndOfGame = False
turn = 0
while not EndOfGame:
    #First Player
    if (turn == 0):
        pass
    #Second Player
    else:
        pass
    turn += 1
    turn = turn % 2
    