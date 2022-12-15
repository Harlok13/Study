from string import ascii_lowercase
d = {v: k for k, v in enumerate(ascii_lowercase, 1)}
print(d)
print(' '.join(map(str, [d.get(i, '') for i in "The sunset sets at twelve o' clock.".lower() if i in d])))
