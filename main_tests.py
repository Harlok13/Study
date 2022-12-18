# # a = [1,2],[6, 10],[11, 15]
# r = [set(range(1, 4)), set(range(7, 10)), set(range(3, 5))]
# # a = set(range(1, 2))
# # b = set(range(6, 10))
# # c = set(range(11,15))
# # print(len(a) + len(b) + len(c))
#
#
# # k = set()
# # for i in r:
# #     k = k.union(i)
# # print(k)
#
# inter = [[1, 2], [6, 10], [11, 15]]
#
#
# def sum_of_intervals(intervals):
#
#     # lst = list(map(lambda a,b: set(range(a,b)), intervals))
#     lst = [set(range(k, j)) for k, j in intervals]
#     s = set()
#     for i in lst:
#         s = s.union(i)
#     print(s)
#     return len(s)
#

def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top    = a
        if top < b: s, top = s+b-top, b
    return s

inter = [[8,9], [1, 2], [6, 10], [11, 15], [4,12], [21, 25], [15, 19], [7, 26]]
print(sum_of_intervals(inter))
print(float('-inf'))
print(sorted(inter))
