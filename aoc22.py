import re

f = open('aoc22.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
raw_input = raw_input[2:]
nodes = {}
for line in raw_input:
    nodeinfo = re.findall(r"\S+",line)
    nodenames = nodeinfo[0].split('node-')[1].split('-')
    x = int(nodenames[0][1:])
    y = int(nodenames[1][1:])
    capacity = int(nodeinfo[1][:-1])
    used = int(nodeinfo[2][:-1])
    remaining = int(nodeinfo[3][:-1])
    percent = int(nodeinfo[4][:-1])
    print()
    nodes[(x,y)] = {'capacity':capacity, 'used':used, 'remaining':remaining, 'percent':percent}

valid_pairs = 0
for node in nodes:
    current_node_info = nodes[node]
    for next_node in nodes:
        if next_node == node:
            continue
        next_node_info = nodes[next_node]
        if current_node_info['used'] > 0 and next_node_info['remaining'] >= current_node_info['used']:
            valid_pairs += 1
print('Part 1: there are ' + str(valid_pairs) + ' valid node pairs')
# Part 2 is going to be by hand
sector_map = []
for y in range(31):
    current_row = ''
    for x in range(31):
        if (x,y) == (0,0):
            current_row += 'G'
        elif(x,y) == (30,0):
            current_row += 'T'
        elif nodes[(x,y)]['capacity'] > 100:
            current_row += '#'
        elif nodes[(x,y)]['used'] == 0:
            current_row += '-'
        else:
            current_row += '.'
    sector_map += [current_row]
for line in sector_map:
    print(line)
# 207 by hand.  Move the empty node around the 'wall' of mostly full high capacity nodes
