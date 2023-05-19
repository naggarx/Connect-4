from ctypes.wintypes import RGB
import tkinter as tk
from turtle import color, left
from ctypes.wintypes import RGB
import tkinter as tk
from turtle import color, left
class myGUI:
    def __init__(self,game):
        self.game = game
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
            self.game.algorithm = algorithm
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
            self.game.difficulty = difficulty
            self.game.Play()
        else:
            print("Please select an algorithm.") 
    def rgb_to_hex(self, rgb): 
        return '#{:02x}{:02x}{:02x}'.format(*[int(x) for x in rgb])        
