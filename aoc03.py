f = open('aoc03.txt','rt')
raw_input = []
for line in f:
    raw_input += [[int(s) for s in line[:-1].split() if s.isdigit()]]
f.close()
valid_tri = 0
for triangle in raw_input:
    s1 = triangle[0]
    s2 = triangle[1]
    s3 = triangle[2]
    valid_triangle = True
    if ((s1 + s2) > s3) and ((s2 + s3) > s1) and ((s3 + s1) > s2):
        valid_tri += 1
print('Part 1: There are ' + str(valid_tri) + ' valid triangles.')
# 1052 too high
# Need to reorder the list
total_sides = 3 * len(raw_input)
new_layout = []
current_tri = []
for counter in range(total_sides):
    if len(current_tri) == 3:
        new_layout += [current_tri]
        current_tri = []
    row = counter % len(raw_input)
    column = counter // len(raw_input)
    current_tri += [raw_input[row][column]]
new_layout += [current_tri]
valid_tri = 0
for triangle in new_layout:
    s1 = triangle[0]
    s2 = triangle[1]
    s3 = triangle[2]
    valid_triangle = True
    if ((s1 + s2) > s3) and ((s2 + s3) > s1) and ((s3 + s1) > s2):
        valid_tri += 1
print('Part 2: There are ' + str(valid_tri) + ' valid triangles.')