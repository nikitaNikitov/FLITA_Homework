import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def graph_is_connected(G) -> bool:
    edges_count = 0
    for i in G.edges:
        if i[0] == i[1]:
            continue
        edges_count += 1
    print(f'{edges_count} > {(len(G.nodes) - 1)} * {(len(G.nodes) - 2)} * 0.5')
    return edges_count > (len(G.nodes) - 1) * (len(G.nodes) - 2) * 0.5


def custom_graph_connected(G):
    all_nodes = list(G)
    connected_nodes = []
    edges = G.edges
    if len(all_nodes) < 2:
        return False
    connected_nodes.append(all_nodes.pop())
    for _ in range(len(all_nodes)):
        result = node_connected(all_nodes, connected_nodes, edges)
        if result is False:
            return False
        all_nodes.remove(result)
        connected_nodes.append(result)
    return True


def node_connected(all_nodes, connected_nodes, edges) -> bool | int:
    for k in all_nodes:
        for edge in edges:
            edge_in, edge_out = edge
            if (k == edge_in and edge_out in connected_nodes) or (
                    edge_in in connected_nodes and k == edge_out):
                return k
    return False


def plot_create(matrix):
    plt.clf()
    try:
        G = nx.from_numpy_array(np.array(matrix), create_using=nx.Graph)
        pos = nx.spring_layout(G)
        labels = {i: i + 1 for i in range(len(nx.nodes(G)))}
        nx.draw(G,
                pos,
                node_color='#ccccff',
                node_size=300,
                edge_color='#9a8ed7',
                labels=labels)
        edge_labels = {i: str(matrix[i[1]][i[0]]) for i in nx.edges(G)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        print(
            'Метод is_connected от networkx передает, что граф: ' +
            ('связной' if nx.is_connected(G) else 'не связной') +
            '\nСледствие о связанности графа передает, что граф: ' +
            ('точно связной' if graph_is_connected(G) else
             'нет доказательства, что точно связной') +
            '\nСобственный метод для проверки связанности графа передает, что граф: '
            + ('связной' if custom_graph_connected(G) else 'не связной'))
        plt.show()

    except nx.NetworkXError:
        print('Матрица не является квадратной')


with open(file='matrix.txt', mode='r', encoding='UTF-8') as f:
    matrix_from_file = []
    try:
        for line in f:
            matrix_from_file.append([int(i) for i in line.split()])
        plot_create(matrix_from_file)
    except ValueError:
        print('Невозможно создать массив из строки')
