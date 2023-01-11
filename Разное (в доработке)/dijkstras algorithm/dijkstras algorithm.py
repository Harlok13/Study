from print_graph import print_graph_with_weighted_edges
from _collections import deque
import random


def random_graph(vertices_quantity: int, edges_quantity: int):
    """Формирование случайного графа"""

    letters = "abcdefghijklmnopqrst"

    assert 4 < vertices_quantity < 21, "ожидалось что количество вершин будет от 5 до 20"
    assert vertices_quantity < edges_quantity < vertices_quantity * (vertices_quantity - 1), \
        "ожидалось что количество рёбер будет больше количества вершин, и не превышать возможное"

    used_edge = set()
    used_vertex = {letters[1], letters[2], letters[3]}
    g = []
    for i in range(edges_quantity):
        v1 = letters[i] if i < vertices_quantity else letters[random.randint(0, vertices_quantity)]
        v2 = v1
        used_vertex.add(v1)
        for k in range(100):
            if v2 != v1 and v2 in used_vertex and (v1 + v2) not in used_edge:
                break
            v2 = letters[random.randint(0, vertices_quantity)]
        used_vertex.add(v2)
        weigt = random.randint(1, 10)
        for u1, u2 in (v1, v2), (v2, v1):
            edge = (u1, u2, weigt)
            g.append(edge)
            used_edge.add(u1 + u2)
    return g


def dijkstra(g, start_vertex):
    """Алгоритм Дейкстры с асимптотикой O(N**2]"""

    adjacencys = {}
    for v1, v2, weight in g:
        if v1 not in adjacencys:
            adjacencys[v1] = {v2: weight}
        else:
            adjacencys[v1][v2] = weight

    way_guide = {start_vertex: start_vertex}
    distance_guide = {start_vertex: 0}

    vertices_queue = deque()
    vertices_queue.append(start_vertex)

    while vertices_queue:
        current_vertex = vertices_queue.popleft()
        for neighbor in adjacencys[current_vertex]:
            d = distance_guide[current_vertex] + adjacencys[current_vertex][neighbor]
            if (neighbor not in distance_guide) or d < distance_guide[neighbor]:
                distance_guide[neighbor] = d
                way_guide[neighbor] = current_vertex
                vertices_queue.append(neighbor)

    return distance_guide, way_guide


def find_minimum_way(way_guide, start_vertex, finish_vertex):
    """Поиск конкретного маршрута"""
    way = []
    current_vertex = finish_vertex

    while current_vertex != start_vertex:
        way.append(current_vertex)
        current_vertex = way_guide[current_vertex]

    return way[::-1]


def dijkstras_algorithm_demonstration():
    N = random.randint(5, 11)  # количество вершин
    M = N * 7 // 5  # количество рёбер

    print("\n формируем случайный граф, у которого", N, "вершин и", M, "рёбер ", end="\n ")
    g = random_graph(N, M)
    print(g)

    start_vertex = "a"
    distance_guide, way_guide = dijkstra(g, "a")
    print("\n определяем длинны кротчайших путей от вершины -", start_vertex, "до остальных вершин графа ",
          "\n", distance_guide)

    finish_vertex = "d"
    print("\n определяем минимальный путь от", start_vertex, "до", finish_vertex,
          "\n", find_minimum_way(way_guide, start_vertex, finish_vertex))

    print_graph_with_weighted_edges(g)


if __name__ == '__main__':
    dijkstras_algorithm_demonstration()
