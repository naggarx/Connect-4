from board import Board
import time
import random
import numpy as np
import MiniMax as algo
import math
# GAME LINK
# http://kevinshannon.com/connect4/


def main():
    board = Board()
    time.sleep(5)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        # YOUR CODE GOES HERE
        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        random_column,minimaxscore = algo.minimax(game_board, 1, True)
        #print(random_column)
        board.select_column(random_column)
        time.sleep(5)


if __name__ == "__main__":
    main()
