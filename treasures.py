#Treasures class. Inherits from entity class. Uses base treasure class.



class treasure(pygame.sprite.Sprite, entity): #I mocked up a treasure class, we can pull it from the other one

	def __init__(self, name, val, image, x, y, points): #initialise it
        entity.__init__(self, name, val) #Call the base class constructor. This is because this constructor should be extending not replacing functionality in entity._init__. 
                                         #See here for information on this: Paragraph 6  https://docs.python.org/2/tutorial/classes.html#inheritance

        #TODO MAKE THE MEMBER VARIABLES PRIVATE BY ADDING __ TO THE START OF THE VARIABLE NAME
        #TODO ONCE THE ABOVE IS DONE, ADD GETTER METHODS FOR ALL RELEVENT VARIABLES THAT MIGHT BE NEEDED TO BE RETREIVED FROM OUTSIDE THIS CLASS.
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

	

