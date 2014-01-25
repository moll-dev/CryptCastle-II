from Tkinter import *
from ttk import Style

class Engine():

    def __init__(self, parent):
        self.commandstr =""
        self.parent = parent
        self.command = Command("test", "test")
        self.guy = Player()

    def step(self):
        command = Command(self.commandstr.split())
        self.do(command)

    def do(self, command):
        self.consolePrint(command.verb)

    def consolePrintln(self,str):
        self.parent.consoleText.configure(state='normal')
        self.parent.consoleText.insert(INSERT,str)
        self.parent.consoleText.insert(END, "\n")
        self.parent.consoleText.see(END)
        self.consoleText.configure(state='disabled')

    def consolePrint(self,str):
        self.parent.consoleText.configure(state='normal')
        self.parent.consoleText.insert(INSERT,str)
        self.parent.consoleText.see(END)
        self.parent.consoleText.configure(state='disabled')

class Command(object):

        def __init__(self,*args):
            self.args = args
            self.verb = args[0]
            self.object = args[1]

            print self.verb
            print self.object

class Player(object):
    hp = 100
    stm = 100


    loc =[0,0]
    map = "ballz"
    room = "room"
    inv =[]

    def move(self,direction):
        self.loc[0] += 1
        self.loc[1] += 1

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

e = Engine(None)
e.commandstr="run west"
command = e.commandstr.split()
bucket = Bucket()
adventurer = Player()
adventurer.take(bucket)
print adventurer.inv[0].name