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
import pygame #We need this to run anything
#from pygame.locals import * #we need this local so we can run the quit sequence
import sys #again used to run quick sequence
from display import display #used for p1, p2
from mapSelection import mapSelect
from city import city
from collectorBot import collectorBot
from display import display
from treasure import treasure
from sortSelection import sortSelect #from sort selection file. import sort select class
from treasureSelectClass import treasureSelect
#MODULES FOR PART 1
import wikipedia #displays  treasure information
#MODULES FOR PART 2
import random #needed to choose trap

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
				#print "click",x,y
				if  x>30 and x<160 and y>40 and y<140: #check to see if we clicked on the button
					print "Bubble Sort Selected"
					return "BubbleSort" #....then we return the sort, in this case bubble sort
			elif event.type == pygame.MOUSEBUTTONDOWN: #if that doesnt ^ then check to see if any of them is a mouse click
				x, y = event.pos #if this is ^ true then we save location of mouse click
				#print "click",x,y
				if  x>190 and x<320 and y>40 and y<140: #check to see if we clicked on the button
					print "Merge Sort Selected"
					return "MergeSort" #....then we return the sort, in this case Merge sort
			elif event.type == pygame.MOUSEBUTTONDOWN: #if that doesnt ^ then check to see if any of them is a mouse click
				x, y = event.pos #if this is ^ true then we save location of mouse click
				#print "click",x,y
				if  x>350 and x<480 and y>40 and y<140: #check to see if we clicked on the button
					print "Insertion Sort Selected"
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
				#print "click",x,y
				if  x>30 and x<160 and y>40 and y<140:
					print "London Clicked"
					City = city("London",[])
					Sort = selectSort()
					Treasure = selectTreasure()
					TreasureTrap = selectTreasureTrap(City)
					return City, Sort, Treasure, TreasureTrap 
					#self.mapSelected = "ASSETS\staticmapLondon.png" # what will be referenced later to know what map to use.
					#treasurePos(mapSelected)
				elif x>190 and x<320 and y>40 and y<140:
					print "Paris Clicked"
					City = city("Paris", [])
					Sort = selectSort()
					Treasure = selectTreasure()
					TreasureTrap = selectTreasureTrap(City)
					return City, Sort, Treasure, TreasureTrap
					#mapSelected = "ASSETS\staticmapParis.png"
					#treasurePos(mapSelected)
				elif x>350 and x<480 and y>40 and y<140:
					print "New York Clicked"
					City = city("NewYork",[]) 
					Sort = selectSort()
					Treasure = selectTreasure()
					TreasureTrap = selectTreasureTrap(City)
					return City, Sort, Treasure, TreasureTrap
					#self.mapSelected = "ASSETS\staticmapNewYork.png"
					#treasurePos(mapSelected)
				elif x>30 and x<160 and y>180 and y<280:
					print "Tokyo Clicked"
					City = city("Tokyo",[])
					Sort = selectSort
					Treasure = selectTreasure()
					TreasureTrap = selectTreasureTrap(City)
					return City, Sort, Treasure, TreasureTrap
					#self.mapSelected = "ASSETS\staticmapTokyo.png"
					#treasurePos(mapSelected)
				elif x>190 and x<320 and y>180 and y<280:
					print "Johannesburg Clicked"
					City = city("Johannesburg",[])
					Sort = selectSort()
					Treasure = selectTreasure()
					TreasureTrap = selectTreasureTrap(City)
					return City, Sort, Treasure, TreasureTrap
					#self.mapSelected = "ASSETS\staticmapJohannesburg.png"
					#treasurePos(mapSelected)
				elif x>350 and x<480 and y>180 and y<280:
					print "Berlin Clicked"
					City = city("Berlin",[])
					Sort = selectSort()
					Treasure = selectTreasure()
					TreasureTrap = selectTreasureTrap(City)
					return City, Sort, Treasure, TreasureTrap
					#self.mapSelected = "ASSETS\staticmapBerlin.png"
					#treasurePos(mapSelected)
				else:
					print "not on button"


def selectTreasure():
	displayScreen = display(False,670,600)#creates a white display for buttons to be placed on

	#places all the buttons
	treasureButton = []

        treasureList = [] #List holding all the treasures
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
	i = 0
	while i < 11:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				x, y =event.pos
				if  x>30 and x<160 and y>40 and y<140:
					print "Chest Clicked"
					i = i + 1
                                        treasureList.append(treasure(x,y, 4, "Chest", 6, "ASSETS/Chest.png"))
                                elif x>190 and x<320 and y>40 and y<140:
					print "Coin Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonCoin.treasureName
				elif x>350 and x<480 and y>40 and y<140:
					print "Crown Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonCrown.treasureName
				elif x>510 and x<640 and y>40 and y<140:
					print "Diamond Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonDiamond.treasureName
				elif x>30 and x<160 and y>180 and y<280:
					print "Diamond Block Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonDiamondBlock.treasureName
				elif x>190 and x<320 and y>180 and y<280:
					print "Emerald Block Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonEmeraldBlock.treasureName
				elif x>350 and x<480 and y>180 and y<280:
					print "Gold Bar Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonGoldBar.treasureName
				elif x>510 and x<640 and y>180 and y<280:
					print "Gold Block Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonGoldBlock.treasureName
				elif x>30 and x<160 and y>320 and y<420:
					print "Iron Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonIron.treasureName
				elif x>190 and x<320 and y>320 and y<420:
					print "Lapis"
					i = i + 1
					#treasureList[i] = treasureButtonLapis.treasureName
				elif x>350 and x<480 and y>320 and y<420:
					print "Lapis Block Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonLapisBlock.treasureName
				elif x>510 and x<640 and y>320 and y<420:
					print "Ring Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonRing.treasureName
				elif x>30 and x<160 and y>460 and y<560:
					print "Sword Clicked"
					i = i + 1 
					#treasureList[i] = treasureButtonSword.treasureName
				elif x>190 and x<320 and y>460 and y<560:
					print "Tiara Clicked"
					i = i + 1
					#treasureList[i] = treasureButtonTiara.treasureName
				elif x>350 and x<480 and y>460 and y<560:
					print "Emerald Clicked"
					i = i + 1 
					#treasureList[i] = treasureButtonEmerald.treasureName
				else:
					print "not on button" 				

                
        return treasureList
	

def selectTreasureTrap(city):
        city.arena.show_arena()
	backgroundImage = city.ret_image_path()

	displayScreen = display(backgroundImage,1280,960)#loads the map selected as background for user to place treasure and traps on

#places the treasure
	i = 0
	treasureNum = 6 #this may need to be changed depending on what num represent which 
	while i < 5:
                displayScreen.render()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
                                print x,y                         
				if (city.arena.ret_element_value(y/3, x/3) == 1 or city.arena.ret_element_value(y/3, x/3) == 2):
#					treasurePosListX[i] = x #puts location in 2 lists for reference later if needed
#					treasurePosListY[i] = y
					city.arena.put(y/3,x/3, treasureNum)  #changes the number in the array from a road to the relevant treasure number the treasures will always be placed in the same order, the order they are in arrayNumberReference.txt
					treasureNum = treasureNum + 1 #im want to reserve numbers 5 to 19 for treasures 
					i=i+1
				else:
					print "Not on road"
        print "done placing treasures"
	
#places the traps
	j=0
	while j < 3:
                print "placing traps"
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
                                print x,y                         
				if (city.arena.ret_element_value(y/3, x/3) == 1 or city.arena.ret_element_value(y/3,x/3) == 2):
#					trapPosListX[j] = x
#					trapPosListY[j] = y
					city.arena.put(y/3,x/3, 3) #might need to be changed, im assuming that 3 is traps
                                else:
                                    print "Not on a road"
        print "Done placing traps"

	
	#mapButtonLondon.cityText(None,20,28,12,"Please select your location",(10,10,10))



def findRobotLocation(ar, name, robotList, wishlist, treasureList):
    width = ar.ret_size()[0]-1        #Get the width and heights of the array
    height = ar.ret_size()[1]-1

    print "Using width:"+str(width) #dbg
    print "Using height:"+str(height)
    
    placed = False                  #Store if we've placed anything
    x = 0
    rand_row = random.randint(0,height) #Pick a random row to spawn a trafficlight

    while x <= width-1 or placed != True:   #While we havent looked at every item in the row, and havent placed a light
        if ar.ret_element_value(rand_row, x) == 1 or ar.ret_element_value(rand_row, x) == 2:    #Check that the item we're on is a road.
            print "ROBOT:"
            print rand_row, x
            bot = collectorBot(ar, wishlist, treasureList, rand_row, x)                                    #Create a new robot!
            robotList.append(bot)
            ar.put(rand_row, x, 5)                                                            #Save it in the arena
            placed = True                       #Move on
            break
        x += 1
    return robotList 

	
def main(mapSelect):

	pygame.init() #initialise pygame
	clock = pygame.time.Clock() #we will need this for ade's timer

	#this is temporary, it will use the display class later
	"""
	displayScreen = pygame.display.set_mode((510,320)) 
	displayBackground = pygame.Surface(displayScreen.get_size())
	displayBackground = displayBackground.convert()
	displayBackground.fill((250,250,250))
	displayScreen.blit(displayBackground,(0,0))"""



def collectBot(city, robots, wishlist, Treasure):
	

	#Here we will create a new map selection instance.
	#Then we will retrive the data from that to use later.
        print "PATH"
	print city.ret_image_path()

	screen = display(city.ret_image_path(),1280, 960)

    #Create a new collector bot. Relies on having an already created City, arena, wishlist and treasurelist.
	
	#Create a new instance of a display - For the collector bot thingy
	#Passes the image of the city as the background. Requires an instance of city to have been created.
	#screen.setCollectorBot(cBot.returnLocationX(), cBot.returnLocationY(), cBot.returnImage()) #Set the location for the collector bot. Requires a location of a new bot to have been specified.



	while True: #While true TODO Add proper clause to quit program
                locY = 0
		for item in wishlist:   #Render the wish list list
                        locY += 10
			textString = str(item.getName())+"    Score"+str(item.returnPoints())+"    Collected: "+str(item.returnCollected())
		 	screen.CreateText(textString, (0,locY,0,0), 40)
                for bots in robots:
	        	bots.updateLocation(city.arena)
	        	screen.setCollectorBot(bots.returnLocationX(),bots.returnLocationY(), bots.returnImage()) #Set the location for the collector bot. Requires a location of a new bot to have been specified.
                        
		screen.render() #render


City, Sort, Treasure, TreasureTrap = selectMap(mapSelect)
City.arena.show_arena()
robots = []
robots = findRobotLocation(City.arena, "Barry", [], [], Treasure)
collectBot(City, robots, Treasure, Treasure)
