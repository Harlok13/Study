from string import ascii_lowercase as asc
gen = (i + j for i in asc for j in asc)
print(*(next(gen) for i in range(50)))
