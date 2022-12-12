# проверить наличие локального атрибута job в p1
# результат должен быть False
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()

print(p1.__dict__)
print('job' in p1.__dict__)
