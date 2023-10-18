from tkinter import *
import random

w=Tk()

colors = ["red", "green", "blue", "black", "white", "yellow"]

def change_color():
    color = random.choice(colors)
    w.configure(bg=color)

Button(w,text="Change Color", command=change_color).pack()

w.mainloop()