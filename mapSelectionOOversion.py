import pygame
class mapSelect():
	def __init__(self,cityName,buttonX,buttonY,imageLocation,buttonHeight,buttonWidth,philsScreen):
		self.cityName = pygame.image.load(imageLocation)
		self.cityName = pygame.transform.scale(self.cityName,(buttonHeight,buttonWidth))
		philsScreen.blit(self.cityName,(buttonX,buttonY))



		def cityText(self,textFont,textSize,textLocationX,textLocationY,textStatment,textColour):
			self.font = pygame.self.font.Font(textFont, textSize)
			self.text = self.font.render(textStatment,1,textColour)
			self.display.blit(self.text,(textLocationX,textLocationY))