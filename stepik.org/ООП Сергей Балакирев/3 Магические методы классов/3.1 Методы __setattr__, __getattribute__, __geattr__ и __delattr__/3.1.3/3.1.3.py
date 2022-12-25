lst_in = list(map(int, '1 3 5 6 10'.split()))
print(lst_in)
# print(lst_in[3] + lst_in[5])
for k, v in enumerate(lst_in):
    if k != len(lst_in)-1:
        print(lst_in[k-1]+lst_in[k+1])
    else:
        print(lst_in[k-1]+lst_in[0])
