f = open('aoc06.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
letter_counter = []
for x in range(len(raw_input[0])):
    letter_counter += [{}]
for line in raw_input:
    for idx, letter in enumerate(line):
        if letter not in letter_counter[idx]:
            letter_counter[idx][letter] = 1
        else:
            letter_counter[idx][letter] += 1
message = ''
for item in letter_counter:
    sorted_list = sorted(item.items(), key=lambda x: (-x[1], x[0]))
    message += sorted_list[0][0]
print('Part 1: message is ' + message)
message = ''
for item in letter_counter:
    sorted_list = sorted(item.items(), key=lambda x: (x[1], x[0]))
    message += sorted_list[0][0]
print('Part 2: message is ' + message)