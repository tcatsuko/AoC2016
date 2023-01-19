import hashlib
salt = 'yjdafjpo'
indices = []
index = 0
seen_hashes = []
#hashed = hashlib.md5((door_id + str(index)).encode())
def find_triplet(digest):
    for c in range(len(digest) - 2):
        c1 = digest[c]
        c2 = digest[c + 1]
        c3 = digest[c + 2]
        if c1 == c2 == c3:
            return c1
    return None

def find_quint(digest, triplet):
    for c in range(len(digest) - 4):
        c1 = digest[c]
        c2 = digest[c + 1]
        c3 = digest[c + 2]
        c4 = digest[c + 3]
        c5 = digest[c + 4]
        if c1 == c2 == c3 == c4 == c5 == triplet:
            return True
    return False
while len(indices) < 64:

    if index < len(seen_hashes):
        digest = seen_hashes[index]
    else:
        current_hash = hashlib.md5((salt + str(index)).encode())
        digest = str(current_hash.hexdigest())
        # for counter in range(2016):
        #     next_hash = hashlib.md5(digest.encode())
        #     digest = str(next_hash.hexdigest())
        seen_hashes += [digest]
    triplet = find_triplet(digest)
    if triplet != None:
        for x in range(index + 1, index + 1001):
            if x < len(seen_hashes):
                new_digest = seen_hashes[x]
            else:
                new_hash = hashlib.md5((salt + str(x)).encode())
                new_digest = str(new_hash.hexdigest())
                # for counter in range(2016):
                #     next_new_hash = hashlib.md5(new_digest.encode())
                #     new_digest = str(next_new_hash.hexdigest())
                # seen_hashes += [new_digest]
            if find_quint(new_digest, triplet) == True:
                indices += [index]
                break
    index += 1
print('Part 1: Index ' + str(indices[-1]) + ' produces the 64th key.')

indices = []
index = 0
seen_hashes = []


while len(indices) < 64:

    if index < len(seen_hashes):
        digest = seen_hashes[index]
    else:
        current_hash = hashlib.md5((salt + str(index)).encode())
        digest = str(current_hash.hexdigest())
        for counter in range(2016):
            next_hash = hashlib.md5(digest.encode())
            digest = str(next_hash.hexdigest())
        seen_hashes += [digest]
    triplet = find_triplet(digest)
    if triplet != None:
        for x in range(index + 1, index + 1001):
            if x < len(seen_hashes):
                new_digest = seen_hashes[x]
            else:
                new_hash = hashlib.md5((salt + str(x)).encode())
                new_digest = str(new_hash.hexdigest())
                for counter in range(2016):
                    next_new_hash = hashlib.md5(new_digest.encode())
                    new_digest = str(next_new_hash.hexdigest())
                seen_hashes += [new_digest]
            if find_quint(new_digest, triplet) == True:
                indices += [index]
                break
    index += 1
print('Part 2: Index ' + str(indices[-1]) + ' produces the 64th key.')
