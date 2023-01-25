import hashlib

passcode = 'pvhmgsws'

move_queue = []
moveset = ''
final_moveset = ''
position = 0+0j
door_open = ['b','c','d','e','f']
move_queue += [(position, moveset)]
while len(move_queue) > 0:
    position, moveset = move_queue.pop(0)
    if position == 3 + 3j:
        final_moveset = moveset
        break
    # Get hash
    current_hash = hashlib.md5((passcode + str(moveset)).encode())
    digest = str(current_hash.hexdigest())
    # check up
    if (digest[0] in door_open) and (position.imag  > 0):
        move_queue += [(position-1j, moveset + 'U')]
    # check down
    if (digest[1] in door_open) and (position.imag < 3):
        move_queue += [(position + 1j, moveset + 'D')]
    # check left
    if (digest[2] in door_open) and (position.real > 0):
        move_queue += [(position - 1, moveset + 'L')]
    # check right
    if (digest[3] in door_open) and (position.real < 3):
        move_queue += [(position + 1, moveset + 'R')]

print('Part 1: path is ' + final_moveset)
move_queue = []
moveset = ''
final_movesets = []
position = 0+0j
door_open = ['b','c','d','e','f']
move_queue += [(position, moveset)]
while len(move_queue) > 0:
    position, moveset = move_queue.pop(0)
    if position == 3 + 3j:
        final_movesets += [moveset]
        continue
    # Get hash
    current_hash = hashlib.md5((passcode + str(moveset)).encode())
    digest = str(current_hash.hexdigest())
    # check up
    if (digest[0] in door_open) and (position.imag  > 0):
        move_queue += [(position-1j, moveset + 'U')]
    # check down
    if (digest[1] in door_open) and (position.imag < 3):
        move_queue += [(position + 1j, moveset + 'D')]
    # check left
    if (digest[2] in door_open) and (position.real > 0):
        move_queue += [(position - 1, moveset + 'L')]
    # check right
    if (digest[3] in door_open) and (position.real < 3):
        move_queue += [(position + 1, moveset + 'R')]

max_length = max(final_movesets, key=len)
print('Part 2: longest path is ' + str(len(max_length)))