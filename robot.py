class Robot: 

    def __init__(self, image, name, x,y): #Constructor - Sets variables.
        import pygame

        self.__image = image 
        self.__name = name 
        self.__points = 0 
        self.__locationX = x
        self.__locationY = y 


    def moveUp(self, arena): #Change the location of the robot to make it move up
        self.__locationY -= 1
        arena.put(self.__locationX, self.__locationY-1, 5)
    def moveDown(self, arena):
        self.__locationY += 1
        arena.put(self.__locationX, self.__locationY+1, 5)
    def moveLeft(self, arena):
        self.__locationX += 1
        arena.put(self.__locationX-1, self.__locationY,5)
    def moveRight(self, arena):
        self.__locationX += 1
        arena.put(self.__locationX+1, self.__locationY,5)

    def returnLocationX(self):  #Return the X location of the bot
        return self.__locationX

    def returnLocationY(self):  #Return the Y location of the bot
        return self.__locationY

    def returnPoints(self):
        return self.__points

    def returnImage(self):  #returns image of the robot
        return self.__image



bot = Robot("map.png", "barry", 10, 22)
