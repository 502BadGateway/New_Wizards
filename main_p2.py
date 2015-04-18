#
#   This file should contain code which brings all the sections together and ties everything into the project.
#   This file should be the only file to be run.
#

import pygame
from pygame.locals import * #this is needed for quit sequence.
import sys #this is also needed for quit sequence
import wikipedia #this is for displaying treasure info
import gen_arena
from robot import Robot
import random
import display
import time

 

def findRobotLocation(ar, name, robotList, targetX, targetY):
    width = ar.ret_size()[0]-1        #Get the width and heights of the array
    height = ar.ret_size()[1]-1

    print "Using width:"+str(width) #dbg
    print "Using height:"+str(height)
    
    placed = False                  #Store if we've placed anything
    x = 0
    rand_row = random.randint(0,height) #Pick a random row to spawn a trafficlight

    while x <= width-1 or placed != True:   #While we havent looked at every item in the row, and havent placed a light
        if ar.ret_element_value(rand_row, x) == 1 or ar.ret_element_value(rand_row, x) == 2:    #Check that the item we're on is a road.
            print "ROBOT:"
            print rand_row, x
            bot = Robot(name, rand_row, x, ar,targetX, targetY)                                    #Create a new robot!
            robotList.append(bot)
            ar.put(rand_row, x, 5)                                                            #Save it in the arena
            placed = True                       #Move on
            break
        x += 1
    return robotList 


def main():

    clock = pygame.time.Clock()
    #Create an instance of the pygeo class.
    #Doing selfso will call the constructor of the pygeo class.

    mapName = "map1"
    lights = []
    landmarks = []
    landmarkslist = [6,7,8,9,10,11,12,13,14,15,16,17,18]    #list of numbers for landmarks TODO need to assotiate the right numbers with the right landmarks

    robotList = []          #List of instances of the robot

    geo = pygeo.Geo(mapName)
    geo.GetsScreenshot()
    #Should now be an image called map1.png in the current directory
    arena = gen_arena.arena(mapName+".png") 
    arena.show_arena()
    landmarks = insertLandmarks(arena, landmarks, len(landmarkslist), landmarkslist, landmarkInfo)
    arena.show_arena()
    
    rand_landmark_num = random.randint(0, len(landmarks)) #Choose a random landmark as a target
    rand_landmark = landmarks[rand_landmark_num]


    robotList = findRobotLocation(arena, "paul", robotList, rand_landmark.locationX, rand_landmark.locationY)      #Add new robot.

    arena.show_arena()

    window = display.display(str(mapName)+".png")    #Create display
    song = pygame.mixer.Sound('backgroundMusic.ogg') #creates an instant of the music
    song.play() #plays the music		 #song.play() plays the music
    while pygame.event.peek((pygame.QUIT, pygame.KEYDOWN)) != True:         #Loop forever until either QUIT or KEYDOWN. TODO Change this to something better. Like a key press of Q or something. Will do for now
        clock.tick()

        
        for i in treasures:
            window.setLandmark(i.locationX, i.locationY, i.image)

        for i in robotList:
            landmark = i.passbyLandmark(arena)      #Check for landmarks around the robot
            if landmark != None:                          #If we found one, then render it's info text
                window.drawWikiText(passbyLandmark[0], passbyLandmark[1], passbyLandmark[2])

        window.render()
        print clock.get_fps()
    return


main()


#   IGNORE
#   Just  noting how i envision the robot loopy section to work 
#   Just here so i remember what i was going to do once Dna submits work from Jan 27th. - Sam
#   for i in robotList:
#       passedLadmark = i.passbyLandmark()
#       if passedLandmark != True:
#           i.move()
#
