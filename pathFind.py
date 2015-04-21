#File containing some stuff for a sorting thingy


class node:
    def __init__(self, value, coords, connected):
        self.value = value
        self.coords = coords
        self.connected = connected



class djistras:

    def convert_arena(self, arena):
        graph = []
        x = 0
        y = 0
        nodeVal = 0
        
        maxX = self.row_length
        maxY = self.column_height
        print maxX,maxY
        for row in self.arenacopy:
            for col in row:
                con = self.find_connected(self.arenacopy, x,y, maxX, maxY)
                nodeVal = self.coords_to_node(x, y)
                graph.append(node(nodeVal,(x,y), con))
                y+=1
                #nodeVal+=1
            y = 0
            x += 1

        for nd in graph:
            pass
        return graph




    def coords_to_node(self,y, x): 
        print y,x
        if y == 0 or y == 1:
            print "wtf"
            node = x
        else:
            node = (y-1)*self.row_length+x
        print node
        return node

    def find_connected(self, arena, x, y,  maxX, maxY):
        con = []
            #print x,y
        if arena[x][y] == 1 or arena[x][y] == 2:
            if x >= 1:
               if arena[x-1][y] == 1 or arena[x-1][y] == 2:
                    con.append(((x-1,y), self.coords_to_node(x-1,y)))
            if x < maxX-1:
                if arena[x+1][y] == 1 or arena[x+1][y] == 2:
                    con.append(((x+1,y), self.coords_to_node(x+1,y)))
            if y >= 1:
                if arena[x][y-1] == 1 or arena[x][y-1] == 2:
                    con.append(((x,y-1), self.coords_to_node(x,y-1)))
            if y < maxY-1:
                if arena[x][y+1] == 1 or arena[x][y+1] == 2:
                    con.append(((x,y+1), self.coords_to_node(x,y+1)))
            return con
        else:
            #print str(x)+" "+str(y)+" Is not a road"
            return None
        #print "Node "+str(x)+" "+str(y)+" Is connected to: "+ str(con)


    def __init__(self, arena, targets):
        self.targets = targets  #get targets
        self.arenainst = arena  #Get instance
        self.arenacopy = self.arenainst.ret_arena_copy()    #Get copy of arena
        self.row_length = arena.ret_size()[1]   #get sizes
        self.column_height = arena.ret_size()[0]
        self.graph = self.convert_arena(arena)
