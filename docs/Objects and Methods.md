# Objects and You:

######This readme file was created for devs to get a good understanding of the objects and their attributes and methods in CryptCastle-II. It's going to be frequesntly updated! So if you don't know where to look this is probably a good place to start. 

These are all subject to change! Although Tom will update this as he adds new methods :)
#Engine Objects

######These objects are all related to the Engine.py file and handle pretty much everything relating to the game's inner workings.

##Engine Object
This is THE object that is created by the Gui object (when initialized) and pretty much handles all behind the scenes aspects of the game.

##Engine.initPlayer()
This method creates a Player object and initializes its position and items (see player)
```python
#Player creation example
self.user = Player(self, [5,5],[2,2],None)

#Creates an object with the reference 'user' for example engine.user would be the player object
#the first parameter sets the player's parent, then its region, and room location, along with a list of items
```
##Engine.step()
Steps the engine! This is where all calculations, combat, etc will go. 

And it runs the Engine.do() command which is pretty important (see Engine.do())

##Engine.do()
This is it, the meat and potatos of the engine. This method 

##Player Object
Needs to be initialized with a dictionary of values, these include:
name,desc,size.


Example in python: 
```python
attributes = {'name': 'World1', 'desc': 'This is a world'}
```

#Gui Objects

######This section contains all the details for working with the current gui setup in CC-II, including the initilization of a new gui object, methods associated with gui, and objects as well.
##gui object
Needs to be initialized with just a parent (which should be a tkinter window).
      
```python
#Python Example
#Create a new gui object with 'window' as it's parent
game = gui(window)
```
Also when a new gui object is created, it executes the following methods: 

>self.e = Engine(self), [gui.initUI()](https://github.com/QuantumFractal/CryptCastle-II/blob/master/docs/Objects%20and%20Methods.md#guiinitui), [gui.initColor()](), engine.loadMap, and engine.initPlayer


##gui.initUI()

Takes no parameters, this method is here simply to setup the buttons and text boxes that make CCII run.
It creates the following objects:

>statText, consoleText, objectText, invText, entryText, and the enterButton

This method is run during the creation of a new gui object.


##gui.initColor()
This method currently isn't being used, but in the future it should add the ability to color text and make cool sequences


##gui.OnPressEnter()
This method does not require any parameters, and it is run when the "Enter" button is pressed. It simply runs the gui.OnButtonPress() method. (It's kind of a loop back method)

##gui.OnButtonPress()
This method does not require any parameters, but it has a very important purpose. It signals the start of a new turn, takes the data from gui.entryText via the get() method and steps the engine. The exact usages are below.
```python
def OnButtonPress(self):
  self.e.commandstr = self.entryText.get()          #Sets the engine's command string as the entry text from the user
  
  if self.entryText.get() == "exit":                #Checks if the command is to exit, then exits
    self.e.consolePrintln("Good Bye Adventurer!")   #<- With a cheeky exit note :) 
    self.parent.quit()

  elif self.e.commandstr.isspace()== True or len(self.entryText.get()) == 0:
    pass                                         #Ignores an all spaces command input
  else:
    self.entryText.delete(0,END)                 #If its normal text, then step the engine (see engine.step)
    self.e.step()
  self.entryText.delete(0,END)                   #Clears the entryText box for the next command!
```
#World Objects:

##World():
needs to be initialized with a dictionary of values, these include:
name,desc,size
      
```python
#Python Example
attributes = {'name': 'World1', 'desc': 'This is a world', 'size':'10 10'}

#Create a new world object with the attributes defined above
world1 = World(attributes)
```
```xml
XML TAG example
<World size = "10 10" name="Middle Earth" desc="hobbits are here">
</World>
```

##Map():
needs to be initialized just like World with these values:
loc, name, desc, contents, exits
    

