import networkx as nx
import matplotlib.pyplot as plt

# grafo ponderado
G = nx.Graph()
G.add_weighted_edges_from([
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 3)
])

# econtra árvore geradora mínima usando kruskal com networkX
mst_kruskal = nx.minimum_spanning_tree(G, algorithm='kruskal')

# exibindo árvore (aresta, peso)
positions = nx.spring_layout(G)  #layout de mola para organizar o grafo

# plotando grafo completo
plt.figure(figsize=(8, 6))
nx.draw(G, pos=positions, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=15)
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels={(u, v): f"{data['weight']}" for u, v, data in G.edges(data=True)})

# plotando MST com cor
nx.draw_networkx_edges(mst_kruskal, pos=positions, edge_color='red', width=2)

plt.title("Grafo e Árvore Geradora Mínima (Kruskal)")
plt.show()
