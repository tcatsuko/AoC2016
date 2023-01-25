f = open('aoc18.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
current_row = raw_input[0]
empty_tiles = 0

rows_to_determine = 40
for x in range(rows_to_determine-1):
    empty_tiles += current_row.count('.')
    previous_row = current_row[:]
    current_row = ''
    for character in range(len(previous_row)):
        if character == 0:
            test_area = '.' + previous_row[0:2]
        elif character == len(previous_row) - 1:
            test_area = previous_row[-2] + previous_row[-1] + '.'
        else:
            test_area = previous_row[character - 1:character + 2]
        if (test_area == '^^.') or (test_area == '.^^') or (test_area == '^..') or (test_area == '..^'):
            current_row += '^'
        else:
            current_row += '.'
empty_tiles += current_row.count('.')

print('Part 1: there are ' + str(empty_tiles) + ' safe tiles in ' + str(rows_to_determine) + ' rows')
current_row = raw_input[0]
empty_tiles = 0

rows_to_determine = 400000
for x in range(rows_to_determine-1):
    empty_tiles += current_row.count('.')
    previous_row = current_row[:]
    current_row = ''
    for character in range(len(previous_row)):
        if character == 0:
            test_area = '.' + previous_row[0:2]
        elif character == len(previous_row) - 1:
            test_area = previous_row[-2] + previous_row[-1] + '.'
        else:
            test_area = previous_row[character - 1:character + 2]
        if (test_area == '^^.') or (test_area == '.^^') or (test_area == '^..') or (test_area == '..^'):
            current_row += '^'
        else:
            current_row += '.'
empty_tiles += current_row.count('.')
print('Part 2: there are ' + str(empty_tiles) + ' safe tiles in ' + str(rows_to_determine) + 'rows')
