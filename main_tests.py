def foo(x):
    return x ** 2
num_list = [2, 5, 6 ,3]
print([y for i in num_list if (y := foo(i)) < 20])
