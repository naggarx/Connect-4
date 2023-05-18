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
    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        # FOR DEBUG PURPOSES
        #board.print_grid(game_board)
        # Copy the content of game_board to new_board
        #print(game_board)
        new_board = np.zeros((6, 7))
        # Copy the content of game_board to new_board
        for i in range(6):
            for j in range(7):
                if game_board[i][j] == 0:
                    new_board[i][j] = 0
                elif game_board[i][j] == 1:
                    new_board[i][j] = 1
                elif game_board[i][j] == 2:
                    new_board[i][j] = 2
        # YOUR CODE GOES HERE
        print(new_board)
        board.print_grid(game_board);
        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        random_column,minimaxscore = algo.alphamax(np.flip(new_board, 0), 4,-math.inf , math.inf, True)
        print(random_column)
        board.select_column(random_column)
      
        time.sleep(2)


if __name__ == "__main__":
    main()
