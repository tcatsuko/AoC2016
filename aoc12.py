f = open('aoc12.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
registers = {'a':0, 'b': 0, 'c': 0, 'd': 0}
pc = 0
while pc < len(raw_input):
    
    current_instruction = raw_input[pc].split(' ')
    if current_instruction[0] == 'cpy':
        if current_instruction[1].isdigit():
            registers[current_instruction[2]] = int(current_instruction[1])
        else:
            registers[current_instruction[2]] = registers[current_instruction[1]]
    elif current_instruction[0] == 'inc':
        registers[current_instruction[1]] += 1
    elif current_instruction[0] == 'dec':
        registers[current_instruction[1]] -= 1
    elif current_instruction[0] == 'jnz':
        if current_instruction[1].isdigit():
            test_eval = int(current_instruction[1])
        else:
            test_eval = registers[current_instruction[1]]
        if test_eval != 0:
            pc += int(current_instruction[2]) - 1
    pc += 1
print('Part 1: The value remaining in register a is ' + str(registers['a']))


registers = {'a':0, 'b': 0, 'c': 1, 'd': 0}
pc = 0
while pc < len(raw_input):
    
    current_instruction = raw_input[pc].split(' ')
    if current_instruction[0] == 'cpy':
        if current_instruction[1].isdigit():
            registers[current_instruction[2]] = int(current_instruction[1])
        else:
            registers[current_instruction[2]] = registers[current_instruction[1]]
    elif current_instruction[0] == 'inc':
        registers[current_instruction[1]] += 1
    elif current_instruction[0] == 'dec':
        registers[current_instruction[1]] -= 1
    elif current_instruction[0] == 'jnz':
        if current_instruction[1].isdigit():
            test_eval = int(current_instruction[1])
        else:
            test_eval = registers[current_instruction[1]]
        if test_eval != 0:
            pc += int(current_instruction[2]) - 1
    pc += 1
print('Part 2: The value remaining in register a is ' + str(registers['a']))