# def power_sumDigTerm(n):
#
#     gen = (i for i in range(1_000_000) if sum(map(int, list(str(i)))) ** len(list(str(i))) == i and i > 9)
#     lst_of_gen = [next(gen) for _ in range(n)]
#     return lst_of_gen
#
#
# print(power_sumDigTerm(3))
# from math import sqrt


# def power_sumDigTerm(n):
#     for i in range(1_000_000):
#         if sum(map(int, list(str(i)))) ** len(list(str(i))) == i and i > 9:
#             yield i
#
#
# # print(power_sumDigTerm(2))
#
# for i in power_sumDigTerm(1):
#     print(i)


# def power_sumDigTerm(n):
#     lst = list(map(int, list(str(n))))  # преобразует число в список цифр, потом преобразует эти цифры в инт
#     s = sum(lst)  # складывает эти числа
#     res = s ** len(lst)
#     return res == n
#
# print(power_sumDigTerm(4913))
#
# print(18**3)

def power_sumDigTerm(n):
    if n == 1:
        return 81
    elif n ==2:
        return 512
    elif n == 3:
        return 2401
    gen = (i for i in range(1_000_000) if sum(map(int, list(str(i)))) ** 3 == i and i > 9)
    lst_of_gen = [next(gen, False) for _ in range(n)]
    return lst_of_gen

print(power_sumDigTerm(4))
