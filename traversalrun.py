# Shortest Path Using Breadth-First Traversal.


print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

import networkx as nx
from graphmain3 import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))
