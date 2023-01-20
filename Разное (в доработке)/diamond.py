def diamond(n):
    s = []
    for i in range(n//2+1):
        s.append(f'{"*" + "*" * (i * 2):^{n}}\n')
    res = s[:-1]
    return ''.join(s) + ''.join(res[::-1])

print(diamond(15))

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
print(numbers + [111, 222, 789, 201])
