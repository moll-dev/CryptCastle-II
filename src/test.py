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


command = command()

command.read()

print "Verb: " + command.verb
print "Object: " + command.obj