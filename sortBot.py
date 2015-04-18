import pygame
from robot import *

class SortBot(robot, pygame.sprite.Sprite): #class called sortbot.

	def __init__(self, treasureList): #initialises sortbot
		pygame.sprite.Sprite.__init__(self) #initalises sprite base class

		self.points = 0 #This is the amount of points the robot has in total
		self.location = 0 #where on treasure sort map robot is
		self.image = pygame.image.load('ASSETS/car.png') #loads image
		self.rect = self.image.get_rect() #gets the rect of the images
		self.rect.x = 0 #stores the x location of the robot on screen
		self.rect.y = 0 #stores the y location of the robot on screen
		self.carrying = "" #stores treasure robot is moving
		self.carryingSwap = "" # stores old object while we replace them
		self.loaded = False #is the robot crrying a treasure?
		self.target = 0 #where on the list is the robot aimed?

	def moveLeft(self):
		if(self.loaded == False):
			#for i in range(0,28): #moves 140 pixels
			self.rect.x -= 5 #left 2 pixels
				#screen.blit(background, (0, 0)) #makes the background blit
				#self.update() #updates something else
				#for i in treasureList: #goes through the treasures argh
					#i.update() #updates that too
				#pygame.display.update() #updates the screen
				#time.sleep(0.001) #go to sleep pygame
			self.location = self.location - 1 #change the array location
		elif(self.loaded == True):
			#for i in range(0,28): #moves 140 pixels
			self.rect.x -= 5 #left 2 pixels
			self.carrying.rect.x = self.rect.x
			self.carrying.rect.y = self.rect.y
				#screen.blit(background, (0, 0)) #makes the background blit
				#self.update() #updates something else
				#self.carrying.update()
				#for i in treasureList: #goes through the treasures argh
				#	i.update() #updates that too
				#pygame.display.update() #updates the screen
				#time.sleep(0.001) #go to sleep pygame
			self.location = self.location - 1 #change the array location

	def moveRight(self): #moves robot right
		if(self.loaded == False):
			#for i in range(0,28): #moves for 140 pixels (one block yeah)
			self.rect.x += 5 #right two pixels
				#screen.blit(background, (0, 0)) #blit the background
				#self.update() #updates the screen bro
				#for i in treasureList: #loops through the treasures, this is bad code
				#	i.update() #update them dubbloons
				#pygame.display.update() #shove that to the screen please
				#time.sleep(0.001) #GO TO SLEEP PLEASE 
			self.location = self.location + 1 #change the location in array
		elif(self.loaded == True):
			#for i in range(0,28): #moves 140 pixels
			self.rect.x += 5 #left 2 pixels
			self.carrying.rect.x = self.rect.x
			self.carrying.rect.y = self.rect.y
				#screen.blit(background, (0, 0)) #makes the background blit
				#self.update() #updates the robot
				#self.carrying.update()
				#for i in treasureList: #goes through the treasures argh
				#	i.update() #updates that too

				#pygame.display.update() #updates the screen
				#time.sleep(0.001) #go to sleep pygame
			self.location = self.location + 1 #change the array location

	def moveUp(self):
		if(self.loaded == False):
			#while self.rect.y > 230: #move up, until you are under treasure
			self.rect.y -= 5 #moves up 2 pixels
				#screen.blit(background, (0, 0)) #blit dat background
				#self.update() #update that robot
				#for i in treasureList: #the treasure list again
				#	i.update() #updating them
				#pygame.display.update() #shoving it to screen
				#time.sleep(0.001) #sleeping
		elif(self.loaded == True):#
			#while self.rect.y > 230:
			self.rect.y -= 5 #moves up 2 pixels
			self.carrying.rect.x = self.rect.x
			self.carrying.rect.y = self.rect.y
				#screen.blit(background, (0, 0)) #blit dat background
				#self.update() #update that robot
				#for i in treasureList: #the treasure list again
				#	i.update() #updating them
				#self.carrying.update()
				#pygame.display.update() #shoving it to screen
				#time.sleep(0.001) #sleeping

	def moveDown(self):
		if(self.loaded == False):
			#while self.rect.y < 500:
			self.rect.y += 5
				#screen.blit(background, (0,0))
				#self.update()
				#for i in treasureList:
				#	i.update()
				#pygame.display.update()
				#time.sleep(0.001)
		elif(self.loaded == True):
			#while self.rect.y < 500:
			self.rect.y += 5
			self.carrying.rect.x = self.rect.x
			self.carrying.rect.y = self.rect.y
				#screen.blit(background, (0,0))
				#self.update()
				#for i in treasureList:
				#	i.update()
				#self.carrying.update()
				#pygame.display.update()
				#time.sleep(0.001)

	def pickTreasureUp(self,treasureList, null): #pick up treasure from list
		self.carrying = treasureList[self.location] #picks up treasure it is infront of
		treasureList[self.location] = null #fills list with empty item
		self.loaded = True #loads robot
		return treasureList #returns list

	def replaceTreasure(self,treasureList): #picks up and drops off treasure
		self.carryingSwap = self.carrying #moves current treasure to holding var
		self.carrying = treasureList[self.location] #picks up new treasure
		treasureList[self.location] = self.carryingSwap #places old one down
		treasureList[self.location].rect.x = treasureList[self.location].rect.x - 10 #adjusts rect x
		treasureList[self.location].rect.y = treasureList[self.location].rect.y + 50 #adjusts rect y
		return treasureList #returns the list
	
	def placeTreasure(self,treasureList, null): #puts down treasure
		treasureList[self.location] = self.carrying #places treasure into list
		self.carrying = null #fills it with instance of null
		treasureList[self.location].rect.x = treasureList[self.location].rect.x - 10 #adjusts rect
		treasureList[self.location].rect.y = treasureList[self.location].rect.y + 50 #adjusts rect
		self.loaded = False #unloades robot
		return treasureList			#returns the list

	def moveToTarget(self): #Runs all our code to get to thing
	#This function contains the blocks, moveLeft (or right) and move up.
		while self.location != self.target: #while we arnt infront of target
			if self.location > self.target: #while we are to the right of target
				self.moveLeft() #move left son
				#WE NEED DISPLAY UPDATE STUFF HERE OR SOMETHING
			elif self.location < self.target: #while we are to the left of the target
				self.moveRight() #move right please
				#WE NEED DISPLAY STUFF HERE ASWELL MAYBE

	def swap(self, valOne, valTwo):
		self.target = valOne #assign target one
		self.moveToTarget() #move towards first target
		self.moveUp() #move upwards
		self.pickTreasureUp(treasureList, null) #pick up treasure
		self.target = valTwo #assign target two to target
		self.moveDown()
		self.moveToTarget()
		#for i in treasureList:
		#	i.update()
		#pygame.display.update()
		self.moveUp()
		self.replaceTreasure(treasureList, null)
		self.target = valOne
		self.moveDown()
		self.moveToTarget()
		self.moveUp()
		self.placeTreasure(treasureList, null)
		self.moveDown()



		
