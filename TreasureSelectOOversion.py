class treasureSelect():
	def __init__(self,treasureName,buttonX,buttonY,imageLocation,buttonHeight,buttonWidth):
		self.treasureName = pygame.image.load(imageLocation)
		self.treasureName = pygame.transform.scale(self.treasureName,(buttonHeight,buttonWidth))
		self.display.blit(self.treasureName,(buttonX,buttonY)