#Super class for sorting algorithms

class Sorter:

    def __init__(self):


    def swap(self, valOne, valTwo, list):
        tmp = None  

        tmp = list[valOne] # put first val into tmp
        list[valOne] = list[valTwo] #replace first value with second
        list[valTwo] = tmp  #replace second value with first

        return
