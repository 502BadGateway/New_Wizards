class BubbleSorting():

	def run(treasureList):

		for passnum in range(len(treasureList)-1,0,-1):
			for i in range(passnum):
				if treasureList[i].points > treasureList[i + 1].points:
					theSortBot.swap(i, i + 1)