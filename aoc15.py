import re
f = open('aoc15.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
discs = []
digits = re.compile(r'(\d+)')

for line in raw_input:
    found_numbers = digits.findall(line)
    discs += [(int(found_numbers[1]), int(found_numbers[3]))]
print()
def check_disc(discs, time, index):
    if (discs[index][1] + time + (index +1)) % discs[index][0] == 0:
        if index < (len(discs) - 1):
            next_test = check_disc(discs, time, index + 1)
            if next_test == True:
                return True
            else:
                return False
        return True
    return False
time = 0
for t in range(10000000000):
    if check_disc(discs, t, 0) == True:
        time = t
        break
        
print('Part 1: target time is ' + str(time))

discs += [(11,0)]
time = 0
for t in range(10000000000):
    if check_disc(discs, t, 0) == True:
        time = t
        break
print('Part 2: target time is ' + str(time))