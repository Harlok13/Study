lst = ['8', '11', '0', '-23', '140', '1']

int_lst = list(map(int, lst))  # приводим значения в списке к целым числам

filt = filter(lambda x: 100 > abs(x) > 9, int_lst)  # фильтруем по двузначным числам

print(*filt)

