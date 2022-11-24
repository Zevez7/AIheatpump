import Queue


dataStore = {"a": ["b", "d"],
             "b": ["c"],
             "c": ["d"],
             "d": ["e"],
             }


def breadthFirstSearch(data):
    # initialized the stack last in first out
    frontier = Queue.Queue()
    exploredSet = []

    startState = "a"
    endState = "d"

    initialNode = {"state": startState, "prevNode": ""}

    # add initialNode to frontier
    frontier.push(initialNode)

    while True:
        if frontier.isEmpty():
            print("empty frontier!")
            return

        # store current node and remove from frontier
        currentNode = frontier.pop()
        print("currentNode", currentNode)
        if endState == currentNode["state"]:
            print("endstate reached terminated program")
            return

        # add the explored state
        exploredSet.append(currentNode["state"])
        print("exploredSet", exploredSet)

        # get the next state
        state = dataStore[currentNode["state"]]
        print(state)
        for item in state:
            nextNode = {"state": item, "prevNode": currentNode["state"]}
            print(nextNode)
            # check to see if it's not already visited
            if nextNode["state"] not in exploredSet:
                print("not in state pushing", nextNode)
                frontier.push(nextNode)

        # print(frontier)
        # print(item)
        # print(state)
    # frontier.push()


def main():
    breadthFirstSearch(dataStore)


if __name__ == "__main__":
    main()
