import hashlib

door_id = 'ojvtpuvg'
password = ''
index = 0
valid_indices = []
new_pass = [None] * 8

while None in new_pass:
    hashed = hashlib.md5((door_id + str(index)).encode())
    digest = str(hashed.hexdigest())
    hashstr = str(hashed)
    if digest[0:5] == '00000':
        if len(password) < 8:
            password += digest[5]
        if (digest[5].isnumeric()) and (int(digest[5]) < 8):
            if new_pass[int(digest[5])] == None:
                new_pass[int(digest[5])] = digest[6] 
    index += 1
print('Part 1: password is ' + password)
new_pass_str = ''.join(new_pass)
print('Part 2: password is ' + new_pass_str)
