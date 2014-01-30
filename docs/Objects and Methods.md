# Objects and You:
These are all subject to change! Although Tom will update this as he adds new methods :)
###Engine Objects:
  
Player():
Needs to be initialized with a dictionary of values, these include:

name,desc,size.
Example in python: 
```python
attributes = {'name': 'World1', 'desc': 'This is a world'}
```

###Gui Objects:

###gui():
Needs to be initialized with just a parent (which should be a tkinter window).
      
```python
#Python Example
#Create a new gui object with 'window' as it's parent
game = gui(window)
```
Also when a new gui object is created, it executes the following methods: 

>self.e = Engine(self), gui.initUI(), engine.loadMap, and engine.initPlayer

----

####gui.initUI()

Takes no parameters, this method is here simply to setup the buttons and text boxes that make CCII run.
It creates the following objects:

>statText, consoleText, objectText, invText, entryText, and the enterButton

This method is run during the creation of a new gui object.

---

####gui.initColor()
This method currently isn't being used, but in the future it should add the ability to color text and make cool sequences

---

###World Objects:

######World():
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

######Map():
needs to be initialized just like World with these values:
loc, name, desc, contents, exits
    

