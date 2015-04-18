treasureList = [18,48,12,15,11,47]  #list of numbers


class  mergesort: #initiates class

    def run(self, treasureList): #
        print(treasureList) #prints list
        if len(treasureList)>1: #if function, if the treasure list is bigger than 1....
            mid = len(treasureList)//2 #divide list by 2
            lefthalf = treasureList[:mid] #merge
            righthalf = treasureList[mid:] #merge

            self.run(lefthalf) 
            self.run(righthalf)

            i=0 
            j=0 
            k=0 
            while i<len(lefthalf) and j<len(righthalf): #while 0 is smalller than left half and 0 is smaller than right half 
                if lefthalf[i]<righthalf[j]: #if left half is smaller than right half
                    treasureList[k]=lefthalf[i] #merge
                    i=i+1 #increments i
                else: # or else
                    treasureList[k]=righthalf[j] #merge
                    j=j+1 #increments j
                k=k+1 #increments k

            while i<len(lefthalf): #loop, id 0 is smaller than left half
                treasureList[k]=lefthalf[i] #merge
                i=i+1 #increments i 
                k=k+1 #increments k

            while j<len(righthalf): #loop, if 0 is smaller than right half
                treasureList[k]=righthalf[j] # then merge
                j=j+1 #increments j
                k=k+1 #increments k
        print(treasureList) #prints sorted list

#sort = mergesort() #call

#sort.run(treasureList) 
