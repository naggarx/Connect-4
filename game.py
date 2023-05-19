from board import Board
import time
import random
import numpy as np
import MiniMax as algo
import math
import GUI 

# GAME LINK
# http://kevinshannon.com/connect4/
class Game:
        def __init__(self):
            self.board = Board()
            self.algorithm = None
            self.difficulty = 1
        def Play(self):
            time.sleep(2)
            game_end = False
            while not game_end:
                (game_board, game_end) = self.board.get_game_grid()
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
                self.board.print_grid(game_board);
                # Insert here the action you want to perform based on the output of the algorithm
                # You can use the following function to select a column
                if self.algorithm == "Alpha":
                    random_column,minimaxscore = algo.alphamax(np.flip(new_board, 0), self.difficulty,-math.inf , math.inf, True)
                    print("alpha")
                else:
                    random_column,minimaxscore = algo.minimax(np.flip(new_board, 0), self.difficulty,True)
                    print("mini")
                print(random_column)
                self.board.select_column(random_column)
                time.sleep(2)

        

def main():
        game = Game()
        GUI.myGUI(game)
           
if __name__ == "__main__":
        main()
