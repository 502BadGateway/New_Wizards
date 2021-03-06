from gen_arena import arena

class city():

    def __init__(self, cityName, treasuresList, gen=False, image=""):
        self.__name = cityName 
        if gen == True:
            self.arena = arena(self.__name, treasuresList, image, False, False)
        else:
            self.arena = arena(self.__name, treasuresList)   #Create a new instance of an arena in the city class.
        print( "City setup finished" )
        self.__image = self.arena.ret_image_path() 


    def ret_image_path(self):
        print self.__image
        return self.__image

    def retArena(self):
        return self.arena

    def retArenaList(self):
        return self.arena.full_arena
