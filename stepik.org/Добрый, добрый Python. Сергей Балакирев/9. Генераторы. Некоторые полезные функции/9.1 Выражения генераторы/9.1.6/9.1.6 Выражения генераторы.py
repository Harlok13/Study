cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (j for i in range(1000000) for j in cities)
[print(next(gen), end=' ') for _ in range(20)]
