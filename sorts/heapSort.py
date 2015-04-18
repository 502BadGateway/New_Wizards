def heapSort(alist):
    heap = []   #New list
    for x in alist: #For every item in list of values
        heappush(h, x)  #Add that to the new heap
    return [heappop(heap) for i in range (0, len(heap))]    #For every value in our heap, get the value starting with the smallest







