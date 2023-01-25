from collections import deque

f = open('aoc21.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
password_string = 'abcdefgh'
password_list = []
for letter in password_string:
    password_list += [letter]
password = deque(password_list)
for line in raw_input:
    split_line = line.split(' ')
    if split_line[0] == 'swap':
        if split_line[1] == 'position':
            pos1 = int(split_line[2])
            pos2 = int(split_line[5])
            temp = password[pos1]
            password[pos1] = password[pos2]
            password[pos2] = temp
        else:
            pos1 = password.index(split_line[2])
            pos2 = password.index(split_line[5])
            temp = password[pos1]
            password[pos1] = password[pos2]
            password[pos2] = temp
    elif split_line[0] == 'reverse':
        pos1 = int(split_line[2])
        pos2 = int(split_line[4]) + 1
        orig = []
        for x in range(pos1, pos2):
            orig += [password[x]]
        orig.reverse()
        for x in range(pos1, pos2):
            password[x] = orig.pop(0)
    elif split_line[0] == 'rotate':
        if split_line[1] == 'left':
            steps = int(split_line[2])
            password.rotate(-1 * steps)
        elif split_line[1] == 'right':
            steps = int(split_line[2])
            password.rotate(steps)
        else:
            relevant_letter = split_line[6]
            position = password.index(relevant_letter)
            password.rotate()
            password.rotate(position)
            if position >= 4:
                password.rotate()

    elif split_line[0] == 'move':
        pos1 = int(split_line[2])
        pos2 = int(split_line[5])
        temp = password[pos1]
        del password[pos1]
        password.insert(pos2,temp)
print('Part 1: password is ' + ''.join(list(password)))

password_string = 'fbgdceah'
password_list = []
for letter in password_string:
    password_list += [letter]
password = deque(password_list)
raw_input.reverse()

for line in raw_input:
    split_line = line.split(' ')
    if split_line[0] == 'swap':
        if split_line[1] == 'position':
            pos1 = int(split_line[2])
            pos2 = int(split_line[5])
            temp = password[pos1]
            password[pos1] = password[pos2]
            password[pos2] = temp
        else:
            pos1 = password.index(split_line[2])
            pos2 = password.index(split_line[5])
            temp = password[pos1]
            password[pos1] = password[pos2]
            password[pos2] = temp
    elif split_line[0] == 'reverse':
        pos1 = int(split_line[2])
        pos2 = int(split_line[4]) + 1
        orig = []
        for x in range(pos1, pos2):
            orig += [password[x]]
        orig.reverse()
        for x in range(pos1, pos2):
            password[x] = orig.pop(0)
    elif split_line[0] == 'rotate':
        if split_line[1] == 'left':
            steps = int(split_line[2])
            password.rotate(steps)
        elif split_line[1] == 'right':
            steps = int(split_line[2])
            password.rotate(-1 * steps)
        else:
            relevant_letter = split_line[6]
            position = password.index(relevant_letter)
            # need to map out inverse of rotate by position
            if position == 1:
                password.rotate(-1)
            elif position == 3:
                password.rotate(-2)
            elif position == 5:
                password.rotate(-3)
            elif position == 7:
                password.rotate(-4)
            elif position == 2:
                password.rotate(2)
            elif position == 4:
                password.rotate(1)
            elif position == 0:
                password.rotate(-1)
            

    elif split_line[0] == 'move':
        pos2 = int(split_line[2])
        pos1 = int(split_line[5])
        temp = password[pos1]
        del password[pos1]
        password.insert(pos2,temp)
print('Part 2: password is ' + ''.join(list(password)))

