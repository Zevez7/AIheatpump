from manhattanDistance import get_manhattan_distance


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, data=None, nodeStore=None):
        self.id = ""
        self.successor = []
        self.data = data
        self.previous = ""
        self.setUpNode()
        self.nodeStore = nodeStore
        self.lat
        self.lng

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
        self.id = self.data["pid"]
        self.lat = self.data["latitude"]
        self.lng = self.data["longitude"]
        # self.successor = self.data["SUCCESSOR"]

    def getLat(self):
        return self.lat

    def getLng(self):
        return self.lng

    # generate successor for the node
    def createSuccessor(self):

        distMH = {}

        for x in self.nodeStore:
            lat2 = self.nodeStore[x].getLat()
            lng2 = self.nodeStore[x].getLng()
            coordId = x
            print(coordId)

            geoCoord1 = (self.lat, self.lng)
            geoCoord2 = (lat2, lng2)
            # print(geoCoord2)
            weightedValue = 10000000
            dist = get_manhattan_distance(geoCoord1, geoCoord2)*weightedValue
            distMH[coordId] = int(dist)

        sortedDistMH = (sorted(distMH.items(), key=lambda kv:
                               (kv[1], kv[0])))
        print(sortedDistMH)

        # adding 4 successor to the list
        for x in range(1, 5):
            self.successor.append(sortedDistMH[x])
            print(sortedDistMH[x])
