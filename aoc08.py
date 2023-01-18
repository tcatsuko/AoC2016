from collections import deque

f = open('aoc08.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
width = 50
height = 6
display = []
for y in range(height):
    current_row = deque()
    for x in range(width):
        current_row.append('.')
    display += [current_row]
for line in raw_input:
    split_line = line.split(' ')
    if split_line[0] == 'rect':
        # Draw a rectangle
        [rect_width, rect_height] = split_line[1].split('x')
        for y in range(int(rect_height)):
            for x in range(int(rect_width)):
                display[y][x] = '#'
    elif split_line[0] == 'rotate':
        if split_line[1] == 'column':
            col_to_rotate = int(split_line[2].split('=')[1])
            amount_to_rotate = int(split_line[4])
            temp_col = deque()
            for y in range(height):
                temp_col.append(display[y][col_to_rotate])
            temp_col.rotate(amount_to_rotate)
            for y in range(height):
                display[y][col_to_rotate] = temp_col[y]
        if split_line[1] == 'row':
            row_to_rotate = int(split_line[2].split('=')[1])
            amount_to_rotate = int(split_line[4])
            display[row_to_rotate].rotate(amount_to_rotate)
pixel_counter = 0
for row in display:
    pixel_counter += row.count('#')
print('Part 1: there are ' + str(pixel_counter) + ' pixels lit.')
for row in display:
    print(''.join(list(row)))