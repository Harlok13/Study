def diamond(n):
    s = []
    for i in range(n//2+1):
        s.append(f'{"*" + "*" * (i * 2):^{n}}\n')
    res = s[:-1]
    return ''.join(s) + ''.join(res[::-1])

print(diamond(15))
