class StatBar:
    def __init__(self,engine,gui):
        self.engine = engine
        self.gui = gui
        self.user = engine.user
        self.turns = engine.turncount

    def update(self):
        self.turns = self.engine.turncount

    def construct(self):
        pass
class ObjBox:

    def __init__(self,engine,gui):
        self.engine = engine
        self.gui = gui

    def update(self):
        pass

class InvBox:

    def __init__(self,engine,gui):
        self.engine = engine
        self.gui = gui

    def update(self):
        pass

