import pygame
import wikipedia
import inputbox

#Creates display and handles all the functionality of drawing to the display.
#Functions get given data from other displayable objects 


class display:      #Class which handles all the display functionality.
    def __init__(self,backgroundImage, screenHeight,screenWidth): #Creates a display 
        if pygame.version.vernum[2] == 2:   #conditional import if pygame freetype is avalible
            from pygame import freetype
            def fontInit():
                pygame.freetype.init()
                self.defaultFont = pygame.freetype.Font(None, 28)          #
                
        else:
            def fontInit():
                pygame.font.init()
                self.defaultFont = pygame.font.Font(None, 28)          #

        pygame.init()
       #self.size = screenHeight,screenWidth
        self.size= (pygame.display.Info().current_w,pygame.display.Info().current_h)
        self.display = pygame.display.set_mode(self.size, pygame.HWSURFACE|pygame.FULLSCREEN)     #Set the screen up
        self.center = (0,0,0,0)                                   #Center of the viewport

        #DATA --------------
        if backgroundImage != False:
            print backgroundImage
            self.background = pygame.Surface(self.size)
            self.background.fill((255,255,255))
            self.image = pygame.image.load(backgroundImage) #Load the background image 
            self.backgroundRect = self.image.get_rect() #Get the the background rectangle
            self.size = self.background.get_size()          #Get dimentions of the window
            self.__screenDimentions = (screenHeight,screenWidth)
        
        elif backgroundImage == False:
            self.image = pygame.Surface(self.display.get_size())
            self.background = pygame.Surface(self.display.get_size())
            self.backgroundRect = self.size 
            self.background = self.background.convert()
            self.background.fill((250,250,250))
            self.display.blit(self.background,(0,0))

        self.State = False
        fontInit()                              #Initialise fonts

        return

    def fillDisplay(self,screenHeight,screenWidth,colour):
        self.display = pygame.display.set_mode(screenHeight,screenWidth)
        self.background = pygame.Surface(self.display.get_size)
        self.background = self.background.convert(colour)
        self.display.blit(self.background,(0,0))

    def addMapSelectBtn(self, btn):
        cityName = pygame.image.load(btn.imageLocation)
        cityName = pygame.transform.scale(cityName,(btn.buttonHeight,btn.buttonWidth))
        self.display.blit(cityName,(btn.buttonX,btn.buttonY))

    def addTreasureBtn(self, btn):
        treasureName = pygame.image.load(btn.imageLocation)
        treasureName = pygame.transform.scale(treasureName,(btn.buttonHeight,btn.buttonWidth))
        self.display.blit(treasureName,(btn.buttonX,btn.buttonY))
        
    def addSortSelectBtn(self, btn):
        sortName = pygame.image.load(btn.imageLocation)
        self.display.blit(sortName,(btn.buttonX,btn.buttonY))

    def pictureDisplay(self,screenHeight,screenWidth,backgroundImage):
        self.display = pygame.display.set_mode(screenHeight,screenWidth)
        self.background = pygame.image.load(backgroundImage)
        self.display.blit(self.background,(0,0))

    def setCollectorBot(self,x,y,image, pygame_im=False):   #Set the location of the robot
        if pygame_im == False:                          #If we're not giving a pygame surface
            robot_image = pygame.image.load(image)  #Load the image
        else:
            robot_image = image
        robot_image = pygame.transform.scale(robot_image, (20,20))
        self.display.blit(robot_image, (y*10, x*10))
        self.State = False
        return 

    def setTreasureCollect(self,x,y,image, pygame_im=False):    #Set the location of the landmark
        if pygame_im == False:                          #If we're not giving a pygame surface
            treasure_image = pygame.image.load(image)  #Load the image
        else:
            treasure_image = image
        treasure_image = pygame.transform.scale(treasure_image, (20,20))
        self.display.blit(treasure_image, (y*10, x*10))
        self.State = False
        return


    def textInput(self,prompt):
        text = inputbox.ask(self.display, prompt)
        return text



    def showPoints(self, font, text, position):
        return

    def render(self):                #Render currently buffered scene
        if self.State == False:      #If the state is dirty
            pygame.display.flip()                                       #Flip buffers.
            self.background.blit(self.image,(0,0))
            self.display.blit(self.background, (0,0))     #Blit background

        self.state = True
        return

    def CreateText(self, landInfo, positionVar, padding, fontsize=15, bg=None):

        if padding != 0:
            positionVar = (positionVar[0]+padding, positionVar[1]+padding, positionVar[2]+padding, positionVar[3]+padding)

        self.state = False
        textFont = pygame.font.Font(None,20)
        if bg != None:
            infoText = textFont.render(str(landInfo),True,(10,10,10),bg)
        else:
            infoText = textFont.render(str(landInfo),True,(10,10,10))

        textPos = pygame.Rect(positionVar) #positionVar needs to be given to this method, it should be in the format "600,10,0,0" and "600,30,0,0"
        self.display.blit(infoText, textPos)
    
    def RobotPoints(self,robotScore,positionVar): #this should display pauls points but im not sure if this needs to be done for both robots

        self.state = False
        scoreFont = pygame.font.Font(None,30)
        scoreText = scoreFont.render(str(robotScore),1,(10,10,10))
        textPos = pygame.Rect(positionVar) #positionVar needs to be given to this method, it should be in the format "600,10,0,0" and "600,30,0,0"
        self.display.blit(scoreText, textPos)

    def drawWikiText(self, landmarkName, positionVar):
        infoText = wikipedia.summary(landmarkName, sentences = 2)        #Get the info text
        rect = pygame.Rect(positionVar[0],positionVar[1], 480-positionVar[0], 640-positionVar[1])
        landmarkVar = landmarkName                                     # this is what will search wikipedia
        font = pygame.font.Font(None, 20) #this is the font handed to the render_textrect method
        textSurface = self.render_textrect(infoText, font, rect, (0,0,0), (0,0,2)) # this calls the method that does the word wrap, this may need to be modified becuse I think it will create a new display.
        textSurface.set_colorkey((0,0,2))
        self.display.blit(textSurface, rect)
        self.state = False

    def returnScreenSizes(self):
        return self.__screenDimensions


    def render_textrect(self,landInfo, font, rect, text_color, background_color, justification=0): #this code will wordwrap text for you IT IS NOT MINE it is from "http://www.pygame.org/pcr/text_rect/index.php"

        import pygame
        
        final_lines = []
        requested_lines = landInfo.splitlines()

        # Create a series of lines that will fit on the provided
        # rectangle.

        for requested_line in requested_lines:
            if font.size(requested_line)[0] > rect.width:
                words = requested_line.split(' ')
                # if any of our words are too long to fit, return.
                for word in words:
                    if font.size(word)[0] >= rect.width:
                        raise TextRectException, "The word " + word + " is too long to fit in the rect passed."
                # Start a new line
                accumulated_line = ""
                for word in words:
                    test_line = accumulated_line + word + " "
                    # Build the line while the words fit.    
                    if font.size(test_line)[0] < rect.width:
                        accumulated_line = test_line 
                    else: 
                        final_lines.append(accumulated_line) 
                        accumulated_line = word + " " 
                final_lines.append(accumulated_line)
            else: 
                final_lines.append(requested_line) 

        # Let's try to write the text out on the surface.

        surface = pygame.Surface(rect.size) 
        surface.fill(background_color) 

        accumulated_height = 0 
        for line in final_lines: 
            if accumulated_height + font.size(line)[1] >= rect.height:
                raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
            if line != "":
                tempsurface = font.render(line, 1, text_color)
                if justification == 0:
                    surface.blit(tempsurface, (0, accumulated_height))
                elif justification == 1:
                    surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
                elif justification == 2:
                    surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
                else:
                    raise TextRectException, "Invalid justification argument: " + str(justification)
            accumulated_height += font.size(line)[1]

        return surface


#dis = display("map1.png")  #dbg
