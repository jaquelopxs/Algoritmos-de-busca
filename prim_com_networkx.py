import networkx as nx

# grafo ponderado
G = nx.Graph()
G.add_weighted_edges_from([
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 3)
])

# encontra árvore min usando prim com networkx
mst_prim = nx.minimum_spanning_tree(G, algorithm='prim')

positions = nx.spring_layout(G)

#plotando o grafo completo
plt.figure(figsize=(8, 6))
nx.draw(G, pos=positions, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=15)
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels={(u, v): f"{data['weight']}" for u, v, data in G.edges(data=True)})

#plotando a MST com arestas destacadas em vermelho
nx.draw_networkx_edges(mst_prim, pos=positions, edge_color='red', width=2)

plt.title("Grafo e Árvore Geradora Mínima (Prim)")
plt.show()
