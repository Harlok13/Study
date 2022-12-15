from string import ascii_lowercase as asc
def high(x):
    d = {}
    for i in x.lower().split():
        lst = []
        for j in i:
            lst.append(ord(j) - 96)
        if lst:
            if sum(lst) not in d:
                d.update({sum(lst): i})
                lst.clear()
            else:
                lst.clear()
    m = max(d)

    return d.get(m, None)
#
# print(high('какая-то строка'))
def high(x):
    alph = {v: k for k, v in enumerate(asc, 1)}
    d = {}
    for i in x.lower().split():
        lst = []
        for j in i:
            lst.append(alph.get(j, ''))
        if lst:
            if sum(lst) not in d:
                d.update({sum(lst): i})
                lst.clear()
            else:
                lst.clear()
    m = max(d)

    return d.get(m, None)

print(high('some string'))
