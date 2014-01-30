Note: This file is written in place of the pydoc, I'm currently trying to figure out the pydoc generator
# Objects and You:
These are all subject to change! Although Tom will update this as he adds new methods :)
###World Objects:

######World():
needs to be initialized with a dictionary of values, these include:
name,desc,size
      
```python
#Python Example
attributes = {'name': 'World1', 'desc': 'This is a world', 'size':'10 10'}
```
```xml
XML example
<World size = "10 10" name="Middle Earth" desc="hobbits are here">
```

######Map():
needs to be initialized just like World with these values:
loc, name, desc, contents, exits
    
###Engine Objects:
  
Player():
needs to be initialized with a dictionary of values, these include:

name,desc,size
Example in python 
```python
attributes = {'name': 'World1', 'desc': 'This is a world'}
```
