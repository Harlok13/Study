def fib_rec(N, f=[1, 1]):
    if len(f) < N:
        f.append(f[-1] + f[-2])
        fib_rec(N, f)
    return f


print(fib_rec(7))
