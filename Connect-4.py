import numpy as np
def create_board():
    board = np.zeros((6,7))
    return board
board = create_board()
#NEGO
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
def winning_move(board , player):
    #Check Horiz.
    for c in range(7-3):
        for r in range (6):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True
    #Check Vertical
    for c in range(7):
        for r in range (6-3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True
    #Check diagonal 1
    for c in range(7-3):
        for r in range (6-3):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True
    #Check diagonal 2
    for c in range(7-3):
        for r in range (3,6):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True
    
    
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
    