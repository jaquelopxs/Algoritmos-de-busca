import networkx as nx
import time
import random

# grafos ponderados aleatorio
def generate_weighted_graph(num_nodes, num_edges):
    G = nx.Graph()
    edges = set()
    while len(edges) < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v and (u, v) not in edges and (v, u) not in edges:  # evita loops e duplicatas
            weight = random.uniform(1, 10)  # peso aleatório entre 1 e 10
            edges.add((u, v, weight))
    G.add_weighted_edges_from(edges)
    return G

#medir o tempo prim
def measure_prim_time(num_nodes, num_edges):
    G = generate_weighted_graph(num_nodes, num_edges)
    start_time = time.time()
    mst_prim = nx.minimum_spanning_tree(G, algorithm='prim')
    end_time = time.time()
    return end_time - start_time

scenarios = [
    (10, 14),
    (100, 140),
    (1000, 1400),
    (10000, 14000)
]

# tempos de execução
print("Tempo de execução do algoritmo de Prim em diferentes cenários:")
for num_nodes, num_edges in scenarios:
    exec_time = measure_prim_time(num_nodes, num_edges)
    print(f"Grafo com {num_nodes} vértices e {num_edges} arestas: {exec_time:.4f} segundos")
