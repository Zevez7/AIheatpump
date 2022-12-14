import json
from collections import defaultdict
from Queue import PriorityQueue

from calculatedLongDistance import maxDist
from Node import NodeAStar

# data = open('./data/realDataMod.json')
data100 = open('./data/realData100.json')

# returns JSON object as
# a dictionary
# importData = json.load(f)
# homeDataLoad = json.load(homeData)
DataLoad = json.load(data100)


def heuristic(node):
    data = node.getData()
    if "actype" in data.keys():
        if data["actype"] == "C - Central AC":
            return 100
        else:
            return 10


    if "heattype" in data.keys():
        if data["heattype"] == "F - Forced Hot Air":
            return 100
        else:
            return 10

    return 10




def createNode(nodeStore, data):
    for item in data:
        createNode = NodeAStar(item, nodeStore)

        # store node inside nodeStorage
        nodeStore[createNode.getId()] = createNode


def isNotInFrontier(currentNode, frontier):

    for frontierItem in frontier.heap:
        print("frontier Item ", frontierItem.getId())

        if frontierItem.getId() == currentNode.getId():
            print("current node is in frontier", currentNode.getId())
            return False
    return True


def printEndState(currentNode, nodeStorage):
    print("endstate reached terminated program")
    print("endNode Reached ID:", currentNode.getId())
    iterNode = currentNode

    while iterNode.getPreviousNode() != "":
        print("previous node", iterNode.getData())
        iterNode = nodeStorage[iterNode.getPreviousNode()]
    print("previous node", iterNode.getData())


def startAndEndNodeId(nodeStorage):
    dataArray = []
    # generate the start and end state nodes
    for x in nodeStorage:

        dataArray.append([nodeStorage[x].getLat(),
                          nodeStorage[x].getLng(), nodeStorage[x].getId()])
    startAndEndpoint = maxDist(dataArray)
    return (startAndEndpoint[0][2], startAndEndpoint[1][2])


def generateSuccessor(nodeStorage):
    for x in nodeStorage:
        nodeStorage[x].createSuccessor()

        value = nodeStorage[x].getSuccessor()
        print(x, "node", value)


def AStarSearch(data):

    nodeStorage = defaultdict(list)

    # loops through the data and generate a node and store the node inside nodeStorage
    createNode(nodeStorage, data)

    # testing that heuristic works
    for item in nodeStorage:

        print("heuristic", heuristic(nodeStorage[item]))

    # initialized the stack last in first out
    frontier = PriorityQueue()
    exploredSet = []
    previousNode = ""

    # loop through the data and find the farthest node in the data and return the location
    startAndEndId = startAndEndNodeId(nodeStorage)
    startState = startAndEndId[0]
    endState = startAndEndId[1]
    print("start", startState, "end", endState)

    initialNode = nodeStorage[startState]

    # add first node to frontier
    frontier.push(initialNode, heuristic(initialNode))

    frontier.heap

    # print(initialNode.getId())

    # initialNode.createSuccessor(exploredSet, frontier)

    # x = initialNode.getSuccessor()
    # print(x)

    # return

    while True:
        if frontier.isEmpty():
            print("empty frontier!")
            return

        # store current node and remove from frontier
        currentNode = frontier.pop()
        print("currentNode", currentNode.getId())

        if endState == currentNode.getId():
            printEndState(currentNode, nodeStorage)
            return

        # add currentNode Id to the exploredSet
        exploredSet.append(currentNode.getId())
        print("exploredSet:", exploredSet)

        # generate successor from current node
        currentNode.createSuccessor(exploredSet, frontier)

        # get the next successorState
        successorState = currentNode.getSuccessor()
        print("successorState:", successorState)

        # save currentNodeID
        currentNodeID = currentNode.getId()
        # print("Add current Node Id to previousNode", previousNode)

        for item in successorState:

            nodeId = item[0]

            # get the node from the nodeStorage
            nextNode = nodeStorage[nodeId]
            print("NextNode", nextNode.getId(), nextNode.getCost())

            # set currentNode to previousNode
            nextNode.setPreviousNode(currentNodeID)
            # print("previous", nextNode.getPreviousNode())

            nextNodeCost = nextNode.getCost()
            # update nextNode cost with its current cost and currentNode cost
            nextNode.setCost(currentNode.getCost()+nextNodeCost)

            print("nextNodeCost", nextNode.getCost())
            # add nextNode to frontier with priority from cost+ heuristic
            frontier.push(nextNode, nextNode.getCost() + heuristic(nextNode))

            # check to see if it's not in exploredSet or in the frontier
            # if nextNode.getId() not in exploredSet and isNotInFrontier(nextNode, frontier):
            #     print("Add to frontier", nextNode.getId())
            #     frontier.push(nextNode)
            # else:
            #     print("Not added to frontierlist", nextNode.getId())


def main():
    # breadthFirstSearch(homeDataLoad)

    AStarSearch(DataLoad)


if __name__ == "__main__":
    main()
