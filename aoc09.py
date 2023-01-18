import re
f = open('aoc09.txt','rt')
encrypted_line = ''
pattern = re.compile(r'\s+')
for line in f:
    encrypted_line += re.sub(pattern, '', line)
f.close()
def decrypt(in_data):
    pos = 0
    new_data = ''
    while pos < len(in_data):
        current_char = in_data[pos]
        if current_char != '(':
            new_data += current_char
            pos += 1
            continue
        else:
            marker = ''
            pos += 1
            while in_data[pos] != ')':
                marker += in_data[pos]
                pos += 1
            data_to_copy = ''
            pos += 1
            chars_to_copy = int(marker.split('x')[0])
            times_to_copy = int(marker.split('x')[1])
            for x in range(chars_to_copy):
                data_to_copy += in_data[pos]
                pos += 1
            for x in range(times_to_copy):
                new_data += data_to_copy
    return new_data
def decrypt2(input_string, part2 = False):
    if '(' not in input_string:
        return len(input_string)
    length = 0
    while '(' in input_string:
        marker_left = input_string.find('(')
        length += marker_left
        input_string = input_string[marker_left + 1:]
        end_marker = input_string.find(')')
        marker = input_string[:end_marker].split('x')
        chars_to_copy = int(marker[0])
        times_to_copy = int(marker[1])
        input_string = input_string[end_marker + 1:]
        if part2 == False:
            length += chars_to_copy * times_to_copy
        else:
            length += decrypt2(input_string[:chars_to_copy], True) * times_to_copy
        input_string = input_string[chars_to_copy:]
    return length


decrypted_length = decrypt2(encrypted_line)
print('Part 1: length of intermediate decrypted data is ' + str(decrypted_length))

decrypted_length = decrypt2(encrypted_line, True)
print('Part 2: length of fully decrypted data is ' + str(decrypted_length))


