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
        self.root.geometry("900x700")   
       
        self.root.configure(bg="#45458B")

        #self.label = tk.Label(self.root, text="Hello Player", font=('Arial', 20))
        #self.label.pack(padx=10, pady=10)
        #self.label.config(fg='white') 
        #self.label.config(bg=self.rgb_to_hex((0, 50, 100))) 
         
        self.label1 = tk.Label(self.root, text="Select Algorithm:", font=('Calibri', 15 , 'bold'), bg="#45458B")
        self.label1.pack(padx=2, pady=10)
        self.label1.config(fg='white')

        self.chech_State = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Alpha", font=('Calibri', 12 , 'bold'), variable=self.chech_State , bg="#45458B")
        self.check.pack(padx=10, pady=10)

        self.chech_State1 = tk.IntVar()

        self.check2 = tk.Checkbutton(self.root, text="MiniMax", font=('Calibri', 12 , 'bold'), variable=self.chech_State1 , bg="#45458B")
        self.check2.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Press", font=('Calibri', 12 , 'bold'), command=self.show_message , bg="#45458B")
        self.button.pack(padx=10, pady=10)
        self.button.config(fg='white')

 
        self.label2 = tk.Label(self.root, text="Select Difficulty:", font=('Calibri', 15, 'bold') , bg="#45458B")
        self.label2.pack(padx=10, pady=10)
        self.label2.config(fg='white')

        self.chech_State2= tk.IntVar()
        self.check3 = tk.Checkbutton(self.root, text="1", font=('Calibri', 12 , 'bold'), variable=self.chech_State2, bg="#45458B")
        self.check3.pack(padx=10, pady=10)

        self.chech_State3 = tk.IntVar()
        self.check4 = tk.Checkbutton(self.root, text="2", font=('Calibri', 12 , 'bold'), variable=self.chech_State3, bg="#45458B")
        self.check4.pack(padx=10, pady=10)

        self.chech_State4 = tk.IntVar()
        self.check5 = tk.Checkbutton(self.root, text="3", font=('Calibri', 12 , 'bold'), variable=self.chech_State4, bg="#45458B")
        self.check5.pack(padx=10, pady=10)

        self.chech_State5 = tk.IntVar()
        self.check6 = tk.Checkbutton(self.root, text="4", font=('Calibri', 12 , 'bold'), variable=self.chech_State5, bg="#45458B")
        self.check6.pack(padx=10, pady=10)

        self.chech_State6 = tk.IntVar()
        self.check7 = tk.Checkbutton(self.root, text="5", font=('Calibri', 12 , 'bold'), variable=self.chech_State6, bg="#45458B")
        self.check7.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Press", font=('Calibri', 12 , 'bold'), command=self.show_message1, bg="#45458B")
        self.button.pack(padx=10, pady=10)
        self.button.config(fg='white')
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
