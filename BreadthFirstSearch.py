import Queue


dataStore = {"a": ["b"],
             "b": ["c"],
             "c": ["d"],
             "d": ["e"]
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
        print(currentNode)

        exploredSet.append(currentNode["state"])
        print("exploredSet", exploredSet)


def main():
    breadthFirstSearch(dataStore)


if __name__ == "__main__":
    main()
