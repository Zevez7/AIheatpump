from collections import defaultdict
import Queue
import json
from NodeRealData import Node

# Opening JSON file
mockedData = open('./data/mockData.json')
homeData = open('./data/homeData.json')
realData = open('./data/realData.json')

# returns JSON object as
# a dictionary
# importData = json.load(f)
# homeDataLoad = json.load(homeData)
realDataLoad = json.load(realData)

# print(realDataLoad)


def createNode(nodeStore, data):
    for item in data:
        createNode = Node(item, nodeStore)

        # store node inside nodeStorage
        nodeStore[createNode.getId()] = createNode


def isNotInFrontier(currentNode, frontier):

    for frontierItem in frontier.list:
        print("frontier Item ", frontierItem.getId())

        if frontierItem.getId() == currentNode.getId():
            print("current node state is in frontier", currentNode.getId())
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


def breadthFirstSearch(data):

    nodeStorage = defaultdict(list)

    createNode(nodeStorage, data)

    # print(nodeStorage[2])
    # for x in nodeStorage:
    #     print(nodeStorage[x].getData())
    # y = x.getId()
    # print(y)

    nodeStorage[100010000].createSuccessor()

    x = nodeStorage[100010000].getSuccessor()
    print(x)
    return

    # initialized the stack last in first out
    frontier = Queue.Queue()
    exploredSet = []
    previousNode = ""

    startState = 1
    endState = 5

    initialNode = nodeStorage[startState]

    # add initialNode to frontier
    frontier.push(initialNode)

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

        # add the explored state
        exploredSet.append(currentNode.getId())
        print("exploredSet", exploredSet)

        # get the next state
        successorState = currentNode.getSuccessor()
        print("successorState", successorState)

        # add currentNodeId to previous State Array
        previousNode = currentNode.getId()
        print("Add current Node Id to previousNode", previousNode)

        for item in successorState:

            # get the node for the nodeStorage
            nextNode = nodeStorage[item["PID"]]
            print("set the nextNode in successorState", nextNode.getId())

            # set previousNode for all nextNode
            nextNode.setPreviousNode(previousNode)

            print("previous", nextNode.getPreviousNode())
            print("explored", exploredSet)

            # check to see if it's not in exploredSet or in the frontier
            if nextNode.getId() not in exploredSet and isNotInFrontier(nextNode, frontier):
                print("not in exploredSet adding to frontier", nextNode.getId())
                frontier.push(nextNode)
            else:
                print("nextNode is in not added to frontierlist", nextNode.getId())


def main():
    # breadthFirstSearch(homeDataLoad)
    breadthFirstSearch(realDataLoad)


if __name__ == "__main__":
    main()
