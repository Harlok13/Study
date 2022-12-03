def get_rec_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + get_rec_sum(lst[1:])


lst = [8, 11, -5, 4, 3]
print(get_rec_sum(lst))
