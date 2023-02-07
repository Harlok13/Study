import networkx as nx
import matplotlib.pyplot as plt


def print_graph_with_weighted_edges(elist):
    """Пример elist=[('a','b',5.0),('b','c',3.0),('a','c',1.0),('c','d',7.3)]"""

    g = nx.Graph()
    g.add_weighted_edges_from(elist)

    # pos = nx.spectral_layout(g)
    pos = nx.circular_layout(g)
    nx.draw(g, pos, with_labels=True, node_color="y")
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    plt.show()
    return


def print_graph(elist):
    """Пример elist=[('a','b'),('b','c'),('a','c'),('c','d')]"""

    g = nx.Graph()
    g.add_edges_from(elist)

    pos = nx.spectral_layout(g)
    nx.draw(g, pos, with_labels=True, node_color="y")
    plt.show()
    return


def little_test():
    elist = [('a', 'b'), ('b', 'c'), ('a', 'c'), ('c', 'd')]
    print_graph(elist)

    elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
    print_graph_with_weighted_edges(elist)


if __name__ == "__main__":
    little_test()
