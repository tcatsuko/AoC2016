initial_data = '01111010110010011'

def dragon(in_data):
    a = in_data
    b = in_data[:]
    b = b[::-1]
    b = b.replace('0','2')
    b = b.replace('1','0')
    b = b.replace('2','1')
    return a + '0' + b
def checksum(data):
    result = ''
    for x in range(0,len(data) - 1, 2):
        if data[x] == data[x + 1]:
            result += '1'
        else:
            result += '0'
    return result
disk_size = 272
while len(initial_data) < disk_size:
    initial_data = dragon(initial_data)

init_checksum = checksum(initial_data[:disk_size])
while (len(init_checksum) % 2 == 0):
    init_checksum = checksum(init_checksum)
print('Part 1: Checksum is ' + str(init_checksum))
initial_data = '01111010110010011'
disk_size = 35651584
while len(initial_data) < disk_size:
    initial_data = dragon(initial_data)
print('filled disc, checking checksum')
init_checksum = checksum(initial_data[:disk_size])
while (len(init_checksum) % 2 == 0):
    init_checksum = checksum(init_checksum)
print('Part 2: Checksum is ' + str(init_checksum))
