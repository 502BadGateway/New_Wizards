def insertionSort(aList):
  for index in range(1, len(aList)):
    currentvalue = aList[index]
    position = index
    while position > 0 and currentvalue < aList[position - 1]:
      aList[position] = aList[position - 1]
      position -= 1
    aList[position] = currentvalue
#SWAPPING THE NUMBERS
#currentvalue = aList[0]
#aList[0] = aList[5]
#aList[5] = currentvalue
aList = [0, 1, 2, 3, 4, 5, 6, 7]
insertionSort(aList)
print(aList)
