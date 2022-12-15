import Stack
import json

f = open('mockData.json')

# the data turned into a dictionary

importData = json.load(f)


def depthFirstSearch(data):
    '''
        the function takes in the  data as a parameter
        imported data is a dictionary where the nodes are
        the keys and the children are the elements in the list
        that the keys are mapped to.
    '''

    # initializing a start node by usilizing getStartstate method
    start = "a"
    goal = "e"
    frontier = Stack.Stack()  # initializing a frontier which is a stack
    exploredSet = []  # initialize empty list which keeps track of explored nodes
    previousState = []
    initialNode = {"state": start, "prevNode": ""}
    frontier.push(initialNode)  # we are admitting tuple of first node and list of actions into the frontier


    # checing whethet the first node is the goal
    if initialNode["state"] == goal:
        return []


    # below loop will execute while we have nodes in the frontier
    while not frontier.isEmpty():
        # we are accessing the current node and actions  associated with it
        current = frontier.pop()
        # if current node is not yet in explored set we add it there
        if current not in exploredSet:
            exploredSet.append(current)
            # if current node is a goal state we return the actions
            if current["state"] == goal:
                # I neet to double check the below
                return current["state"]
            successor = data[current["state"]]
            previousState.append(
                current["state"])
            for succ in successor:
                nextNode = {"state": succ, "prevNode": previousState}
                frontier.push(nextNode)
                print(exploredSet)


    # while not frontier.isEmpty():
    #     #we are accessing the current node and actions  associated with it
    #     current = frontier.pop()
    #     if current not in exploredSet:
    #         exploredSet.append(current)
    #
    #         if current["state"] == endState:
    #             print("endstate reached terminated program")
    #             return exploredSet
    #         successor = data[current["state"]]
    #         for succ in successor:
    #             nextNode = {"state": succ, "prevNode": previousState}
    #
    #             frontier.push(nextNode)
    #
    #     print("exploredSet", exploredSet)





def main():

    print(depthFirstSearch(importData))

if __name__ == '__main__':
    main()

