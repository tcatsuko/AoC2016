f = open('aoc04.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
valid_rooms = []
valid_sectors = []
for line in raw_input:
    # get the sector ID
    sector_id = ''.join(x for x in line if x.isdigit())
    enc_name = line[:line.index(sector_id)][:-1]
    checksum = line.split('[')[1].split(']')[0]
    letter_dict = {}
    for letter in enc_name:
        if letter == '-':
            continue
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    sorted_list = sorted(letter_dict.items(), key=lambda x: (-x[1], x[0]))     
    letter_freq = ''
    for x in range(5):
        letter_freq += sorted_list[x][0]
    if letter_freq == checksum:
        valid_rooms += [line]
        valid_sectors += [int(sector_id)]
print('Part 1: sum of sector IDs is ' + str(sum(valid_sectors)))
decrypted_rooms = []
for (idx, string) in enumerate(valid_rooms):
    decrypted_room = ''
    for letter in string:
        if letter == '-':
            decrypted_room += ' '
        else:
            sector_id = valid_sectors[idx]
            dec_letter = chr(((ord(letter) - ord('a') + sector_id) % 26) + ord('a'))
            decrypted_room += dec_letter
    decrypted_rooms += [decrypted_room]
    if 'northpole' in decrypted_room:
        winning_sector = sector_id
print('Part 2: north pole objects stored at ' + str(winning_sector))
