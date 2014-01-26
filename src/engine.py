from Tkinter import *
from ttk import Style
from map import *

class Engine():

    def __init__(self, parent):
        self.commandstr =""
        self.parent = parent
        self.guy = Player()
        self.command = ""


    def step(self):
        self.do(self.command)

    def do(self, command):
        self.consolePrintln(command)

    def consolePrintln(self,str):
        self.parent.consoleText.configure(state='normal')
        self.parent.consoleText.insert(INSERT,str)
        self.parent.consoleText.insert(END, "\n")
        self.parent.consoleText.see(END)
        self.parent.consoleText.configure(state='disabled')

    def consolePrint(self,str):
        self.parent.consoleText.configure(state='normal')
        self.parent.consoleText.insert(INSERT,str)
        self.parent.consoleText.see(END)
        self.parent.consoleText.configure(state='disabled')

    def loadMap(self,file):
        world1xml = xml.dom.minidom.parse(file)
        root = world1xml.getElementsByTagName("World")[0]
        worldattrs = dict(root.attributes.items())
        self.world = World(worldattrs)

        maps = world1xml.getElementsByTagName("Map")
        attrs = dict(maps[0].attributes.items())

        for x in range(root.getElementsByTagName("Map").length):
            mapattrs = dict(maps[x].attributes.items())
            loc = map(int,mapattrs['loc'].split())
            self.world.appendMap(mapattrs)
            for y in range(maps[x].getElementsByTagName("Room").length):
                roomattrs = dict(maps[x].getElementsByTagName("Room")[y].attributes.items())
                loc = map(int,mapattrs['loc'].split())
                self.world.grid[loc[0]][loc[1]].appendRoom(roomattrs)

class Command(object):
        def __init__(self,string):
            self.string = string


class Player(object):
    hp = 100
    stm = 100


    loc =[0,0]
    map = "map"
    room = "room"
    inv =[]

    def move(self,direction):
        self.loc[0] += 1
        self.loc[1] += 1
        self.room = map.getroom(self.loc[0],self.loc[1])

    def warp(self,map):
        pass

    def take(self,item):
        self.inv.append(item)

    def drop(self,item):
        pass

    def look(self,item):
        pass

class Item(object):
    pass
class Bucket(Item):

    def __init__(self):
        self.name = "Bucket"
        self.desc = "It's a bucket"

#TEST CODE
