
import json
from collections import defaultdict

graph = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"],
         "f": []
         }

graph2 = defaultdict(list)

# add edges to a graph


def addEdge(graph2, node, linking_node):
    graph2[node].append(linking_node)


# Print outs the edges of a graph
def generate_edge(graph):
    edges = []

    for node in graph:
        print("node", node)
        for neighbor in graph[node]:
            print("neighbor", neighbor)
            edges.append((node, neighbor))

    return edges


# addEdge(graph2, "a", "c")
# addEdge(graph2, "a", "b")
# addEdge(graph2, "b", "d")

# print(generate_edge(graph2))
# print(graph2)


# Opening JSON file
f = open('jsonData.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['data']:
    if (i["id"] == "a"):
        print(i)

# Closing file
f.close()
