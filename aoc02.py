f = open('aoc02.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Positions:
# (-1 + 1j)   (0 + 1j)   (1 + 1j)
# (-1 + 0j)   (0 + 0j)   (1 + 0j)
# (-1 - 1j)   (0 - 1j)   (1 - 1j)
key_position = 0+0j
keycode = ''
number_positions = [999+999j, -1+1j, 0+1j, 1+1j, -1+0j, 0+0j, 1+0j, -1-1j, 0-1j, 1-1j]
for instruction in raw_input:
    for letter in instruction:
        if letter == 'U':
            
            imaginary = min(key_position.imag + 1,1)
            key_position = complex(key_position.real, imaginary)
        elif letter == 'R':
            real = min(key_position.real + 1, 1)
            key_position = complex(real, key_position.imag)
        elif letter == 'D':
            key_position = complex(key_position.real, max(key_position.imag - 1, -1))
        elif letter == 'L':
            key_position = complex(max(key_position.real - 1, -1), key_position.imag)
    keycode += str(number_positions.index(key_position))
print('Part 1: keycode is ' + keycode)
key_positions = {
    0+2j: '1',
    -1 + 1j: '2',
    0 + 1j: '3',
    1 + 1j: '4',
    -2 + 0j: '5',
    -1 + 0j: '6',
    0 + 0j: '7',
    1 + 0j: '8',
    2 + 0j: '9',
    -1 - 1j: 'A',
    0 - 1j: 'B',
    1 - 1j: 'C',
    0 - 2j: 'D'
}
keycode = ''
key_position = -2 + 0j
for instruction in raw_input:
    for letter in instruction:
        real = key_position.real
        imag = key_position.imag
        if letter == 'U':
            if abs(real) == 2:
                limit = 0
            elif abs(real) == 1:
                limit = 1
            else:
                limit = 2
            key_position = complex(real, min(imag + 1, limit))
        elif letter == 'D':
            if abs(real) == 2:
                limit = 0
            elif abs(real) == 1:
                limit = -1
            else:
                limit = -2
            key_position = complex(real, max(imag - 1, limit))
        elif letter == 'R':
            if abs(imag) == 2:
                limit = 0
            elif abs(imag) == 1:
                limit = 1
            else:
                limit = 2
            key_position = complex(min(real + 1, limit), imag)
        elif letter == 'L':
            if abs(imag) == 2:
                limit = 0
            elif abs(imag) == 1:
                limit = -1
            else:
                limit = -2
            key_position = complex(max(real - 1, limit), imag)
    keycode += key_positions[key_position]
print('Part 2: keycode is ' + keycode)

