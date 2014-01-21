from Tkinter import *
from ttk import Style
from engine import *

bgcolor = "grey26"
bgtext  = "grey13"
fgtext  = "dark goldenrod"

'''
    The purpose of this file (I know gui is a misnomner) is to create a
    gui for the game and provide hooks and interupts into the lower levels
    of the game. Like the engine object.







'''
class gui(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent)
        self.command = ""
        self.parent = parent
        #e = engine()
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

        self.consoleText = Text(consoleFrame,bg=bgtext,relief=SUNKEN,bd=5,height=31,width=30,
                           fg=fgtext)
        self.consoleText.pack(fill=X,expand=1,side=LEFT,padx = 6, pady=4)
        self.consoleText.configure(state='disabled')

        self.objectText = Label(consoleFrame,bg="DodgerBlue4",relief=SUNKEN,bd=5,
                          height=15,width=20)#,selectbackground="DodgerBlue4")
        self.objectText.pack(side=TOP,padx=5,pady=5)


        self.invText = Label(consoleFrame,bg="DodgerBlue4",relief=SUNKEN,bd=5,
                          height=16,width=20)#,selectbackground="DodgerBlue4")
        self.invText.pack(side=BOTTOM,padx=5,pady=5)

        #Lower Gui Bar
        promptLabel = Label(self,text=">",font=("System",17),
                            bg=bgcolor,fg="gold",justify=RIGHT)
        promptLabel.pack(side=LEFT, padx=2)

        s = u'\u21A9'
        text = "Enter "+s
        self.enterButton = Button(self, text=text,font=("System",12),
                             bg="tomato4",fg="light goldenrod",
                             activebackground=fgtext, command=self.OnButtonPress)
        self.enterButton.pack(side=RIGHT, padx=6, pady= 6)

        self.entryText   = Entry(self, relief=SUNKEN,
                           selectborderwidth=2, width=120,
                           font=("System",16), bd=4, bg="gray13",
                           selectbackground="gray23",
                           fg=fgtext)
        self.entryText.pack(side=LEFT,padx=0)

        self.entryText.bind("<Return>", self.OnPressEnter)

    def OnPressEnter(self,event):
        self.statText.config(bg=fgtext)
        self.command =self.entryText.get()
        self.consoleText.configure(state='normal')
        self.consoleText.insert(INSERT,self.command)
        self.consoleText.configure(state='disabled')

    def OnButtonPress(self):
        self.statText.config(bg=fgtext)
        self.command = self.entryText.get()
        #Parse the text

        #step


        self.consoleText.configure(state='normal')
        self.consoleText.insert(INSERT,self.command)
        self.consoleText.configure(state='disabled')
