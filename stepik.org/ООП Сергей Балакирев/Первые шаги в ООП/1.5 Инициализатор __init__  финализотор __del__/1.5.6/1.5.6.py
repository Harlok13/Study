"""
Решено самостоятельно
"""

class CPU:

    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:

    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = args[:self.total_mem_slots]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {"; ".join([f"{i.name} - {i.volume}" for i in self.mem_slots])}'
        ]


cpu = CPU('Проц', '3.2MHz')
mem1 = Memory('Оперативка 1', '1.8MHz')
mem2 = Memory('Оперативка 2', '1.8MHz')

mb = MotherBoard('Материнка', cpu, mem1, mem2)

print(mb.__dict__)
print(mb.get_config())
