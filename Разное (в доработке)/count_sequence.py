def count_sequence(iter_obj: iter) -> int:
    """Считает самую длинную последовательность повторяющихся чисел"""
    last_num, last_count, res_count = None, 1, 1
    for i in iter_obj:
        if i == last_num: last_count += 1
        else: last_count = 1
        if last_count > res_count: res_count = last_count
        last_num = i
    return res_count


tup1 = (1, 3, 2, 2, 4, 2, 2, 2, 2, 4, 6, 3, 2, 6, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 0)
tup2 = (3, 3, 2, 2, 5, 3, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0)
if __name__ == '__main__':
    assert count_sequence(tup1) == 8
    assert count_sequence(tup2) == 9
