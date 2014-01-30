from Tkinter import *
from ttk import Style
from map import *

class Engine():
    turncount = 0

    def __init__(self, parent):
        self.commandstr ="verb object"
        self.parent = parent
        self.command = Command(self.commandstr)

    def initPlayer(self):
        self.user = Player(self, [5,5],[2,2],None)

    def step(self):
        self.turncount += 1
        self.do()

    def do(self):
        command = self.command
        player = self.user

        runverbs  = {'g','travel','run', 'go', 'move','walk','climb'}
        takeverbs = {'t','take','pickup','grab'}
        dropverbs = {'d','drop','leave','toss'}
        lookverbs = {'x','examine','look'}
        helpverbs  = {'h','help', 'help!'}
        verbs = (runverbs,takeverbs,runverbs,dropverbs,lookverbs,helpverbs)

        command.update(self.commandstr)
        iskeyword = False
        for x in verbs:
            if command.verb in x:
                iskeyword=True
        if iskeyword:
            if command.object is None:
                self.consolePrintcmd(command.verb)
            else:
                self.consolePrintcmd(command.verb+" "+command.object)
        else:
            self.consolePrintcmd(self.commandstr)
            self.consolePrintln("I don't understand that verb.")

        #Verb Break down!
        if command.verb in runverbs:
            if self.command.object is None:
                self.consolePrintln(command.verb.capitalize()+" where?")
            else:
                self.consolePrintln("You went "+command.object+".")
                player.move(command.object)

        elif command.verb in takeverbs:
            if self.command.object is None:
                self.consolePrintln(command.verb.capitalize()+" what?")
            else:
                self.consolePrintln("You took "+command.object+".")

        elif command.verb in dropverbs:
            if self.command.object is None:
                self.consolePrintln(command.verb.capitalize()+" what?")
            else:
                self.consolePrintln("You dropped"+command.object+".")

        elif command.verb in lookverbs:
            if self.command.object is None:
                self.consolePrintln(command.verb+" where?")
            else:
                self.consolePrintln("You ran!")
                player.move(command.object)
            self.consolePrintln("You looked at that!")

        elif command.verb in helpverbs:
            self.consolePrintln("Put help stuff here")

        self.consolePrintln("")

    def consolePrintln(self,str):
        self.parent.consoleText.configure(state='normal')
        self.parent.consoleText.insert(INSERT,str)
        self.parent.consoleText.insert(END, "\n")
        self.parent.consoleText.see(END)
        self.parent.consoleText.configure(state='disabled')

    def consolePrintcmd(self,str):
        self.parent.consoleText.configure(state='normal')
        self.parent.consoleText.insert(INSERT,"> "+str)
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

        regions = world1xml.getElementsByTagName("Map")
        attrs = dict(regions[0].attributes.items())

        for x in range(root.getElementsByTagName("Map").length):
            mapattrs = dict(regions[x].attributes.items())
            loc = map(int,mapattrs['loc'].split())
            self.world.appendRegion(mapattrs)
            for y in range(regions[x].getElementsByTagName("Room").length):
                roomattrs = dict(regions[x].getElementsByTagName("Room")[y].attributes.items())
                loc = map(int,mapattrs['loc'].split())
                self.world.grid[loc[0]][loc[1]].appendRoom(roomattrs)

class Command(object):
        def __init__(self,string):
            self.string = string
            self.commandlst = string.split()
            self.verb = self.commandlst[0]
            self.object = self.commandlst[1]

        def update(self,string):
            self.string = string
            self.commandlst = string.split()

            try:
                if len(self.commandlst) == 1:
                    self.verb = self.commandlst[0].lower()
                    self.object = None
                    return None
                else:
                    self.verb = self.commandlst[0].lower()
                    self.object = self.commandlst[1].lower()
                    return True
            except IndexError:
                self.verb = ""
                self.object = ""
                return False

class Player(object):
    hp = 100
    stm = 100

    loc =[0,0]
    region = "map"
    room = "room"
    inv =[]

    def __init__(self, parent, map, room, inv):
        self.parent = parent
        self.region = self.parent.world.grid[map[0]][map[1]]
        self.room = self.region.grid[room[0]][room[1]]
        self.inventory = inv

    def move(self,direction):
        self.loc[0] += 1
        self.loc[1] += 1
        self.room = self.region.getRoom(self.loc[0],self.loc[1])

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
