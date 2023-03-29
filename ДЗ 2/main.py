import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

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
        plt.show()
    except nx.NetworkXError:
        print('Матрица не является квадратной')

with open(file='matrix.txt', mode='r',encoding='UTF-8') as f:
    matrix_from_file = []
    try:
        for line in f:
            matrix_from_file.append([int(i) for i in line.split()])
        plot_create(matrix_from_file)
    except ValueError:
        print('Невозможно создать массив из строки')