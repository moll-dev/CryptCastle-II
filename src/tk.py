import Tkinter

#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
from ttk import Style

bgcolor = "grey26"
bgtext  = "grey13"
fgtext  = "dark goldenrod"

class gui(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("[ Crypt & Castle II ]")
        self.style = Style()
        self.style.theme_use("clam")
        self.config(bg=bgcolor)
        self.pack(fill=BOTH, expand=1)

        topFrame = Frame(self, relief=FLAT, borderwidth=1,bg=bgcolor)
        topFrame.pack(fill=BOTH,expand=1)

        self.statText = Label(topFrame,fg=fgtext, bg="RoyalBlue4", justify=LEFT,
                              font=("System",12),relief=SUNKEN,bd=5,height=1,
                              )#selectbackground="RoyalBlue4")
        self.statText.pack(fill=X,padx=6,expand=1,pady=4)
        #self.statText.configure(state='disabled')

        consoleFrame = Frame(topFrame, relief=FLAT, borderwidth=1, bg=bgcolor)       #Top Frame
        consoleFrame.pack(fill=X, expand=1)

        consoleText = Text(consoleFrame,bg=bgtext,relief=SUNKEN,bd=5,height=31,width=30)
        consoleText.pack(fill=X,expand=1,side=LEFT,padx = 6, pady=4)
        consoleText.configure(state='disabled')

        objectText = Text(consoleFrame,bg="DodgerBlue4",relief=SUNKEN,bd=5,
                          height=31,width=15,selectbackground="DodgerBlue4")
        objectText.pack(side=RIGHT,padx=5)
        objectText.configure(state='disabled')

        #Lower Gui Bar
        promptLabel = Label(self,text=">",font=("System",17),
                            bg=bgcolor,fg="gold",justify=RIGHT)
        promptLabel.pack(side=LEFT, padx=2)

        s = u'\u21A9'
        text = "Enter "+s
        self.enterButton = Button(self, text=text,font=("System",12),
                             bg="tomato4",fg="light goldenrod",
                             activebackground=fgtext, command=self.OnPressEnter)
        self.enterButton.pack(side=RIGHT, padx=6, pady= 6)

        self.command = Tkinter.StringVar()
        self.entryText   = Text(self, relief=SUNKEN, height=1,
                           selectborderwidth=2, width=120,
                           font=("System",16), bd=4, bg="gray13",
                           selectbackground="gray23",
                           fg=fgtext)
        self.entryText.pack(side=LEFT,padx=0)

        self.entryText.bind("<Return>", self.OnPressEnter)

    def OnPressEnter(self,event):
        self.statText.config(bg=fgtext)
        self.labelVariable.set(self.entryText.get())

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
