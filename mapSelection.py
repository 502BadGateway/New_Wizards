import pygame
class mapSelect():
	def __init__(self,cityName,buttonX,buttonY,imageLocation,buttonHeight,buttonWidth):
		self.cityName = cityName
		self.buttonX = buttonX
		self.buttonY = buttonY
		self.imageLocation = imageLocation
		self.buttonHeight = buttonHeight
		self.buttonWidth = buttonWidth		



		def cityText(self,textFont,textSize,textLocationX,textLocationY,textStatment,textColour):
			self.font = pygame.self.font.Font(textFont, textSize)
			self.text = self.font.render(textStatment,1,textColour)
			self.display.blit(self.text,(textLocationX,textLocationY))