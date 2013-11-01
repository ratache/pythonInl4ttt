# -*- coding: cp1252 -*-
#tic tac toe mofo - per j -inl4


class AppControl:
    #This class instantiates the board and players
    def __init__(self):
        self.board = Board()
        self.__ai = Ai()

    def getTile(self, tileX, tileY):
        number = self.board.getAction(tileX, tileY)
        self.board.chosenTile(number, "P")
        self.getCpuTile()

    def getCpuTile(self):
        number = self.__ai.iterateBoard(self.board.getGameField())
        self.board.chosenTile(number, "C")
        
class Board:
    #This class represents the gameboard
    def __init__(self):
        self.__GameField = [0,1,2,
                          3,4,5,
                          6,7,8]
        print "Board ready"

    def getGameField(self):
        return self.__GameField

    def chosenTile(self, number, player):
        for num in self.__GameField:
            if(num == number):
                self.__GameField[number] = player
                print self.__GameField

    def getAction(self,row,col):
        if row == '0' and col == '0':
                return 0
        elif row == '0' and col == '1':
                return 1
        elif row == '0' and col == '2':
                return 2
        elif row == '1' and col == '0':
                return 3
        elif row == '1' and col == '1':
                return 4
        elif row == '1' and col == '2':
                return 5
        elif row == '2' and col == '0':
                return 6
        elif row == '2' and col == '1':
                return 7
        elif row == '2' and col == '2':
                return 8

class Ai:
    #Task: choose cpu tile
    def __init__(self):
        print "Ai instance ready"
        self.__twoFlag = False

    def iterateBoard(self, gameField):
        if self.__twoFlag == False:
            if 4 in gameField:
                return 4
            elif gameField[5] != "P" and gameField[5] != "C" and gameField[4] == "C":
                self.__twoFlag = True
                return 5
            elif gameField[3] != "P" and gameField[3] != "C" and gameField[4] == "C":
                self.__twoFlag = True
                return 3
            elif gameField[1] != "P" and gameField[1] != "C" and gameField[4] == "C":
                self.__twoFlag = True
                return 1
            elif gameField[7] != "P" and gameField[7] != "C" and gameField[4] == "C":
                self.__twoFlag = True
                return 7
        
        if self.__twoFlag == True:
            index = gameField.index("C")
            print "in method " + str(index)
            if gameField[index+1] == "C" and index < 7:
                #Checks for horizontal options
                if index == 6 and gameField[8] != "P" and gameField[8] != "C":
                    print "row2"
                    return 8
                elif index == 0 and gameField[index+2] != "C" and gameField[index+2] != "P":
                    print "row0"
                    return index + 2
                elif index == 3 and gameField[index+2] != "C" and gameField[index+2] != "P":
                    print "row1"
                    return index + 2
                elif index == 1 and gameField[index+1] == "C" and gameField[index-1] != "C" and gameField[index-1] != "P":
                    print "complete row 0"
                    return 0
                elif index == 4 and gameField[index+1] == "C" and gameField[index-1] != "C" and gameField[index-1] != "P":
                    print "complete row 1"
                    return 3
                elif index == 7 and gameField[index+1] == "C" and gameField[index-1] != "C" and gameField[index-1] != "P":
                    print "complete row 2"
                    return 6

                    


        


#END