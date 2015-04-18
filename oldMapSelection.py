
import pygame
import sys


class mapSelect():
	def mapPanel(self):
		pygame.init()

		#create display
		self.size = width, height = 510, 320
		self.display = pygame.display.set_mode(self.size)
		self.background = pygame.Surface(self.display.get_size())
		self.background = self.background.convert()
		self.background.fill((250, 250, 250))
		self.display.blit(self.background,(0,0))
		#pygame.display.set_catption("Map Selection")

		#load in button images


		self.London = pygame.image.load("ASSETS/London.png")
		self.Paris = pygame.image.load("ASSETS/Paris.png")
		self.NewYork = pygame.image.load("ASSETS/New York.png")
		self.Tokyo = pygame.image.load("ASSETS/Tokyo 2.png")
		self.johannesburg = pygame.image.load("ASSETS/Johannesburg.png")
		self.Berlin = pygame.image.load("ASSETS/Berlin.png")

		#make all the images the same size
		self.London = pygame.transform.scale(self.London,(130,100))
		self.Paris = pygame.transform.scale(self.Paris,(130,100))
		self.NewYork = pygame.transform.scale(self.NewYork,(130,100))
		self.Tokyo = pygame.transform.scale(self.Tokyo,(130,100))
		self.johannesburg = pygame.transform.scale(self.johannesburg,(130,100))
		self.Berlin = pygame.transform.scale(self.Berlin,(130,100))

		#buttons
		self.L = self.display.blit(self.London,(30,40))
		self.P = self.display.blit(self.Paris,(190,40))
		self.N = self.display.blit(self.NewYork,(350,40))
		self.T = self.display.blit(self.Tokyo, (30,180))
		self.J = self.display.blit(self.johannesburg, (190,180))
		self.B = self.display.blit(self.Berlin, (350,180))

		#text
		font = pygame.font.Font(None, 20)
		text = font.render("Please select your desired location",1,(10,10,10))
		self.display.blit(text, (28,12))
		
		pygame.display.flip()

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
						self.mapSelected = "ASSETS\staticmapLondon.png" # what will be referenced later to know what map to use.
						#treasurePos(mapSelected)
					elif x>190 and x<320 and y>40 and y<140:
						print "Paris Clicked"
						mapSelected = "ASSETS\staticmapParis.png"
						#treasurePos(mapSelected)
					elif x>350 and x<480 and y>40 and y<140:
						print "New York Clicked"
						self.mapSelected = "ASSETS\staticmapNewYork.png"
						#treasurePos(mapSelected)
					elif x>30 and x<160 and y>180 and y<280:
						print "Tokyo Clicked"
						self.mapSelected = "ASSETS\staticmapTokyo.png"
						#treasurePos(mapSelected)
					elif x>190 and x<320 and y>180 and y<280:
						print "Johannesburg Clicked"
						self.mapSelected = "ASSETS\staticmapJohannesburg.png"
						#treasurePos(mapSelected)
					elif x>350 and x<480 and y>180 and y<280:
						print "Berlin Clicked"
						self.mapSelected = "ASSETS\staticmapBerlin.png"
						#treasurePos(mapSelected)
					else:
						print "not on button"

					
map1 = mapSelect()
map1.mapPanel()



