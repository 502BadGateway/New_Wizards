from entity import entity
class treasure(entity):

    def __init__(self, x, y, points, name, val, image):
        entity.__init__(self, name, val, image)

        self.__x = x
        self.__y = y

        self.__arenaValue = val

        self.__points = points 

        self.__collected = False
        

    def returnPoints(self):
        return self.__points

    def returnCollected(self):
        return self.__collected
   
    def setCollected(self, val):
        self.__collected = val 
        return

    def returnLocationX(self):
        return self.__x

    def returnLocationY(self):
        return self.__y


    def getArenaValue(self):
        return self.__arenaValue

