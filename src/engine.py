



def __init__(self):
    self.player = Player()


def step(self,commandstr):
    command = Command(commandstr)
    self.do(command)

def do(self,command):
    verb = command.verb
    object = command.object

    if verb == "go":
        self.player.move("north")



class Command(object):

        def __init__(self,commandstr):
            words = commandstr.split()
            self.verb = words[0]
            self.object = words[1]

class Player(object):
    hp = 100
    loc =[0,0]
    def move(self,direction):
        self.loc[0] += 1
        self.loc[1] += 1

