from collections import defaultdict
import Queue
import json
from Node import NodeBFS
from calculatedLongDistance import maxDist

# Opening JSON file
# mockedData = open('./data/mockData.json')
# homeData = open('./data/homeData.json')
# data = open('./data/realData.json')
data = open('./data/realData100.json')

# returns JSON object as
DataLoad = json.load(data)

# print(realDataLoad)


def createNode(nodeStore, data):
    for item in data:
        createNode = NodeBFS(item, nodeStore)

        # store node inside nodeStorage
        nodeStore[createNode.getId()] = createNode


def isNotInFrontier(currentNode, frontier):

    for frontierItem in frontier.list:
        print("frontier Item ", frontierItem.getId())

        if frontierItem.getId() == currentNode.getId():
            print("current node is in frontier", currentNode.getId())
            return False
    return True


def printEndState(currentNode, nodeStorage):
    print("endstate reached terminated program")
    print("endNode Reached ID:", currentNode.getId())
    iterNode = currentNode

    nodePath = []

    while iterNode.getPreviousNode() != "":
        # print("previous node", iterNode.getData())
        nodePath.append(iterNode.getData())
        iterNode = nodeStorage[iterNode.getPreviousNode()]
    # print("previous node", iterNode.getData())
    nodePath.append(iterNode.getData())
    print(nodePath)


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


def breadthFirstSearch(data):

    nodeStorage = defaultdict(list)

    # loops through the data and generate a node and store the node inside nodeStorage
    createNode(nodeStorage, data)

    # generate successor for each node and save it in successor location

    # initialized the stack last in first out
    frontier = Queue.Queue()
    exploredSet = []
    previousNode = ""

    # loop through the data and find the farthest node in the data and return the location
    startAndEndId = startAndEndNodeId(nodeStorage)
    startState = startAndEndId[0]
    endState = startAndEndId[1]
    print("start", startState, "end", endState)

    initialNode = nodeStorage[startState]

    # add first node to frontier
    frontier.push(initialNode)
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
        print("exploredSet", exploredSet)

        # generate successor from current node
        currentNode.createSuccessor(exploredSet, frontier)

        # get the next successorState
        successorState = currentNode.getSuccessor()
        print("successorState", successorState)

        # save currentNodeID
        currentNodeID = currentNode.getId()
        print("Add current Node Id to previousNode", previousNode)

        for item in successorState:

            nodeId = item[0]

            # get the node from the nodeStorage
            nextNode = nodeStorage[nodeId]
            print("set the nextNode in successorState", nextNode.getId())

            # set currentNode to previousNode
            nextNode.setPreviousNode(currentNodeID)
            # print("previous", nextNode.getPreviousNode())

            # check to see if it's not in exploredSet or in the frontier
            if nextNode.getId() not in exploredSet and isNotInFrontier(nextNode, frontier):
                print("not in exploredSet adding to frontier", nextNode.getId())
                frontier.push(nextNode)
            else:
                print("nextNode is in not added to frontierlist", nextNode.getId())


def main():
    # breadthFirstSearch(homeDataLoad)
    breadthFirstSearch(DataLoad)


if __name__ == "__main__":
    main()
