def counter_add(n):
    def increase_count(k):
        nonlocal n
        n += k
        return n
    return increase_count


print(counter_add(2)(7))
print(counter_add(2)(7))
cnt = counter_add(3)
print(cnt(10))
print(cnt(10))
print(cnt(10))

