from collections import defaultdict

import Stack
import json
import Node

homeData = open("./homeData.json")
homeDataDict = json.load(homeData)

def createNode(nodeStore, data):
    for item in data:
        createNode = Node.Node(item)

        # store node inside nodeStroage
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


def depthFirstSearch(data):
    nodeStorage = defaultdict(list)

    print("node storage", nodeStorage)

    createNode(nodeStorage, data)

    # initialized the stack last in first out
    frontier = Stack.Stack()
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
    depthFirstSearch(homeDataDict)


if __name__ == "__main__":
    main()
