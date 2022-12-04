from collections import defaultdict
import Queue
import json
import Node

# Opening JSON file
f = open('./data/mockData.json')
mockedData = open('./data/homeData.json')

# returns JSON object as
# a dictionary
importData = json.load(f)
mockedDataLoad = json.load(mockedData)


def breadthFirstSearch(data):

    nodeStorage = defaultdict(list)

    # loop through the mockedDataLoad and add the node to storage
    for item in mockedDataLoad:
        createNode = Node.Node(item["PID"], item["SUCCESSOR"], item)
        nodeStorage[item["PID"]] = createNode

    # initialized the stack last in first out
    frontier = Queue.Queue()
    exploredSet = []
    previousNode = ""

    startState = 1
    endState = 6

    initialNode = nodeStorage[startState]

    # add initialNode to frontier
    frontier.push(initialNode)

    def isNotInFrontier(currentNode):

        for frontierItem in frontier.list:
            print("frontier Item ", frontierItem.getId())

            if frontierItem.getId() == currentNode.getId():
                print("current node state is in frontier", currentNode.getId())
                return False
        return True

    while True:
        if frontier.isEmpty():
            print("empty frontier!")
            return

        # store current node and remove from frontier
        currentNode = frontier.pop()
        print("currentNode", currentNode.getId())
        if endState == currentNode.getId():
            print("endNode", currentNode.getData())
            iterNode = currentNode
            print("endstate reached terminated program")

            while iterNode.getPreviousNode() != "":
                print("previous node", iterNode.getId())
                iterNode = nodeStorage[iterNode.getPreviousNode()]
            print("previous node", iterNode.getId())
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
            if nextNode.getId() not in exploredSet and isNotInFrontier(nextNode):
                print("not in exploredSet adding to frontier", nextNode.getId())
                frontier.push(nextNode)
            else:
                print("nextNode is in not added to frontierlist", nextNode.getId())


def main():
    breadthFirstSearch(importData)


if __name__ == "__main__":
    main()
