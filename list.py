# -*- coding: cp1252 -*-
#tic tac toe mofo - per j -inl4
from Tkinter import *

root = Tk()

def callback(event):
    print "clicked at", event.x, event.y 

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()