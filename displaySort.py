import pygame 


class displaySort:

	def __init__(self):
		pygame.init()
		screen = pygame.display.set_mode((1280,720))
		self.background = pygame.image.load('ASSETS/setSortBackground.png')
		self.display.set_caption("Sorting the Treasures!")
		self.setSortBackground()


    def setSortBot(self, sortBot): #blits sortbot
        self.display.blit(sortBot.image, (sortBot.rect.x, sortBot.rect.y)) #blits it at its rect location

    def setSorttreasure(self, sortBot, treasureList):
        for i in treasureList:
            self.display.blit(i.image, (i.rect.x, i.rect.y)) #blits treasure on screen

    def setSortBackground(self):
        self.blit(self.background, (0,0))