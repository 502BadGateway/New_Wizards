"""

This file is a stand alone testing script
It will run the same sorting animation as the final project will
However, we are over a week away from completion.
This, when completed will allow the group to test their own sorting algorithms

"""
"""
THE MODULES
"""
import sys
import pygame
from pygame.locals import *
import time

pygame.init()
valOne = 4
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Sort Bot")
background = pygame.image.load('ASSETS/sortBackground.png')
screen.blit(background, (0,0))

"""
THE CLASSES
"""

class sortBot(pygame.sprite.Sprite): #calls sprite base class

	def __init__(self):
		pygame.sprite.Sprite.__init__(self) #initialised base class
		self.name = "" #gives robot a name
		self.points = 0 #gives robot points
		self.location = 0
		self.dir = 0 #direction turning
		self.image = pygame.image.load('ASSETS/car.png') #loads image
		self.rect = self.image.get_rect() #gets the rect
		self.rect.x = 0 #stores coord x
		self.rect.y = 0 #stores coord y
		self.carrying = ""
		self.target = 0

	def turnLeft(self): #charges turning var to left 
		self.dir = 90 #Makes dir left turning
		oldCenter = self.rect.center #Stores the old centre here
 		self.image = pygame.transform.rotate(self.image, self.dir) #turns car
		self.rect = self.image.get_rect() #gets the rect
		self.rect.center = oldCenter #returns the old centre
		screen.blit(self.image, (self.rect.x, self.rect.y)) #blit it on screen
    
	def turnRight(self): #changes turning var to right 
		self.dir = -90 #makes dir right turning
		oldCenter = self.rect.center #sotrs old centre
		self.image = pygame.transform.rotate(self.image, self.dir) #rotates the robot
		self.rect = self.image.get_rect() #gets the rect
		self.rect.center = oldCenter #returns the old centre
		screen.blit(self.image, (self.rect.x, self.rect.y)) #blit it on screen

	def update(self):
		screen.blit(self.image, (self.rect.x, self.rect.y)) #updates image on screen

	def moveLeft(self): #moves robot left
		for i in range(0,70): #moves 140 pixels
			self.rect.x -= 2 #left 2 pixels
			screen.blit(background, (0, 0)) #makes the background blit
			self.update() #updates something else
			for i in treasureList: #goes through the treasures argh
				i.update() #updates that too
			pygame.display.update() #updates the screen
			time.sleep(0.001) #go to sleep pygame
		self.location = self.location - 1 #change the array location
		print self.location #DEBUG print whut

	def moveRight(self): #moves robot right
		for i in range(0,70): #moves for 140 pixels (one block yeah)
			self.rect.x += 2 #right two pixels
			screen.blit(background, (0, 0)) #blit the background
			self.update() #updates the screen bro
			for i in treasureList: #loops through the treasures, this is bad code
				i.update() #update them dubbloons
			pygame.display.update() #shove that to the screen please
			time.sleep(0.001) #GO TO SLEEP PLEASE 
		self.location = self.location + 1 #change the location in array
		print self.location #Debug, this needs to go soon

	def moveUp(self): #moves the robot up to treasure yay
		for i in range(0,10): #moves for 20 pixels
			self.rect.y -= 2 #moves up 2 pixels
			screen.blit(background, (0, 0)) #blit dat background
			self.update() #update that robot
			for i in treasureList: #the treasure list again
				i.update() #updating them
			pygame.display.update() #shoving it to screen
			time.sleep(0.001) #sleeping


	def moveToTarget(self): #Runs all our code to get to thing
		while self.location != self.target: #while we arnt infront of target
			if self.location > self.target: #while we are to the right of target
				self.moveLeft() #move left son
			elif self.location < self.target: #while we are to the left of the target
				self.moveRight() #move right please

		while self.rect.y > 230: #move up, until you are under treasure
			self.moveUp() #move please





class treasure(pygame.sprite.Sprite): #I mocked up a treasure class, we can pull it from the other one

	def __init__(self): #initialise it
		pygame.sprite.Sprite.__init__(self) #no idea why i need it, but i need it
		self.name = "" #give that dubbloon a name
		self.image = pygame.image.load('ASSETS/testTreasure.png') #and a picture
		self.rect = self.image.get_rect() #get yourself a rectangle
		self.rect.x = 0 #x coord of the treasure
		self.rect.y = 0 #y coord of the treasure
		self.points = 0 #points the treasure is worth
		self.location = 0 #location in list yeah

	def update(self): #update it
		screen.blit(self.image, (self.rect.x, self.rect.y)) #blit that dubbloon


"""
THE TREASURES 
"""

treasure1 = treasure()  #ALL THIS ISNT NEEDED I DONT THINK
treasure1.location = 5  #make the treasure location 5 in list

treasure2 = treasure() #create object treasure2
treasure2.location = 3 #put treasure 2 in slot 3

treasure3 = treasure() #create object treasure3
treasure3.location = 1 #put treasure 3 in slot 1

treasure4 = treasure() #create object treasure4
treasure4.location = 2 #put it in slot 2 please

treasure5 = treasure() #create object treasure5
treasure5.location = 0 #put it in slot 5

treasure6 = treasure() #ok so you get the point, but i want the lines on the github
treasure6.location = 6 #gunna look like i wrote so much code son

treasure7 = treasure() #I mean, just give me my degree already
treasure7.location = 4 #place treasure 7 in slot 4

treasureList = [treasure1, treasure2, treasure3, treasure4, treasure5, treasure6, treasure7]
#this is a list of all the treasure objects

for i in treasureList: #this is a for loop of the treasure objects
	i.rect.x = ((i.location * 143) + 140) #this places the objects at the right slots
	i.rect.y = 280 #this gives then the right y coord

"""
THE ROBOT 
"""

theSortBot = sortBot()
theSortBot.name = "Fred"
theSortBot.location = 2
theSortBot.rect.x = ((theSortBot.location * 143) + 150) 
theSortBot.rect.y = 500
theSortBot.dir = 0
theSortBot.target = valOne

"""
THE MAIN LOOP
"""

screen.blit(background, (0,0))
pygame.display.update() #updates everything

theSortBot.update()
for i in treasureList:
	i.update()

pygame.display.update()
while 1:
	for event in pygame.event.get(): #Quit sequence
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	theSortBot.moveToTarget()
	theSortBot.update()
	for i in treasureList:
		i.update()
	pygame.display.update() #updates everything
	time.sleep(0.1)


