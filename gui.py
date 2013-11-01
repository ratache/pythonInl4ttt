# -*- coding: cp1252 -*-
#tic tac toe mofo - per j -inl4
from Tkinter import *
from board import *


class GUI:
    def __init__(self):
        self.createApp = AppControl()
        self.__createGUI()#starts up the guiscript
        print 'GUI init ok'

    def __createGUI(self):
        self.__game = Tk()
        self.__game.wm_title("Tic-tac-toe-mofo!")
        self.__gameField = Frame(self.__game, padx=20, pady=20)
        #build window
        self.cr()
        self.__gameField.pack()
        
        
    def __handleClick(self, event):
        #Get click data
        grid_info = event.widget.grid_info()
        self.createApp.getTile(grid_info["row"], grid_info["column"])
        self.cr()

    def cr(self):
        #build gamebuttons
        gridSize = 3
        tick = 0
        gameBoard = self.createApp.board.getGameField()

        for row in range(gridSize):
            for col in range(gridSize):
                if gameBoard[tick] != "P" and gameBoard[tick] != "C" and tick <= 8:
                    b = Button(self.__gameField, width=5, bg="#0F0")
                    b.grid(row=row, column=col)
                    b.bind("<Button-1>", self.__handleClick)
                    tick += 1
                    print 1
                elif gameBoard[tick] == "P" and tick <= 8:
                    b = Button(self.__gameField, width=5, bg="#00F")
                    b.grid(row=row, column=col)
                    b.bind("<Button-1>", self.__unactive)
                    tick += 1
                    print 2
                elif gameBoard[tick] == "C" and tick <= 8:
                    b = Button(self.__gameField, width=5, bg="#F00")
                    b.grid(row=row, column=col)
                    b.bind("<Button-1>", self.__unactive)
                    tick += 1
                    print 3


    def __unactive(self, event):
        print"Inactive button"

    def run(self):
        print 'Application start'        
        self.__game.mainloop()

v = GUI()
v.run()
