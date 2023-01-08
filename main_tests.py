from itertools import groupby


def group_consecutives(lst):
    for _, g in groupby(enumerate(lst), lambda i_x : i_x[0] - i_x[1]):
        r = [x for _, x in g]
        if len(r) > 2:
            yield f"{r[0]}-{r[-1]}"
        else:
            yield from map(str, r)

def range_extraction(lst):
    return ','.join(group_consecutives(lst))


if __name__ == '__main__':
    print(range_extraction([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))

