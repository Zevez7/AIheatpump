
from math import sqrt

# Function calculates distance
# between two points


def dist(p1, p2):

    x0 = p1[0] - p2[0]
    y0 = p1[1] - p2[1]
    return x0 * x0 + y0 * y0

# Function to find the maximum
# distance between any two points


def maxDist(p):

    n = len(p)
    maxm = 0
    point1 = []
    point2 = []

    # Iterate over all possible pairs
    for i in range(n):
        for j in range(i + 1, n):

            # Update maxm
            calcMax = max(maxm, dist(p[i], p[j]))

            if calcMax > maxm:
                # print("found max value:", p[i], p[j], calcMax*1000000000)
                point1 = p[i]
                point2 = p[j]
                maxm = calcMax

    # Return actual distance
    return [point1, point2, sqrt(maxm)]
