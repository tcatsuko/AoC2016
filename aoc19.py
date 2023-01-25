from collections import deque

num_of_elves = 3014603
elf_list = []
presents = [1] * num_of_elves
elves = deque(list(range(num_of_elves)))

while len(elves) > 1:
    if presents[elves[0]] == 0:
        elves.popleft()
    else:
        presents[elves[0]] += presents[elves[1]]
        presents[elves[1]] = 0
        elves.rotate(-1)
print('Part 1: elf ' + str(elves[0] + 1) + ' has all the presents.')


num_of_elves = 3014603
left_elves = deque(list(range(num_of_elves // 2 + 1)))
right_elves = deque(list(range(num_of_elves // 2 + 1 , num_of_elves)))
test1 = right_elves[-1]
print()
while left_elves and right_elves:
    if len(left_elves) > len(right_elves):
        left_elves.pop()
    else:
        right_elves.pop()
    right_elves.appendleft(left_elves.popleft())
    left_elves.append(right_elves.pop())
print('Part 2: elf ' + str(left_elves[0] + 1) + ' has all the presents')
