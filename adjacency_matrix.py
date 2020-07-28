import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = np.zeros((nodes, nodes), dtype=int)

    def add_edge(self, u, v):
        self.graph[u - 1][v - 1], self.graph[v - 1][u - 1] = 1, 1

    def graph_data(self):
        data = pd.DataFrame(self.graph, index=[idx for idx in range(0, self.nodes)],
                            columns=[idx for idx in range(0, self.nodes)])
        adjacency_matrix = data.values
        return data, adjacency_matrix

    def relation(self):
        _, rel = self.graph_data()
        rows, cols = np.where(rel == 1)
        edges = zip(rows.tolist(), cols.tolist())
        for edge in edges:
            print(f"\nedge ==> {edge} = {1}", end='')

    def plot_graph(self):
        _, adjacency_matrix = self.graph_data()
        rows, cols = np.where(adjacency_matrix == 1)
        edges = zip(rows.tolist(), cols.tolist())
        G = nx.Graph()
        G.add_edges_from(edges)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_size=500, labels={node: node for node in G.nodes()}, node_color='pink', edge_color='black')
        nx.draw_networkx_edge_labels(G, pos, edge_labels={edge: 1 for edge in G.edges()}, font_color='red')
        plt.show()


graph = Graph(5)
graph.add_edge(1, 3)
graph.add_edge(3, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 5)
graph.add_edge(4, 5)

_, adjacency_matrix = graph.graph_data()
graph.relation()
graph.plot_graph()
