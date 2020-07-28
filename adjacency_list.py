import networkx as nx
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[] for node in range(nodes)]

    def add_edge(self, u, v):
        self.graph[u - 1].append((u - 1, v - 1))

    def relation(self):
        for idx in range(len(self.graph)):
            print(f"\nPosition [{idx}] => edge {self.graph[idx]}", end='')

    def plot_graph(self):
        edges = [edge for edges in self.graph for edge in edges]
        G = nx.Graph()
        G.add_edges_from(edges)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_size=500, labels={node: node for node in G.nodes()}, node_color='pink', edge_color='black')
        nx.draw_networkx_edge_labels(G, pos, edge_labels={edge: 1 for edge in G.edges()}, font_color='red')
        plt.show()

graph = Graph(5)
graph.add_edge(1, 2)
graph.add_edge(4, 1)
graph.add_edge(2, 3)
graph.add_edge(2, 5)
graph.add_edge(5, 3)
graph.relation()
graph.plot_graph()