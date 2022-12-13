from manhattanDistance import get_manhattan_distance


class Node():
    def __init__(self, data=None):
        self.id = ""
        self.successor = ""
        self.data = data
        self.previous = ""
        self.setUpNode()

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


class NodeUniformCost():
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
        self.cost = 0

    def getCost(self):
        return self.cost

    def setCost(self, cost):
        self.cost = cost

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
    def createSuccessor(self, exploredSet, frontier):

        distMH = {}

        for x in self.nodeStore:
            lat2 = self.nodeStore[x].getLat()
            lng2 = self.nodeStore[x].getLng()
            coordId = x
            # print(coordId)

            geoCoord1 = (self.lat, self.lng)
            geoCoord2 = (lat2, lng2)
            # print(geoCoord2)
            weightedValue = 10000000
            dist = get_manhattan_distance(geoCoord1, geoCoord2)*weightedValue
            distMH[coordId] = int(dist)

        sortedDistMH = (sorted(distMH.items(), key=lambda kv:
                               (kv[1], kv[0])))
        # print("sorted MH", sortedDistMH)

        # filtered out node already explored
        filteredExploredList = []
        for x in sortedDistMH:
            if x[0] not in exploredSet:
                filteredExploredList.append(x)

        # filtered out node in the frontier
        frontierArray = []
        for frontierItem in frontier.list:
            # print("frontier Item ", frontierItem.getId())
            frontierArray.append(frontierItem.getId())

        filteredFrontierList = []
        for x in filteredExploredList:
            if x[0] not in frontierArray:
                filteredFrontierList.append(x)

        # print("exploredSet", exploredSet)
        # print("filteredExploredList", filteredExploredList)
        # print("frontierArray", frontierArray)
        # print("filteredFrontierList", filteredFrontierList)
        # remove successor
        # adding 4 successor to the list

        for x in range(2):
            if filteredFrontierList:  # if empty_list will evaluate as false.
                successor = filteredFrontierList.pop(0)
                self.successor.append(successor)


class NodeUniformCost():

    def __init__(self, data=None, nodeStore=None):
        self.id = ""
        self.successor = []
        self.data = data
        self.previous = ""
        self.setUpNode()
        self.nodeStore = nodeStore
        self.lat
        self.lng
        self.cost = 1

    def getCost(self):
        return self.cost

    def setCost(self, cost):
        self.cost = cost

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
    def createSuccessor(self, exploredSet, frontier):

        distMH = {}

        for x in self.nodeStore:
            lat2 = self.nodeStore[x].getLat()
            lng2 = self.nodeStore[x].getLng()
            coordId = x
            # print(coordId)

            geoCoord1 = (self.lat, self.lng)
            geoCoord2 = (lat2, lng2)
            # print(geoCoord2)
            weightedValue = 10000000
            dist = get_manhattan_distance(geoCoord1, geoCoord2)*weightedValue
            distMH[coordId] = int(dist)

        sortedDistMH = (sorted(distMH.items(), key=lambda kv:
                               (kv[1], kv[0])))
        # print("sorted MH", sortedDistMH)

        # filtered out node already explored
        filteredExploredList = []
        for x in sortedDistMH:
            if x[0] not in exploredSet:
                filteredExploredList.append(x)

        # filtered out node in the frontier
        frontierArray = []
        for frontierItem in frontier.heap:
            # print(frontierItem[2].getId())
            # print("frontier Item ", frontierItem.getId())
            frontierArray.append(frontierItem[2].getId())

        filteredFrontierList = []
        for x in filteredExploredList:
            if x[0] not in frontierArray:
                filteredFrontierList.append(x)

        # print("exploredSet", exploredSet)
        # print("filteredExploredList", filteredExploredList)
        # print("frontierArray", frontierArray)
        # print("filteredFrontierList", filteredFrontierList)
        # remove successor
        # adding 4 successor to the list

        for x in range(2):
            if filteredFrontierList:  # if empty_list will evaluate as false.
                successor = filteredFrontierList.pop(0)
                self.successor.append(successor)
