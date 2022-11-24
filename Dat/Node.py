class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, name="", x=None, y=None):
        # self.parent = parent
        # self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
        self.successor = []
        self.x = x
        self.y = y
        self.name = name

    def __eq__(self, other):
        return self.position == other.position

    def getSuccessor(self):
        return self.successor

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getName(self):
        return self.name
