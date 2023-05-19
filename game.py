from board import Board
import time
import random
import numpy as np
import MiniMax as algo
import math
from ctypes.wintypes import RGB
import tkinter as tk
from turtle import color, left
from ctypes.wintypes import RGB
import tkinter as tk
from turtle import color, left
# GAME LINK
# http://kevinshannon.com/connect4/

algorithm = None
difficulty = 1
class myGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect 4")
        self.root.geometry("900x600")   
       
        self.root.configure(bg=self.rgb_to_hex((0, 100, 100)))

        self.label = tk.Label(self.root, text="Hello Player", font=('Arial', 20))
        self.label.pack(padx=10, pady=10)
        self.label.config(fg='white') 
        self.label.config(bg=self.rgb_to_hex((0, 50, 100))) 
         
        self.label1 = tk.Label(self.root, text="Select Algorithm:", font=('Arial', 15))
        self.label1.pack(padx=10, pady=10)
        self.label1.config(fg='green')

        self.chech_State = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Alpha", font=('Arial', 10), variable=self.chech_State)
        self.check.pack(padx=10, pady=10)

        self.chech_State1 = tk.IntVar()

        self.check2 = tk.Checkbutton(self.root, text="minMax", font=('Arial', 10), variable=self.chech_State1)
        self.check2.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Press", font=('Arial', 10), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        self.button.config(fg='red')

 
        self.label2 = tk.Label(self.root, text="Select Difficulty:", font=('Arial', 15))
        self.label2.pack(padx=10, pady=10)
        self.label2.config(fg='green')

        self.chech_State2= tk.IntVar()
        self.check3 = tk.Checkbutton(self.root, text="1", font=('Arial', 10), variable=self.chech_State2)
        self.check3.pack(padx=10, pady=10)

        self.chech_State3 = tk.IntVar()
        self.check4 = tk.Checkbutton(self.root, text="2", font=('Arial', 10), variable=self.chech_State3)
        self.check4.pack(padx=10, pady=10)

        self.chech_State4 = tk.IntVar()
        self.check5 = tk.Checkbutton(self.root, text="3", font=('Arial', 10), variable=self.chech_State4)
        self.check5.pack(padx=10, pady=10)

        self.chech_State5 = tk.IntVar()
        self.check6 = tk.Checkbutton(self.root, text="4", font=('Arial', 10), variable=self.chech_State5)
        self.check6.pack(padx=10, pady=10)

        self.chech_State6 = tk.IntVar()
        self.check7 = tk.Checkbutton(self.root, text="5", font=('Arial', 10), variable=self.chech_State6)
        self.check7.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Press", font=('Arial', 10), command=self.show_message1)
        self.button.pack(padx=10, pady=10)
        self.button.config(fg='red')
        self.root.mainloop()

    def show_message(self):
        algorithm = None
        if self.chech_State.get() == 1:
            algorithm = "Alpha"
        elif self.chech_State1.get() == 1:
            algorithm = "MiniMax"
        if algorithm:
            return algorithm
        else:
            print("Please select an algorithm.")

    def show_message1(self):
        difficulty  = 0
        if self.chech_State2.get() == 1:
           difficulty = 1
        elif self.chech_State3.get() == 1:
           difficulty = 2
        elif self.chech_State4.get() == 1:
           difficulty = 3
        elif self.chech_State5.get() == 1:
           difficulty = 4
        elif self.chech_State6.get() == 1:
           difficulty = 5     
        if difficulty:
            pass
        else:
            print("Please select an algorithm.") 
    def rgb_to_hex(self, rgb): 
        return '#{:02x}{:02x}{:02x}'.format(*[int(x) for x in rgb])        
myGUI()
def main():
        board = Board()
        game_end = False
        time.sleep(2)
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
            if algorithm == "Alpha":
                random_column,minimaxscore = algo.alphamax(np.flip(new_board, 0), difficulty,-math.inf , math.inf, True)
                print("alpha")
            else:
                random_column,minimaxscore = algo.minimax(np.flip(new_board, 0), difficulty,True)
                print("mini")
            print(random_column)
            board.select_column(random_column)
        
            time.sleep(2)

        


if __name__ == "__main__":
        main()
