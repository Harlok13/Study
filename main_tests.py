def sum_of_intervals(intervals: list) -> int:
    res_sum, last = 0, float('-inf')
    for start, end in sorted(intervals):
        if start > last:
            last = start
        if end > last:
            res_sum, last = res_sum + end - last, end

    return res_sum


if __name__ == '__main__':
    print(sum_of_intervals([[1,2], [6, 10], [11, 15]]))
    assert sum_of_intervals([[1,2], [6, 10], [11, 15]]) == 9
    assert sum_of_intervals([[1,4], [7, 10], [3, 5]]) == 7
    assert sum_of_intervals([[1,5], [10, 20], [1, 6], [16, 19], [5, 11]]) == 19
    assert sum_of_intervals([[0, 20], [-100000000, 10], [30, 40]]) == 100000030

