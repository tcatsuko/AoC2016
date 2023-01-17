
f = open('aoc01.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close
instructions = raw_input[0].split(', ')
coordinate = (0 + 0j)
direction = (0 + 1j)
visited_points = set()
visited_points.add(coordinate)
hq_found = False
for instruction in instructions:
    turn = instruction[0]
    if turn == 'R':
        # North: (0 + 1j)
        # East: (1 + 0j)
        # South: (0 - 1j)
        # West: (-1 + 0j)
        direction = complex(direction.imag, -1 * direction.real)
        

    elif turn == 'L':
        # North: (0 + 1j)
        # West: (-1 + 0j)
        # South: (0 - 1j)
        # East: (1 + 0j)
        direction = complex(-1 * direction.imag, direction.real)
    magnitude = int(instruction[1:])
    for x in range(magnitude):
        coordinate += direction
        if (coordinate in visited_points) and (hq_found == False):
            hq = coordinate
            hq_found = True
        visited_points.add(coordinate)

x_distance = coordinate.real
y_distance = coordinate.imag
distance = abs(x_distance) + abs(y_distance)
print('Part 1: distance is ' + str(distance))
print('Part 2: HQ is ' + str(abs(hq.real) + abs(hq.imag)))
# 250 too high
