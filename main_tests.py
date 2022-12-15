def find_missing_letter(chars):
    d = {}
    for i in chars:
        d.update({ord(i): i})
    for j in range(min(d), max(d)):
        if j in d.keys():
            continue
        else:
            return chr(j)

    return d

print(find_missing_letter(['a','b','c','d','f', 'g']))


