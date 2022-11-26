import Queue


dataStore = {
    "a": ["b", "d"],
    "b": ["c"],
    "c": ["d"],
    "d": ["e"],
}


def breadthFirstSearch(data):
    # initialized the stack last in first out
    frontier = Queue.Queue()
    exploredSet = []
    previousState = []

    startState = "a"
    endState = "d"

    initialNode = {"state": startState, "prevNode": ""}

    # add initialNode to frontier
    frontier.push(initialNode)

    # print("successor", successor)
    def isNotInFrontier(checkItem):
        for frontierItem in frontier.list:
            print("frontier state ", frontier.list)

            # if frontierItem["state"] == checkItem:
            # print("current node state is in frontier", frontierItem["state"])
            return False
        return True

    while True:
        if frontier.isEmpty():
            print("empty frontier!")
            return

        # store current node and remove from frontier
        currentNode = frontier.pop()
        print("currentNode", currentNode)
        if endState == currentNode["state"]:
            print("endNode", currentNode)
            print("endstate reached terminated program")
            return

        # add the explored state
        exploredSet.append(currentNode["state"])
        print("exploredSet", exploredSet)

        # get the next state
        successorState = dataStore[currentNode["state"]]
        print("successorState", successorState)
        previousState.append(
            currentNode["state"])
        for item in successorState:

            nextNode = {"state": item, "prevNode": previousState}
            print("nextNode", nextNode)

            print("frontier list 1", frontier.list)

            # check to see if it's not already visited
            if nextNode["state"] not in exploredSet and isNotInFrontier(nextNode["state"]):
                print("not in exploredSet adding to frontier", nextNode)
                frontier.push(nextNode)
                print("frontier list 2", frontier.list)

        # print(frontier)
        # print(item)
        # print(state)
    # frontier.push()


def main():
    breadthFirstSearch(dataStore)


if __name__ == "__main__":
    main()
