import random
import time
import heapq
import networkx as nx

# gerar grado ponderado
def generate_weighted_graph(num_nodes, num_edges, use_networkx=False):
    if use_networkx:
        G = nx.Graph()
        edges = set()
        while len(edges) < num_edges:
            u = random.randint(0, num_nodes - 1)
            v = random.randint(0, num_nodes - 1)
            if u != v and (u, v) not in edges and (v, u) not in edges:
                weight = random.uniform(1, 10)
                edges.add((u, v, weight))
                G.add_edge(u, v, weight=weight)
        return G
    else:
        G = {}
        edges = set()
        while len(edges) < num_edges:
            u = random.randint(0, num_nodes - 1)
            v = random.randint(0, num_nodes - 1)
            if u != v and (u, v) not in edges and (v, u) not in edges:
                weight = random.uniform(1, 10)
                edges.add((u, v, weight))
                if u not in G:
                    G[u] = []
                if v not in G:
                    G[v] = []
                G[u].append((v, weight))
                G[v].append((u, weight))
        return G

# kruskal sem networkX
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal_no_nx(graph, n):
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            if u < v:  # evita arestas duplicadas
                edges.append((weight, u, v))
    edges.sort()  # ordena por peso
    uf = UnionFind(n)
    mst = []
    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
    return mst

# Prim sem networkX
def prim_no_nx(graph, n):
    mst = []
    visited = [False] * n
    min_heap = [(0, 0)]  # começa do nó 0 com peso 0
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if not visited[u]:
            visited[u] = True
            if weight > 0:
                mst.append((u, weight))
            for v, edge_weight in graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (edge_weight, v))
    return mst

# medir o tempo de execução de cada algoritmo
def measure_time(algorithm, graph, n, m):
    start_time = time.time()
    result = algorithm(graph, n)
    end_time = time.time()
    return end_time - start_time

scenarios = [
    (10, 14),
    (100, 140),
    (1000, 1400),
    (10000, 14000)
]

# comparação de todos os algoritmos
for num_nodes, num_edges in scenarios:
    # Gerar grafo
    G_nx = generate_weighted_graph(num_nodes, num_edges, use_networkx=True)
    G_no_nx = generate_weighted_graph(num_nodes, num_edges, use_networkx=False)

    # medindo os tempos de execução
    print(f"\nAnalisando Grafo com {num_nodes} vértices e {num_edges} arestas:")

    # kruskal com networkX
    start_time = time.time()
    mst_kruskal_nx = nx.minimum_spanning_tree(G_nx, algorithm='kruskal')
    kruskal_nx_time = time.time() - start_time
    print(f"Kruskal com NetworkX: {kruskal_nx_time:.4f} segundos")

    # prim com networkX
    start_time = time.time()
    mst_prim_nx = nx.minimum_spanning_tree(G_nx, algorithm='prim')
    prim_nx_time = time.time() - start_time
    print(f"Prim com NetworkX: {prim_nx_time:.4f} segundos")

    # kruskal sem networkX
    kruskal_no_nx_time = measure_time(kruskal_no_nx, G_no_nx, num_nodes, num_edges)
    print(f"Kruskal sem NetworkX: {kruskal_no_nx_time:.4f} segundos")

    # prim sem networkX
    prim_no_nx_time = measure_time(prim_no_nx, G_no_nx, num_nodes, num_edges)
    print(f"Prim sem NetworkX: {prim_no_nx_time:.4f} segundos")
