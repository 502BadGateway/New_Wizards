#Class file for trap class. Should inherit from entity class.
from entity import entity

class trap(entity):

    def __init__(self, x, y, points, name, val, image):
        entity.__init__(self, name, val, image) #Call the base class constructor. This is because this constructor should be extending not replacing functionality in entity._init__. 
                                         #See here for information on this: Paragraph 6  https://docs.python.org/2/tutorial/classes.html#inheritance
        self.__locationX = x
        self.__locationY = y

    def returnLocationX(self):
        return self.__locationX

    def returnLocationY(self):
        return self.__locationY
