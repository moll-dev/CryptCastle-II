#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
from ttk import Style
from gui import *

bgcolor = "grey26"
bgtext  = "grey13"
fgtext  = "dark goldenrod"

def parseCommand(string):
    print string

def main():

    window = Tk()
    window.geometry("800x600+300+300")
    game = gui(window)

    # game.bind("<Return>", parseCommand(game.entryText.))

    game.statText.config(text='Time!')

    #print game.consoleText.get(first,last)
    window.mainloop()

if __name__ == '__main__':
    main()
