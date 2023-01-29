class BinaryHeap:
    def __init__(self):
        """Инициализация кучи"""
        self.list = [0]
        self.length = 0

    def sift_up(self, i):
        """Просеивание элемента вверх"""
        while i // 2 > 0:
            if self.list[i] < self.list[i // 2]:
                self.list[i // 2], self.list[i] = self.list[i], self.list[i // 2]
            i = i // 2

    def add(self, item):
        """Добавление нового элемента """
        self.list.append(item)
        self.length += 1
        self.sift_up(self.length)

    def sift_down(self, i):
        """Просеивание элемента вниз"""
        while (i * 2) <= self.length:
            k = self.find_min_child(i)
            if self.list[i] > self.list[k]:
                self.list[i], self.list[k] = self.list[k], self.list[i]
            i = k

    def find_min_child(self, i):
        """Поиск потомка с меньшим значением"""
        if i * 2 + 1 > self.length:
            return i * 2
        else:
            if self.list[i * 2] < self.list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def extract_minimum(self):
        """Извлечение из кучи элемента с минимальным значением"""
        minimum = self.list[1]
        self.list[1] = self.list[self.length]
        self.length -= 1
        self.list.pop()
        self.sift_down(1)
        return minimum

    def print(self):
        """Распечатка содержимого кучи"""
        line = 2 ** len(str(bin(self.length))[2:]) * 2
        k = 0
        indent = 0
        for i in range(self.length):
            if (i + 1) % 2 ** k == 0:
                characters = 2 ** (k + 1)
                spaces = line - characters
                indent = spaces // (characters // 2)
                print("\n ", end=" " * (indent // 2))
                k += 1
            print(self.list[i + 1], end=" "*indent)
        print()

    def heap_sort(self):
        """Построение из кучи отсортированного списка"""
        sorted_list = [0] * self.length
        for i in range(self.length):
            sorted_list[i] = self.extract_minimum()
        return sorted_list

    def heap_replacement(self, new_list):
        """Замена содержимого кучи целиком"""
        i = len(new_list) // 2
        self.length = len(new_list)
        self.list = [0] + new_list
        while i > 0:
            self.sift_down(i)
            i = i - 1


def heap_sort_demonstration():
    print("\n",
          " тестируем сортировку кучей (пирамидой)")

    first = [0] * 31  # формируем оригинал списка для тестов
    for i in range(0, 15):
        first[15 + i] = 39 - i
        first[i] = 24 - i

    test_heap = BinaryHeap()  # заполняем кучу поэлементно
    for item in first:
        test_heap.add(item)

    print("\n",
          "исходник ------", first, "\n",
          "пирамида кучи (с поэлементным добавлением) - ")
    test_heap.print()

    test_heap.heap_replacement(first)  # заменяем содержимое кучи разово целиком

    print("\n",
          "пирамида кучи (с преобразованием списка добавленного целиком) - ")
    test_heap.print()

    second = test_heap.heap_sort()  # получаем отсортированный через кучу список
    first.sort()  # сортируем исходный список

    print("\n",
          "отсортировано кучей ------", second, "\n",
          "отсортированный оригинал -", first, "\n",
          "результат тестирования сортировки через кучу -", second == first, "\n")


if __name__ == '__main__':
    heap_sort_demonstration()
