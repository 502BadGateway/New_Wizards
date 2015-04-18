# """

#Ive recreated this file because the original main file was straight from project 2.
#No attempt to clean up, add new functionality or adapt current has been made. 
#Importing modules we arnt using, and using stuff we agreed not to use.
#After going through it, its quicker to c/p back in stuff we need, rather than modify it.
#Since its quicker to write code than to read it.
#
#- Dan
#
#"""
#ALL PROJECT MODULES
from __future__ import print_function
import pygame #We need this to run anything
#from pygame.locals import * #we need this local so we can run the quit sequence
import sys #again used to run quick sequence
from display import display #used for p1, p2
from mapSelection import mapSelect
from city import city
from collectorBot import collectorBot
from display import display
from treasure import treasure
from trap import trap
from sortSelection import sortSelect #from sort selection file. import sort select class
from treasureSelectClass import treasureSelect
from treasureDictionary import dictionary
from pygeo import Geo
#MODULES FOR PART 1
import wikipedia #displays  treasure information
#MODULES FOR PART 2
import random #needed to choose trap
import wikipedia


def selectSort(): #defines function
    sortScreen= display(False,510,320) #creates display
    sortButtons = []#created empty list
    sortButtons.append (sortSelect("bubbleSort",30,40,"ASSETS/bubbleSort.png",130,100)) #creates a instance of a class and puts it into the end of the sort buttons list
    sortButtons.append (sortSelect("mergeSort",190,40,"ASSETS/mergeSort.png",130,100))
    sortButtons.append (sortSelect("insertionSort",350,40,"ASSETS/insertionSort.png",130,100))
    
    for btns in sortButtons: #this states for every button in that list it will...
        sortScreen.addSortSelectBtn(btns) #...display that button
        
    sortScreen.render()#actually draws the button
    
    while 1: #loops forever
        for event in pygame.event.get(): #will look at all the event that pygame has stored
            if event.type == pygame.QUIT: #tries to find if any of them are quit
                sys.exit() #then it would quit

            #detects which button the user has clicked on
            elif event.type == pygame.MOUSEBUTTONDOWN: #if that doesnt ^ then check to see if any of them is a mouse click
                x, y = event.pos #if this is ^ true then we save location of mouse click
                #print( "click" ),x,y
                if  x>30 and x<160 and y>40 and y<140: #check to see if we clicked on the button
                    print( "Bubble Sort Selected" )
                    #bubbleSorting = BubbleSorting()
                    return "BubbleSort" #....then we return the sort, in this case bubble sort

            elif event.type == pygame.MOUSEBUTTONDOWN: #if that doesnt ^ then check to see if any of them is a mouse click
                x, y = event.pos #if this is ^ true then we save location of mouse click
                #print( "click" ),x,y
                if  x>190 and x<320 and y>40 and y<140: #check to see if we clicked on the button
                    print( "Merge Sort Selected" )
                    #mergeSorting = MergeSorting()
                    return "MergeSort" #....then we return the sort, in this case Merge sort
            elif event.type == pygame.MOUSEBUTTONDOWN: #if that doesnt ^ then check to see if any of them is a mouse click
                x, y = event.pos #if this is ^ true then we save location of mouse click
                #print( "click" ),x,y
                if  x>350 and x<480 and y>40 and y<140: #check to see if we clicked on the button
                    print( "Insertion Sort Selected" )
                    #insertionSorting = InsertionSorting()
                    return "InsertionSort" #....then we return the sort, in this case Heap sort    


def selectMap(mapSelect):
    displayScreen = display(False,510,320)

    buttons = []

    buttons.append(mapSelect("London",30,40,"ASSETS/London.png",130,100))
    buttons.append(mapSelect("Paris",190,40,"ASSETS/Paris.png",130,100))
    buttons.append(mapSelect("New York",350,40,"ASSETS/NewYork.png",130,100))
    buttons.append(mapSelect("Tokyo",30,180,"ASSETS/Tokyo.png",130,100))
    buttons.append(mapSelect("Johannesburg",190,180,"ASSETS/Johannesburg.png",130,100))
    buttons.append(mapSelect("Berlin",350,180,"ASSETS/Berlin.png",130,100))

    for btns in buttons:
        displayScreen.addMapSelectBtn(btns)

    displayScreen.render()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #detects which button the user has clicked on
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                x, y = event.pos
                #print( "click" ),x,y
                if  x>30 and x<160 and y>40 and y<140:
                    print( "London Clicked" )
                    City = city("London",[])
                    Sort = selectSort()
                    Treasure = selectTreasure()
                    Treasure, Trap = selectTreasureTrap(City, Treasure)
                    return City, Sort, Treasure, Trap 
                    #self.mapSelected = "ASSETS\staticmapLondon.png" # what will be referenced later to know what map to use.
                    #treasurePos(mapSelected)
                elif x>190 and x<320 and y>40 and y<140:
                    print( "Paris Clicked" )
                    City = city("Paris", [])
                    Sort = selectSort()
                    Treasure = selectTreasure()
                    Treasure, Trap = selectTreasureTrap(City, Treasure)
                    return City, Sort, Treasure, Trap
                    #mapSelected = "ASSETS\staticmapParis.png"
                    #treasurePos(mapSelected)
                elif x>350 and x<480 and y>40 and y<140:
                    print( "New York Clicked" )
                    City = city("NewYork",[]) 
                    Sort = selectSort()
                    Treasure = selectTreasure()
                    Treasure, Trap = selectTreasureTrap(City, Treasure)
                    return City, Sort, Treasure,Trap
                    #self.mapSelected = "ASSETS\staticmapNewYork.png"
                    #treasurePos(mapSelected)
                elif x>30 and x<160 and y>180 and y<280:
                    print( "Tokyo Clicked" )
                    City = city("Tokyo",[])
                    Sort = selectSort
                    Treasure = selectTreasure()
                    Treasure, Trap = selectTreasureTrap(City, Treasure)
                    return City, Sort, Treasure, Trap
                    #self.mapSelected = "ASSETS\staticmapTokyo.png"
                    #treasurePos(mapSelected)
                elif x>190 and x<320 and y>180 and y<280:
                    print( "Johannesburg Clicked" )
                    City = city("Johannesburg",[])
                    Sort = selectSort()
                    Treasure = selectTreasure()
                    Treasure, Trap = selectTreasureTrap(City, Treasure)
                    return City, Sort, Treasure, Trap
                    #self.mapSelected = "ASSETS\staticmapJohannesburg.png"
                    #treasurePos(mapSelected)
                elif x>350 and x<480 and y>180 and y<280:
                    print( "Berlin Clicked" )
                    City = city("Berlin",[])
                    Sort = selectSort()
                    Treasure = selectTreasure()
                    Treasure, Trap = selectTreasureTrap(City, Treasure)
                    return City, Sort, Treasure,Trap
                    #self.mapSelected = "ASSETS\staticmapBerlin.png"
                    #treasurePos(mapSelected)
                else:
                    print( "not on button" )


def selectTreasure():
        displayScreen = display(False,670,600)#creates a white display for buttons to be placed on

        #places all the buttons
        treasureButton = []

        treasureList = ["Chest","Coins","Diamond","DiamondBlock","EmeraldBlock","GoldBar","GoldBlock","Iron","Lapis","LapisBlock","Ring","Sword","Tiara","Emerald"] #List holding all the treasures
         #                                        left corner
        #items handed are as followed ---     name   x   y   file locations   size x&y

        treasureButton.append(treasureSelect("Chest",30,40,"ASSETS/treasures/chest.png",130,100))
        treasureButton.append(treasureSelect("Coin",190,40,"ASSETS/treasures/coins.png",130,100))
        treasureButton.append(treasureSelect("Crown",350,40,"ASSETS/treasures/crown.png",130,100))
        treasureButton.append(treasureSelect("Diamond",510,40,"ASSETS/treasures/diamond.png",130,100))
        treasureButton.append(treasureSelect("DiamondBlock",30,180,"ASSETS/treasures/diamondblock.png",130,100))
        treasureButton.append(treasureSelect("EmeraldBlock",190,180,"ASSETS/treasures/emeraldblock.png",130,100))
        treasureButton.append(treasureSelect("GoldBar",350,180,"ASSETS/treasures/goldbar.png",130,100))
        treasureButton.append(treasureSelect("GoldBlock",510,180,"ASSETS/treasures/goldblock.png",130,100))
        treasureButton.append(treasureSelect("Iron",30,320,"ASSETS/treasures/iron.png",130,100))
        treasureButton.append(treasureSelect("Lapis",190,320,"ASSETS/treasures/lapis.png",130,100))
        treasureButton.append(treasureSelect("LapisBlock",350,320,"ASSETS/treasures/lapisblock.png",130,100))
        treasureButton.append(treasureSelect("Ring",510,320,"ASSETS/treasures/ring.png",130,100))
        treasureButton.append(treasureSelect("Sword",30,460,"ASSETS/treasures/sword.png",130,100))
        treasureButton.append(treasureSelect("Tiara",190,460,"ASSETS/treasures/tiara.png",130,100))
        treasureButton.append(treasureSelect("Emerald",350,460,"ASSETS/treasures/emerald.png",130,100))

        for btn in treasureButton:
                displayScreen.addTreasureBtn(btn)

        displayScreen.render()
# this waits for the user to click on 5 different treasures
        treasureWishList = []
        i = 0
        while i < 10:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()

                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                                if  x>30 and x<160 and y>40 and y<140:
                                        print( "Chest Clicked" )
                                        i = i + 1
                                        treasureWishList.append("Chest")
                                elif x>190 and x<320 and y>40 and y<140:
                                        print( "Coins Clicked" )
                                        i = i + 1
                                        treasureWishList.append("Coins")
                                elif x>350 and x<480 and y>40 and y<140:
                                        print( "Crown Clicked" )
                                        i = i + 1
                                        treasureWishList.append("Crown")
                                elif x>510 and x<640 and y>40 and y<140:
                                        print( "Diamond Clicked" )
                                        i = i + 1
                                        treasureWishList.append("Diamond")
                                elif x>30 and x<160 and y>180 and y<280:
                                        print( "Diamond Block Clicked" )
                                        i = i + 1
                                        treasureWishList.append("DiamondBlock")
                                elif x>190 and x<320 and y>180 and y<280:
                                        print( "Emerald Block Clicked" )
                                        i = i + 1
                                        treasureWishList.append("EmeraldBlock")
                                elif x>350 and x<480 and y>180 and y<280:
                                        print( "Gold Bar Clicked" )
                                        i = i + 1
                                        treasureWishList.append("GoldBar")
                                elif x>510 and x<640 and y>180 and y<280:
                                        print( "Gold Block Clicked" )
                                        i = i + 1
                                        treasureWishList.append("GoldBlock")
                                elif x>30 and x<160 and y>320 and y<420:
                                        print( "Iron Clicked" )
                                        i = i + 1
                                        treasureWishList.append("Iron")
                                elif x>190 and x<320 and y>320 and y<420:
                                        print( "Lapis" )
                                        i = i + 1
                                        treasureWishList.append("Lapis")
                                elif x>350 and x<480 and y>320 and y<420:
                                        print( "Lapis Block Clicked" )
                                        i = i + 1
                                        treasureWishList.append("LapisBlock")
                                elif x>510 and x<640 and y>320 and y<420:
                                        print( "Ring Clicked" )
                                        i = i + 1
                                        treasureWishList.append("Ring")
                                elif x>30 and x<160 and y>460 and y<560:
                                        print( "Sword Clicked" )
                                        i = i + 1 
                                        treasureWishList.append("Sword")
                                elif x>190 and x<320 and y>460 and y<560:
                                        print( "Tiara Clicked" )
                                        i = i + 1
                                        treasureWishList.append("Tiara")
                                elif x>350 and x<480 and y>460 and y<560:
                                        print( "Emerald Clicked" )
                                        i = i + 1 
                                        treasureWishList.append("Emerald")
                                else:
                                        print( "not on button" )                           


        print( "got here?" )                       
        print( "treasureWishList" )
        return treasureWishList, treasureList
        

def selectTreasureTrap(city):
    backgroundImage = city.ret_image_path()

        #displayScreen = display(backgroundImage,1280,960)#loads the map selected as background for user to place treasure and traps on
    #displayScreen = display(backgroundImage,1280,960)#loads the map selected as background for user to place treasure and traps on
    displayScreen = display(False,670,600)#creates a white display for buttons to be placed on

    #places all the buttons
    treasureButton = []

    treasureWishList = [] #List holding all the treasures
     #                                        left corner
    #items handed are as followed ---     name   x   y   file locations   size x&y

    treasureButton.append(treasureSelect("Chest",30,40,"ASSETS/treasures/chest.png",130,100))
    treasureButton.append(treasureSelect("Coin",190,40,"ASSETS/treasures/coins.png",130,100))
    treasureButton.append(treasureSelect("Crown",350,40,"ASSETS/treasures/crown.png",130,100))
    treasureButton.append(treasureSelect("Diamond",510,40,"ASSETS/treasures/diamond.png",130,100))
    treasureButton.append(treasureSelect("DiamondBlock",30,180,"ASSETS/treasures/diamondblock.png",130,100))
    treasureButton.append(treasureSelect("EmeraldBlock",190,180,"ASSETS/treasures/emeraldblock.png",130,100))
    treasureButton.append(treasureSelect("GoldBar",350,180,"ASSETS/treasures/goldbar.png",130,100))
    treasureButton.append(treasureSelect("GoldBlock",510,180,"ASSETS/treasures/goldblock.png",130,100))
    treasureButton.append(treasureSelect("Iron",30,320,"ASSETS/treasures/iron.png",130,100))
    treasureButton.append(treasureSelect("Lapis",190,320,"ASSETS/treasures/lapis.png",130,100))
    treasureButton.append(treasureSelect("LapisBlock",350,320,"ASSETS/treasures/lapisblock.png",130,100))
    treasureButton.append(treasureSelect("Ring",510,320,"ASSETS/treasures/ring.png",130,100))
    treasureButton.append(treasureSelect("Sword",30,460,"ASSETS/treasures/sword.png",130,100))
    treasureButton.append(treasureSelect("Tiara",190,460,"ASSETS/treasures/tiara.png",130,100))
    treasureButton.append(treasureSelect("Emerald",350,460,"ASSETS/treasures/emerald.png",130,100))

    for btn in treasureButton:
        displayScreen.addTreasureBtn(btn)

    displayScreen.render()
# this waits for the user to click on 5 different treasures
    treasureWishList = []
    i = 0
    while i < 10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if  x>30 and x<160 and y>40 and y<140:
                    print( "Chest Clicked" )
                    i = i + 1
                    treasureWishList.append("Chest")
                elif x>190 and x<320 and y>40 and y<140:
                    print( "Coins Clicked" )
                    i = i + 1
                    treasureWishList.append("Coins")
                elif x>350 and x<480 and y>40 and y<140:
                    print( "Crown Clicked" )
                    i = i + 1
                    treasureWishList.append("Crown")
                elif x>510 and x<640 and y>40 and y<140:
                    print( "Diamond Clicked" )
                    i = i + 1
                    treasureWishList.append("Diamond")
                elif x>30 and x<160 and y>180 and y<280:
                    print( "Diamond Block Clicked" )
                    i = i + 1
                    treasureWishList.append("DiamondBlock")
                elif x>190 and x<320 and y>180 and y<280:
                    print( "Emerald Block Clicked" )
                    i = i + 1
                    treasureWishList.append("EmeraldBlock")
                elif x>350 and x<480 and y>180 and y<280:
                    print( "Gold Bar Clicked" )
                    i = i + 1
                    treasureWishList.append("GoldBar")
                elif x>510 and x<640 and y>180 and y<280:
                    print( "Gold Block Clicked" )
                    i = i + 1
                    treasureWishList.append("GoldBlock")
                elif x>30 and x<160 and y>320 and y<420:
                    print( "Iron Clicked" )
                    i = i + 1
                    treasureWishList.append("Iron")
                elif x>190 and x<320 and y>320 and y<420:
                    print( "Lapis" )
                    i = i + 1
                    treasureWishList.append("Lapis")
                elif x>350 and x<480 and y>320 and y<420:
                    print( "Lapis Block Clicked" )
                    i = i + 1
                    treasureWishList.append("LapisBlock")
                elif x>510 and x<640 and y>320 and y<420:
                    print( "Ring Clicked" )
                    i = i + 1
                    treasureWishList.append("Ring")
                elif x>30 and x<160 and y>460 and y<560:
                    print( "Sword Clicked" )
                    i = i + 1 
                    treasureWishList.append("Sword")
                elif x>190 and x<320 and y>460 and y<560:
                    print( "Tiara Clicked" )
                    i = i + 1
                    treasureWishList.append("Tiara")
                elif x>350 and x<480 and y>460 and y<560:
                    print( "Emerald Clicked" )
                    i = i + 1 
                    treasureWishList.append("Emerald")
                else:
                    print( "not on button" )               


    print( "got here?" )           
    print ( "treasureWishList" )
    return treasureWishList
    

def selectTreasureTrap(city, treasureStringList):
    backgroundImage = city.ret_image_path()
    displayScreen = display(backgroundImage,1280,960)#loads the map selected as background for user to place treasure and traps on

    Trdict = dictionary()

    treasureList = []
    trapList = []
    print (len(treasureStringList))

#places the treasure
    i = 0
    treasureNum = 6 #this may need to be changed depending on what num represent which 
    print ("treasureStringList")
    print (city.arena.show_arena())

    grid_sizes = [116,122]
        
    while i < 10:
        displayScreen.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print( "y, x:" )
                print (y,x)
                print( "Arena value" )
                print (city.arena.ret_element_value(y/10, x/10))
                if city.arena.ret_element_value(y/10, x/10) == 1 or city.arena.ret_element_value(y/10, x/10) == 2:
                     print( "in loop" )
                     city.arena.put(x/10,y/10, treasureNum)  #changes the number in the array from a road to the relevant treasure number the treasures will always be placed in the same order, the order they are in arrayNumberReference.txt
                     treasureList.append(treasure(x/10,y/10, Trdict.itemList[treasureStringList[0][i].lower()]['arenaVal'], treasureStringList[1][i], 6, "ASSETS/treasures/"+str(treasureStringList[1][i]).lower()+".png"))
                     print( "arena coords" )
                     print (city.arena.ret_element_value(y/10, x/10) )
                     print( "treasure list coords:" )
                     print (y/10,x/10)

                     
                     treasureNum = treasureNum + 1 #im want to reserve numbers 5 to 19 for treasures 
                     i=i+1
                else:
                    print( "Not a road" )
        for treasures in treasureList:
             displayScreen.setTreasureCollect(treasures.returnLocationY(), treasures.returnLocationX(), treasures.getImage())

#places the traps
    j=0
    while j < 3:
        displayScreen.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print (x,y)                         
                if (city.arena.ret_element_value(y/10, x/10) == 1 or city.arena.ret_element_value(y/10,x/10) == 2):
                    city.arena.put(y/10,x/10, 10) #might need to be changed, im assuming that 3 is traps
                    trapList.append(trap(y/10,x/10, random.randint(0, 100), "Trap", 8, "ASSETS/treasures/trap.png"))
                    j=j+1
                    print( "Placed road" )
                else:
                    print( "Not on a road" )
        for treasures in treasureList:
            displayScreen.setTreasureCollect(treasures.returnLocationY(), treasures.returnLocationX(), treasures.getImage())
        for traps in trapList:
            displayScreen.setTreasureCollect(traps.returnLocationX(), traps.returnLocationY(), traps.getImage())
    
    return treasureList, trapList
    



def findRobotLocation(ar, name, robotList, wishlist, treasureList):
    width = ar.ret_size()[0]-1        #Get the width and heights of the array
    height = ar.ret_size()[1]-1

    print( "Using width:" +str(width)) #dbg
    print( "Using height:" +str(height))
    
    placed = False                  #Store if we've placed anything
    x = 0
    rand_row = random.randint(0,height) #Pick a random row to spawn a trafficlight

    while x <= width-1 or placed != True:   #While we havent looked at every item in the row, and havent placed a light
        if ar.ret_element_value(rand_row, x) == 1 or ar.ret_element_value(rand_row, x) == 2:    #Check that the item we're on is a road.
            print( "ROBOT:" )
            print (rand_row, x)
            bot = collectorBot(ar, wishlist, treasureList, rand_row/10, x/10)                                    #Create a new robot!
            robotList.append(bot)
            ar.put(rand_row, x, 5)                                                            #Save it in the arena
            placed = True                       #Move on
            break
        x += 1
    return robotList 


def wiki(treasureName):


    wikiText = wikipedia.summary(treasureName, sentences = 2)
    wikiTextPos = (0,940,0,0)
    display.CreateText(wikiText,wikiTextPos,0)

    #display.render_textrect(wikiText,None,wikiTextPos,(0,0,0))


def main(mapSelect):

    pygame.init() #initialise pygame
    clock = pygame.time.Clock() #we will need this for ade's timer

    #this is temporary, it will use the display class later


def collectBot(city, robots, wishlist, Treasure, Traps): 

    TreasureCopy = list(Treasure)   #Copy treasure list
    Inventory = []
    
    #Passes the image of the city as the background. Requires an instance of city to have been created.
    #screen.setCollectorBot(cBot.returnLocationX(), cBot.returnLocationY(), cBot.returnImage()) #Set the location for the collector bot. Requires a location of a new bot to have been specified.
    resolution = (pygame.display.Info().current_w,pygame.display.Info().current_h)

    screen = display(city.ret_image_path(), resolution[0],resolution[1])

    while True: #While true TODO Add proper clause to quit program
        locY = 0
        for item in Treasure:   #Render the wish list list
            locY += 10
            textString = str(item.getName())+"    Score"+str(item.returnPoints())+"    Collected: "+str(item.returnCollected())
            screen.CreateText(textString, (680,locY,0,0), 40)

        for item in Traps:
            screen.setTreasureCollect(item.returnLocationX(), item.returnLocationY(), item.getImage())

        for item in Treasure:
            screen.setTreasureCollect(item.returnLocationY(), item.returnLocationX(), item.getImage())

        for bots in robots:
            if len(Treasure) > 0:
                collected, treasure = bots.treasureCheck(city.retArena(), Treasure)
                print (collected, treasure)
            else:
                print( "Collected all treasures" )
                #Treasure.remove(treasure)
                Inventory = bots.retInventory()
                return Inventory
                break
            if collected == True:
                Treasure.remove(treasure)
            if len(Treasure) == 0:
                print( "collected all treasures" )
                break
            screen.CreateText(str(bots.returnPoints()), (200,0,0,0), 0)
            bots.updateLocation(city, city.retArena(), bots, (Treasure[0].returnLocationX(), Treasure[0].returnLocationY()))
            screen.setCollectorBot(bots.returnLocationX(),bots.returnLocationY(), bots.returnImage()) #Set the location for the collector bot. Requires a location of a new bot to have been specified.
                        
        screen.render() #render
def locationSelect():
    geo = Geo("map1")
    geo.GetsScreenshot()
    City = city("Usrchoosen", [], True, "map1.png")
    Sort = selectSort()
    Treasure = selectTreasure()
    Treasure, Trap = selectTreasureTrap(City, Treasure)
    return City, Sort, Treasure, Trap 
    


#city, Sort, TreasureList, TrapList = selectMap(mapSelect)
pygame.init()
city, Sort, TreasureList, TrapList = locationSelect()
robots = []
robots = findRobotLocation(city.arena, "Barry", [], [], TreasureList)
inventory = collectBot(city, robots, TreasureList, TreasureList, TrapList)
print (inventory)
f = open("moduledList.py", 'w')
f.write("theList = [") 
count = 0
for items in inventory:
    if count == len(inventory)-1:
        f.write('"'+str(items.getName()).lower()+'"')
    else:
        f.write('"'+str(items.getName()).lower()+'",')
    count += 1
f.write("]")
f.close()

execfile('testSort.py')

