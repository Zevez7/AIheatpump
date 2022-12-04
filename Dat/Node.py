class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, data=None):
        self.id = ""
        self.successor = ""
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

    def setUpNode(self):
        self.id = self.data["PID"]
        self.successor = self.data["SUCCESSOR"]
