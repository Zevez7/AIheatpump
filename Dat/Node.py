class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, id="", successor=None, data=None):
        self.id = id
        self.successor = successor
        self.data = data
        self.previous = ""

    def getSuccessor(self):
        return self.successor

    def getId(self):
        return self.id

    def getData(self):
        return self.data

    def setPreviousNode(self, previous):
        self.previous = previous

    def getPreviousNode(self):
        return self.previous
