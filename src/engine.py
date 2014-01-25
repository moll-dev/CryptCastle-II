from Tkinter import *
from ttk import Style

class Engine():

    def __init__(self, parent):
        self.command = ""
        self.parent = parent
        self.command = "herpderp"

    def step(commandstr):
        command = Command(commandstr)
        do(command)

    def do(self):
        self.consolePrint(self.command)


    def consolePrint(self,str):
        self.parent.consoleText.configure(state='normal')
        self.parent.consoleText.insert(INSERT,str)
        self.parent.consoleText.insert(END, "\n")
        self.parent.consoleText.see(END)
        self.parent.consoleText.configure(state='disabled')

class Command(object):

        def __init__(self,commandstr):
            words = commandstr.split()
            self.verb = words[0]
            self.object = words[1]

class Player(object):
    hp = 100
    loc =[0,0]
    def move(self,direction):
        self.loc[0] += 1
        self.loc[1] += 1

