# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).


NOTE:conda activate AIPA
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))

    # initialized the stack last in first out
    frontier = util.Stack()
    exploredSet = []

    # get start state returns tuple (5,5)
    startState = problem.getStartState()
    intialStateNode = {"state": startState, "action": "", "prevNode": ""}

    # add initialStateNode to frontier
    frontier.push(intialStateNode)

    # loop
    while True:

        # exit loop when frontier is empty
        if frontier.isEmpty():
            print(">>>Empty frontier")
            return

        # store current node and remove from frontier
        currentNode = frontier.pop()
        # print("currentNode", currentNode["action"])

        exploredSet.append(currentNode["state"])

        # exit loop if goal state is found
        if problem.isGoalState(currentNode["state"]):
            actionSet = []
            GoalNode = currentNode
            # loop through goal node
            while "prevNode" in GoalNode:
                actionSet.append(GoalNode["action"])
                GoalNode = GoalNode["prevNode"]

            # remove the empty string in array
            actionSet.pop()

            # reverse the array
            actionSet.reverse()
            print("action", actionSet)

            return actionSet
        # loop through the successors
        successor = problem.getSuccessors(currentNode["state"])

        def frontierCheck(checkItem):
            for frontierItem in frontier.list:
                # print("frontier state ", frontierItem["state"])

                if frontierItem["state"] == checkItem:
                    print("current node state is in frontier",
                          frontierItem["state"])
                    return False
            return True
            # print("frontier list",frontier.list)

        # frontierCheck();

        for item in successor:
            print(item)
            # frontier check
            # def frontierCheck ():
            #     for frontierItem in frontier.list:
            #         if frontierItem["state"] == item[0]:
            #             print("frontier state ", frontierItem["state"])
            #     # return False
            # print("frontier list",frontier.list)

            # frontierCheck (item[0])
            # if state is not in exploredSet and not in frontier
            if item[0] not in exploredSet:
                print("state not in explored set", item[0])
                node = {"state": item[0], "action": item[1],
                        "prevNode": currentNode}

                # add node to the end of frontier
                frontier.push(node)

    util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))

    # initialized the Queue First in first out
    frontier = util.Queue()
    exploredSet = []

    # get start state returns tuple (5,5)
    startState = problem.getStartState()
    intialStateNode = {"state": startState, "action": "", "prevNode": ""}

    # add initialStateNode to frontier
    frontier.push(intialStateNode)

    # loop
    while True:

        # exit loop when frontier is empty
        if frontier.isEmpty():
            print(">>>Empty frontier")
            return

        # store current node and remove from frontier
        currentNode = frontier.pop()
        # print("currentNode", currentNode["state"])

        exploredSet.append(currentNode["state"])
        # print("exploredSet", exploredSet)

        # exit loop if goal state is found
        if problem.isGoalState(currentNode["state"]):
            actionSet = []
            GoalNode = currentNode
            # print("goal found", problem.isGoalState(
            #     currentNode["state"]), currentNode["state"])
            # loop through goal node
            while "prevNode" in GoalNode:
                actionSet.append(GoalNode["action"])
                GoalNode = GoalNode["prevNode"]

            # remove the empty string in array
            actionSet.pop()

            # reverse the array
            actionSet.reverse()
            # print("action", actionSet)

            return actionSet

        # loop through the successors
        successor = problem.getSuccessors(currentNode["state"])

        # print("successor", successor)
        def frontierCheck(checkItem):
            for frontierItem in frontier.list:
                # print("frontier state ", frontierItem["state"])

                if frontierItem["state"] == checkItem:
                    # print("current node state is in frontier", frontierItem["state"])
                    return False
            return True

        for item in successor:
            # print("successor",item)

            # if state is not in exploredSet and not in frontier
            if item[0] not in exploredSet and frontierCheck(item[0]):
                # print("state not in explored set, add to queue", item[0])
                node = {"state": item[0], "action": item[1],
                        "prevNode": currentNode}

                # add node to the front of frontier
                frontier.push(node)
    # count += 1
    # return ["West", "West"]
    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Is the start a goal?", problem.getSuccessors(problem.getStartState()))

    # initialized the Queue First in first out
    frontier = util.PriorityQueue()
    exploredSet = []

    # get start state returns tuple (5,5)
    startState = problem.getStartState()
    intialStateNode = {"state": startState,
                       "action": "", "cost": 0, "prevNode": ""}

    # add initialStateNode to frontier
    frontier.push(intialStateNode, 0)

    while True:

        # exit loop when frontier is empty
        if frontier.isEmpty():
            # print(">>>Empty frontier")
            return
        # store current node and remove from frontier
        currentNode = frontier.pop()
        # print("currentNode", currentNode["state"])
        # print("currentNode", currentNode)

        exploredSet.append(currentNode["state"])

        # exit loop if goal state is found
        if problem.isGoalState(currentNode["state"]):
            actionSet = []
            GoalNode = currentNode
            # print("goal found", problem.isGoalState(
            #     currentNode["state"]), currentNode["state"])
            # loop through goal node
            while "prevNode" in GoalNode:
                actionSet.append(GoalNode["action"])
                GoalNode = GoalNode["prevNode"]

            # remove the empty string in array
            actionSet.pop()

            # reverse the array
            actionSet.reverse()
            # print("action", actionSet)

            return actionSet

        # loop through the successors
        successor = problem.getSuccessors(currentNode["state"])
        # print("successor", successor)
        # create a frontier list from the priorityHeap

        def frontierCheck(checkItem):

            for front in frontier.heap:
                # print("front", front)

                if front[2]["state"] == checkItem:
                    # print("current node state is in frontier")
                    return True
            return False
        # print("exploredSet,",exploredSet)

        for item in successor:
            # print(item)
            # print(item)
            next_cost = currentNode["cost"] + item[2]
            next_node = {"state": item[0], "action": item[1], "cost": next_cost,
                         "prevNode": currentNode}
            # if state is not in exploredSet
            if item[0] not in exploredSet:

                # if state is not in frontier
                if not frontierCheck(item[0]):
                    print("state not in explored set and not in frontier", item)
                    # add next cost with heuristic to priority
                    frontier.push(next_node, next_cost)

                elif frontierCheck(item[0]):
                    # for front in frontier.heap:
                    # loop through the frontier
                    for front in frontier.heap:
                        # match the succesor state with the one in frontier
                        if front[2]["state"] == item[0]:
                            # found same state, if next_cost is less than frontier cost
                            if next_cost <= front[2]["cost"]:
                                # update frontier
                                frontier.update(next_node, next_cost)

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    
    
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Is the start a goal?", problem.getSuccessors(problem.getStartState()))

    # initialized the Queue First in first out
    frontier = util.PriorityQueue()
    exploredSet = []
    heuristic = heuristic

    # get start state returns tuple (5,5)
    startState = problem.getStartState()
    intialStateNode = {"state": startState,
                       "action": "", "cost": 0, "prevNode": ""}

    # add initialStateNode to frontier
    frontier.push(intialStateNode, heuristic(intialStateNode["state"], problem))

    while True:

        # exit loop when frontier is empty
        if frontier.isEmpty():
            # print(">>>Empty frontier")
            return
        # store current node and remove from frontier
        currentNode = frontier.pop()
        # print("currentNode", currentNode["state"])
        # print("currentNode", currentNode)

        # {'state': (27, 8), 'action': 'South', 'cost':1}
        exploredSet.append(currentNode["state"])

        # exit loop if goal state is found
        if problem.isGoalState(currentNode["state"]):
            actionSet = []
            GoalNode = currentNode
            # print("goal found", problem.isGoalState(
            #     currentNode["state"]), currentNode["state"])
            # loop through goal node
            while "prevNode" in GoalNode:
                actionSet.append(GoalNode["action"])
                GoalNode = GoalNode["prevNode"]

            # remove the empty string in array
            actionSet.pop()

            # reverse the array
            actionSet.reverse()
            # print("action", actionSet)

            return actionSet

        # loop through the successors
        successor = problem.getSuccessors(currentNode["state"])
        # print("successor", successor)
        # create a frontier list from the priorityHeap

        def frontierCheck(checkItem):

            for front in frontier.heap:
                # print("front", front)

                if front[2]["state"] == checkItem:
                    # print("current node state is in frontier")
                    return True
            return False
        # print("exploredSet,",exploredSet)

        for item in successor:
            # print(item)
            next_cost = currentNode["cost"] + item[2]
            next_node = {"state": item[0], "action": item[1], "cost": next_cost,
                         "prevNode": currentNode}
            # if state is not in exploredSet
            if item[0] not in exploredSet:

                # if state is not in frontier
                if not frontierCheck(item[0]):
                    # print("state not in explored set and not in frontier", item)
                    # add next cost with heuristic to priority
                    frontier.push(next_node, next_cost +
                                  heuristic(item[0], problem))

                elif frontierCheck(item[0]):
                    # for front in frontier.heap:
                    # loop through the frontier
                    for front in frontier.heap:
                        # match the succesor state with the one in frontier
                        if front[2]["state"] == item[0]:
                            # found same state, if next_cost is less than frontier cost
                            if next_cost <= front[2]["cost"]:
                                # update frontier
                                frontier.update(
                                    next_node, next_cost+heuristic(item[0], problem))

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
