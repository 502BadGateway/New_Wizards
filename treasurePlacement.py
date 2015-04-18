import pygame
import sys

class treasurePos(mapSelected):
	def mapTreasurePos(self,mapSelected):
		pygame.init()

		#create display
		self.size = width, height = 1280, 960
		self.display = pygame.display.set_mode(self.size)
		self.background = pygame.image.load(mapSelected)
		self.display.blit(self.background,(0,0))

		font = pygame.font.Font(None,20)
		text = font.render("Please place 5 treasures on the map, you must click on a road.")
		self.display.blit(text, (28,12))

		i = 0
		while i < 5:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				elif event.type == pygame.MOUSEBUTTONDOWN:
					if (array[x][y] == 1 or array[x][y] == 2) #this needs to be changed to what the array is acturly calleds
						x, y = event.pos
						treasurePosListX[i] = x
						treasurePosListY[i] = y
						i=i+1
					else:
						print "Not on road"