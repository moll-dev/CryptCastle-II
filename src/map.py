class Map(object):
    height = 1000
    width = 1000
    grid = [[None for x in range(width)]for y in range(height)]

    def __init__(self):
        pass

    def getRoom(self, x,y):
        return self.grid[x][y]

class Room(object):
    contents = [None]

    def __init__(self, name, description):
        self.name = name
        self.description = description


castle = Room("Castle","Herpderp")

castle.contents[0] = "Spatula"









map = Map()
map.grid[10][10] = "Outhouse"
print map.grid[10][10]
print map.grid[10][11]
print castle.contents[0]
castle.contents.append("Spoon")
print castle.name

