#Treasures class. Inherits from entity class. Uses base treasure class.



class treasure(pygame.sprite.Sprite, entity): #I mocked up a treasure class, we can pull it from the other one

	def __init__(self): #initialise it
		pygame.sprite.Sprite.__init__(self) #no idea why i need it, but i need it
		self.name = "" #give that dubbloon a name
		self.image = pygame.image.load('ASSETS/testTreasure.png') #and a picture
		self.rect = self.image.get_rect() #get yourself a rectangle
		self.rect.x = 0 #x coord of the treasure
		self.rect.y = 0 #y coord of the treasure
		self.points = 0 #points the treasure is worth
		self.location = 0 #location in Sorting inventory list yeah
		self.locationInListX = 0 #stores location user gives it in city list.
		self.locationInListY = 0 #stores location user gives it in city list.

	

