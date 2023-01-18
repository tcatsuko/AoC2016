favorite_number = 1362
visited_places = set()
under_fifty = set()
nodes_to_visit = []
position = (1,1)
target_position = (31,39)
def is_open(coord):
    global favorite_number
    x = coord[0]
    y = coord[1]
    result = x * x + 3 * x + 2 * x * y + y + y * y + favorite_number
    binrep = str(bin(result))[2:]
    ones = binrep.count('1')
    if ones % 2 == 0:
        return True
    else:
        return False
steps = 0
nodes_to_visit += [(position, steps)]
while len(nodes_to_visit) > 0:
    current_node = nodes_to_visit.pop(0)
    current_steps = current_node[1]
    current_position = current_node[0]
    if current_position == target_position:
        break
    visited_places.add(current_position)
    x = current_position[0]
    y = current_position[1]
    # check up
    if y > 0:
        if is_open((x,y-1)):
            if (x,y-1) not in visited_places:
                nodes_to_visit += [((x,y-1),current_steps + 1)]
    # check down
    if is_open((x, y+1)):
        if (x,y+1) not in visited_places:
            nodes_to_visit += [((x,y+1),current_steps + 1)]
    # check left
    if x > 0:
        if is_open((x-1,y)):
            if (x-1,y) not in visited_places:
                nodes_to_visit += [((x-1, y), current_steps + 1)]
    # check right
    if is_open((x+1, y)):
        if (x+1, y) not in visited_places:
            nodes_to_visit += [((x+1,y), current_steps + 1)]
print('Part 1: it took ' + str(current_steps) + ' steps to get to the target position')
visited_places = set()
nodes_to_visit = []
position = (1,1)
steps = 0
nodes_to_visit += [(position, steps)]
while len(nodes_to_visit) > 0:
    current_node = nodes_to_visit.pop(0)
    current_steps = current_node[1]
    current_position = current_node[0]
    if current_steps <= 50:
        under_fifty.add(current_position)
    if current_steps > 100:
        break
    visited_places.add(current_position)
    x = current_position[0]
    y = current_position[1]
    # check up
    if y > 0:
        if is_open((x,y-1)):
            if (x,y-1) not in visited_places:
                nodes_to_visit += [((x,y-1),current_steps + 1)]
    # check down
    if is_open((x, y+1)):
        if (x,y+1) not in visited_places:
            nodes_to_visit += [((x,y+1),current_steps + 1)]
    # check left
    if x > 0:
        if is_open((x-1,y)):
            if (x-1,y) not in visited_places:
                nodes_to_visit += [((x-1, y), current_steps + 1)]
    # check right
    if is_open((x+1, y)):
        if (x+1, y) not in visited_places:
            nodes_to_visit += [((x+1,y), current_steps + 1)]
print('Part 2: you can reach ' + str(len(under_fifty)) + ' locations in at most 50 steps.')
