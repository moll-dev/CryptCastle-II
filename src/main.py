#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import Style

from gui import *
from engine import *

def main():
    window = Tk()

    window.geometry("800x600+560+150")
    game = gui(window)
    try:
        window.wm_iconbitmap("cc2.ico")
        window.mainloop()
    except TclError:
        print 'No ico file found'

    game.mainloop()

if __name__ == '__main__':
    main()
