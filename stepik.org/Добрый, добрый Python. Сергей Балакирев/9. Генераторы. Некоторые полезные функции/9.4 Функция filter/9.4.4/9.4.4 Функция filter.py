S, G = input().split(), input().split()

intersec = set(S) & set(G)  # находим общие включения

print(*sorted(filter(lambda x: not x % 2, map(int, intersec))))  # сортируем по четным
