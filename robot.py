class Robot: 

    def __init__(self, image, name, x,y): #Constructor - Sets variables.
        import pygame

        self.__image = image 
        self.__name = name 
        self.__points = 0 
        self.__locationX = x
        self.__locationY = y 


    def moveLeft(self, arena): #Change the location of the robot to make it move up
        self.__locationY -= 1
    def moveRight(self, arena):
        self.__locationY += 1
    def moveDown(self, arena):
        self.__locationX += 1
    def moveUp(self, arena):
        self.__locationX -= 1

    def returnLocationX(self):  #Return the X location of the bot
        return self.__locationX

    def returnLocationY(self):  #Return the Y location of the bot
        return self.__locationY

    def returnPoints(self):
        return self.__points

    def returnImage(self):  #returns image of the robot
        return self.__image

    def setlocationx(self, x):
        self.__locationX = x
 
    def setlocationy(self, y):
        self.__locationY = y

    def setPoints(self, val):
        self.__points = val
        return
bot = Robot("map.png", "barry", 10, 22)
