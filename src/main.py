#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
from ttk import Style

from gui import *
from engine import *

bgcolor = "grey26"
bgtext  = "grey13"
fgtext  = "dark goldenrod"

def parse_command(string):
    print string

def main():

    window = Tk()

    window.geometry("800x600+300+300")
    window.resizable(width=FALSE, height=FALSE)

    game = gui(window)
    try:
        window.wm_iconbitmap("cc2.ico")
        window.mainloop()
    except TclError:
        print 'No ico file found'
    game.mainloop()




    #print game.consoleText.get(first,last)


if __name__ == '__main__':
    main()
