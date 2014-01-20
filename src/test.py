#BIG OLE TEST 
import curses 

class command(object):
	string = ""
	wArray = {}
	delim  = '>'
	verb   = ""
	obj    = ""

	def read(self):
		self.string = raw_input(self.delim) #Change to curses some how?
		self.wArray = self.string.split()
		
		if(len(self.wArray) < 2):
			return 
		else:
			self.verb   = self.wArray[0]
			self.obj    = self.wArray[1]


class Player(object):
	hp  = 100
	stm = 100

	posx = 0
	posy = 0

	def move(self):
		#direction.lower()
		self.posy += 1
		return "Moved!"
		'''
		if(direction == "north"):
			self.posy += 1
			return "wat"
		if(direction == "south"):
			self.posy += -1
		if(direction == "east"):
			self.posx += 1
		if(direction == "west"):
			self.posx += -1

		'''


player1 = Player()

print player1.hp
print player1.posy
print player1.move()
print player1.posy

'''

command = command()

command.read()

print "Verb: " + command.verb
print "Object: " + command.obj
'''