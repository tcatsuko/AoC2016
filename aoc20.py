import math
f = open('aoc20.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
blocklist = sorted([int(x), int(y)] for x, y in [line.split('-') for line in raw_input])
# assume candidates are one past the upper bound of each range
candidates = []
for item in blocklist:
    candidates += [item[1] + 1]
print()
def check_ip(blocklist, candidate):
    for item in blocklist:
        if item[0] <= candidate <= item[1]:
            break
    else:
        if candidate < 2**32:
            return True
    return False
for candidate in candidates:
    if check_ip(blocklist, candidate) == True:
        lowest_ip = candidate
        break
print('Part 1: lowest available IP is ' + str(lowest_ip))

total_allowed = 0
for candidate in candidates:
    test_ip = candidate
    while check_ip(blocklist, test_ip):
        total_allowed += 1
        test_ip += 1

print('Part 2: total IPs available is ' + str(total_allowed))
