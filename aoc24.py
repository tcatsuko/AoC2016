from itertools import permutations
import networkx as nx

f = open('aoc24.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Scan input to see where nodes are
nodelist = {}
for y, row in enumerate(raw_input):
    for x, character in enumerate(row):
        if not (character == '#' or character == '.'):
            nodelist[character] = (x,y)

node_distances = {}
G = nx.Graph()
# generate a graph of the maze
for y in range(1, len(raw_input) - 1):
    for x in range(1, len(raw_input[0]) - 1):
        if raw_input[y][x] != '#':
            if raw_input[y-1][x] != '#':
                G.add_edge((x, y),(x,y-1))
            if raw_input[y+1][x] != '#':
                G.add_edge((x,y),(x,y+1))
            if raw_input[y][x-1] != '#':
                G.add_edge((x,y),(x-1,y))
            if raw_input[y][x+1] != '#':
                G.add_edge((x,y),(x+1,y))

for node in nodelist:
    if node not in node_distances:
        node_distances[node] = {}
        
    for nextnode in nodelist:
        if nextnode == node:
            continue
        if nextnode not in node_distances:
            node_distances[nextnode] = {}
        if nextnode not in node_distances[node]:
            #distance = bfs_length(raw_input, nodelist, node, nextnode)
            distance = nx.shortest_path_length(G, nodelist[node], nodelist[nextnode])
            node_distances[node][nextnode] = distance
            node_distances[nextnode][node] = distance

shortest_path = 9999999999999999999999999999999
node_names = list(nodelist.keys())
node_names.remove('0')
possible_paths = permutations(node_names)
for path in possible_paths:
    full_path = ['0'] + list(path)
    distance = 0
    for x in range(len(full_path) - 1):
        distance += node_distances[full_path[x]][full_path[x+1]]
    if distance < shortest_path:
        shortest_path = distance


print('Part 1: shortest path is ' + str(shortest_path))

shortest_path = 9999999999999999999999999999999


possible_paths = permutations(node_names)
for path in possible_paths:
    full_path = ['0'] + list(path) + ['0']
    distance = 0
    for x in range(len(full_path) - 1):
        distance += node_distances[full_path[x]][full_path[x+1]]
    if distance < shortest_path:
        shortest_path = distance
print('Part 2: shortest path is ' + str(shortest_path))


        
