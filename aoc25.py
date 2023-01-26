f = open('aoc25.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
keep_looping = True
a_counter = -1
while keep_looping == True:
    output = ''
    registers = {'a':0, 'b':0, 'c':0, 'd':0}
    a_counter += 1
    registers['a'] = a_counter
    pc = 0

    while pc < len(raw_input) and pc >= 0:
        
        current_instruction = raw_input[pc].split(' ')
        if current_instruction[0] == 'cpy':
            argument = current_instruction[2]
            if not (argument == 'a' or argument == 'b' or argument == 'c' or argument == 'd'):
                continue
            #
            #  if current_instruction[2].isdigit():
            #     continue
            argument = current_instruction[1]
            if argument == 'a' or argument == 'b' or argument == 'c' or argument == 'd':
                registers[current_instruction[2]] = registers[argument]
            else:
                registers[current_instruction[2]] = int(argument)
            # if current_instruction[1].isdigit():
            #     registers[current_instruction[2]] = int(current_instruction[1])
            # else:
            #     registers[current_instruction[2]] = registers[current_instruction[1]]
        elif current_instruction[0] == 'inc':
            registers[current_instruction[1]] += 1
        elif current_instruction[0] == 'dec':
            registers[current_instruction[1]] -= 1
        elif current_instruction[0] == 'out':
            argument = current_instruction[1]
            if argument == 'a' or argument == 'b' or argument == 'c' or argument == 'd':
                output += str(registers[argument])
            else:
                output += str(argument)
        elif current_instruction[0] == 'jnz':
            argument = current_instruction[1]
            if argument == 'a' or argument == 'b' or argument == 'c' or argument == 'd':
                test_eval = registers[argument]
            else:
                test_eval = int(argument)
            
            # if current_instruction[1].isdigit():
            #     test_eval = int(current_instruction[1])
            # else:
            #     test_eval = registers[current_instruction[1]]
            if test_eval != 0:
                argument = current_instruction[2]
                if argument == 'a' or argument == 'b' or argument == 'c' or argument == 'd':
                    pc += registers[argument] - 1
                else:
                    pc += int(argument) - 1

        elif current_instruction[0] == 'tgl':
            argument = current_instruction[1]
            if argument == 'a' or argument == 'b' or argument == 'c' or argument == 'd':
                offset = registers[argument]
            else:
                offset = int(argument)
            location = offset + pc
            if (location < 0) or (location >= len(raw_input)):
                pc += 1
                continue
            target_instruction = raw_input[location].split(' ')
            if target_instruction[0] == 'inc':
                raw_input[location] = 'dec ' + target_instruction[1]
            elif target_instruction[0] == 'dec':
                raw_input[location] = 'inc ' + target_instruction[1]
            elif target_instruction[0] == 'tgl':
                raw_input[location] = 'inc ' + target_instruction[1]
            elif target_instruction[0] == 'jnz':
                raw_input[location] = 'cpy ' + target_instruction[1] + ' ' + target_instruction[2]
            elif target_instruction[0] == 'cpy':
                raw_input[location] = 'jnz ' + target_instruction[1] + ' ' + target_instruction[2]
        if output == '010101010101' or output == '101010101010':
            keep_looping = False
        if len(output) > 12:
            break
        pc += 1
print('Part 1: set a to ' + str(a_counter))