#File containing some stuff for a sorting thingy


class node:
    def __init__(self, value, coords, connected):
        self.value = value
        self.coords = coords
        self.connected = connected



class djistras:

    def __init__(self, arena_copy, targets):
        self.targets = targets
        self.arena = arena_copy
        self.row_length = self.arena.ret_size[1]
        self.column_height = self.arena.ret_size[0]
        self.graph = convert_arena(arena)

    def convert_arena(self, arena):
        for row in self.arena:
            for col in row:
                coords_to_nodes(self.arena, row, col)



    def coords_to_node(self, arena, x, y): 
        node = (y-1)*self.row_length+x
        return node

    def find_connected(self, x, y)
        con = []
        if arena[x][y] == 1 or arena[x][y] == 2:
            if arena[x-1][y] == 1 or arena[x-1][y] == 2:
                con.append(((x-1,y), coords_to_nodes(self.arena,x-1,y))
            if arena[x+1][y] == 1 or arena[x+1][y] == 2:
                con.append((x+1,y), coords_to_nodes(self.arena,x+1,y)
            if arena[x][y-1] == 1 or arena[x][y-1] == 2:
                con.append((x,y-1), coords_to_nodes(self.arena,x,y-1)
            if arena[x][y+1] == 1 or arena[x][y+1] == 2:
                con.append((x,y+1), coords_to_nodes(self.arena,x,y+1)
        else:
            print str(x)+" "+str(y)+" Is not a road"







