import xml.dom.minidom
from map import *

class worldimporter():
    def __init__(self,engine):
        self.parent = engine

    def importWorld(self):
        pass

world1xml = xml.dom.minidom.parse("world1.xml")


root = world1xml.getElementsByTagName("World")[0]
worldattrs = dict(root.attributes.items())
world = World(worldattrs)

maps = world1xml.getElementsByTagName("Map")
attrs = dict(maps[0].attributes.items())


for x in range(root.getElementsByTagName("Map").length):
    mapattrs = dict(maps[x].attributes.items())
    loc = map(int,mapattrs['loc'].split())
    world.appendMap(mapattrs)
    for y in range(maps[x].getElementsByTagName("Room").length):
        roomattrs = dict(maps[x].getElementsByTagName("Room")[y].attributes.items())
        loc = map(int,mapattrs['loc'].split())
        world.grid[loc[0]][loc[1]].appendRoom(roomattrs)

print world.grid[2][2].name
print world.grid[2][2].grid[1][4].name
print world.grid[5][5].name
print world.grid[5][5].grid[2][2].name









