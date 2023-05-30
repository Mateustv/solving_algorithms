def encode(strs):
    encoded = ''
    for i in strs:
        encoded += str(len(i)) + '#' + i
    return encoded
def decode(strs):
    decoded = []
    i = 0
    while i < len(strs):
        j = i
        while strs[j] != '#':
            j += 1
        length = int(strs[i:j])
        decoded.append(strs[i+2:j+1+length])
        i = j + 1 + length
    return decoded