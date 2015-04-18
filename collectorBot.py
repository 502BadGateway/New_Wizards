from robot import Robot
import time
import random
#Landmark1 - London
#Landmark2 - Paris
#Landmark3 - Johnasaburgg
#Landmark4 - Tokyo
#Landmark5 - New York
#Landmark6 - Trap

class collectorBot(Robot):      #Class for the collector robot. Inherits from the super class robot.
    def __init__(self, arena, wishList, treasureList, x, y):
        Robot.__init__(self,"ASSETS/car.png","Barry",x, y)
    
        self.__wishlist = set(wishList)#Define with wishlist and inventory varS
        self.__inventory = [] 
        self.__treasureList = treasureList 
        self.targetX = 0
        self.targetY = 0
        self.incCount = 0

    def retInventory(self):
        return self.__inventory
    def treasureCheck(self, arena, treasureList): #checks for treasures around this location. TODO Should make sure that Phil knows what order this funtion expects the treasures in.
        wishlist = treasureList #Cos who knows where the actual wish list is meant to be coming from.
        collected = False
        tcollected = None

        treasure = treasureList[0]

        if collected == True:
            return 
        if treasure.getName() == treasureList[0].getName():
            if self.returnLocationX() -2 <= treasure.returnLocationY() <= self.returnLocationX()+2 and self.returnLocationY()-2 <= treasure.returnLocationX() <=  self.returnLocationY()+2: #If we are, then see if they're in our wishlist
                print "found treasure"
                self.__inventory.append(treasure)       #If so then add them to the inventory
                self.setPoints(1)                     #And add to the score
                treasure.setCollected(True)
                collected = True
                tcollected = treasure
                self.incCount += 1
            
    
        return collected, tcollected

    def trapCheck(self, arena, trapLandmark6): #this is a trap check which works in a similar way as the treasure check
        for items in wishlist:
            if collected == True:
                break
            if treasure.getName() == items.getName():
                if self.returnLocationX() -2 <= treasure.returnLocationX() <= self.returnLocationX()+2 and self.returnLocationY()-2 <= treasure.returnLocationY() <=  self.returnLocationY()+2: #If we are, then see if they're in our wishlist
                    print "You have come across a trap!"
                    self.__inventory.pop()
                    self.__points -= 1



    def updateLocation(self, city, arena, bot, target):
        print "Update Location"
        self.targetX = target[0]
        self.targetY = target[1]


        moved = False


        if bot.returnLocationY() > self.targetX:
            print bot.returnLocationY() , self.targetX
            print "1"
            self.moveLeft(arena)
            return
        elif self.returnLocationY() < self.targetX:
            print self.returnLocationY() , self.targetX
            print "2"
            self.moveRight(arena)
            return
        if self.returnLocationX() > self.targetY:
            print self.returnLocationX() , self.targetY
            print "3"
            self.moveUp(arena)
            moved = True
            return
        elif self.returnLocationX() < self.targetY:
            print self.returnLocationX() , self.targetY
            print "4"
            self.moveDown(arena)
            moved = True
            return

        if self.returnLocationX() == self.targetY and self.returnLocationY() == self.targetX:
#            print self.returnLocationX()
#            print self.returnLocationY()
#            print self.targetX 
#            print self.targetY
            return

        return

    def ret_points(self):
        return self.__points
        
##TIME VARIABLE
##user inputs time in minutes and seconds
#minutes = input("How many minutes: ") 
#seconds = input("Number of seconds: ")
#
#startTime = time.time()
#finishTime = startTime + seconds
#
#count = 0
#
#while time.time() < finishTime:
#  count += 1
#  print count
#  time.sleep(1) #sleep for a second
#
#print "Time is up!"  



