
import json
from collections import defaultdict
import Node
import Queue

graph = defaultdict(list)

file = open('jsonData.json')
data = json.load(file)

# Iterating through the json
# list
# for i in data['data']:
#     if (i["id"] == "a"):
#         print(i)


# convert data to node and store node into graph


for i in data['data']:

    newNode = Node(i["id"], i["x"], i["y"])
    graph[i["id"]] = newNode


for i in graph:
    node = graph[i]
    print(node.getName(), node.getX(), node.getY())
# Closing file
file.close()
