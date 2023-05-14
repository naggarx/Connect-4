import numpy as np
import pygame
import sys
import math

BLUE = (0, 0, 255)


def create_board():
    board = np.zeros((6, 7))
    return board


board = create_board()
pygame.init()
SQUARESIZE = 100
width = 7 * SQUARESIZE
height = 7 * SQUARESIZE

size = (width, height)
radius = int(SQUARESIZE / 2 - 5)
screen = pygame.display.set_mode(size)


# NEGO
# BTATES
def drop(board, row, col, player):
    board[row][col] = player


def is_valid(board, col):
    return board[5][col] == 0


def get_next(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r


def winning_move(board, player):
    # Check Horiz.
    for c in range(7 - 3):
        for r in range(6):
            if board[r][c] == player and board[r][c + 1] == player and board[r][c + 2] == player and board[r][
                c + 3] == player:
                return True
    # Check Vertical
    for c in range(7):
        for r in range(6 - 3):
            if board[r][c] == player and board[r + 1][c] == player and board[r + 2][c] == player and board[r + 3][
                c] == player:
                return True
    # Check diagonal 1
    for c in range(7 - 3):
        for r in range(6 - 3):
            if board[r][c] == player and board[r - 1][c + 1] == player and board[r - 2][c + 2] == player and \
                    board[r - 3][c + 3] == player:
                return True
    # Check diagonal 2
    for c in range(7 - 3):
        for r in range(3, 6):
            if board[r][c] == player and board[r + 1][c + 1] == player and board[r + 2][c + 2] == player and \
                    board[r + 3][c + 3] == player:
                return True


def draw_board(board):
    for c in range(7):
        for r in range(6):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, (0, 0, 0), (
            c * SQUARESIZE + int(SQUARESIZE / 2), r * SQUARESIZE + SQUARESIZE + int(SQUARESIZE / 2)), radius)

    for c in range(7):
        for r in range(6):
            if board[r][c] == 1:
                pygame.draw.circle(screen, (255, 0, 0), height - ( c * SQUARESIZE + int(SQUARESIZE / 2), r * SQUARESIZE + int(SQUARESIZE / 2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, (255, 255, 0), height - ( c * SQUARESIZE + int(SQUARESIZE / 2), r * SQUARESIZE + SQUARESIZE + int(SQUARESIZE / 2)), radius)
    pygame.display.update()


EndOfGame = False
turn = 0
while not EndOfGame:
    # First Player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if (turn == 0):
            pass
        # Second Player
        else:
            pass
        turn += 1
        draw_board(board)
        turn = turn % 2