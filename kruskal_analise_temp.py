import heapq
import time
import random

def prim(n, edges):
    # lista adjacente grafo
    graph = {i: [] for i in range(n)}
    for u, v, weight in edges:
        graph[u].append((weight, v))  # (peso, vertice)
        graph[v].append((weight, u))  # grafo não direcionado

    # min heap
    min_heap = [(0, 0)]  # (peso, vertice inicial)
    visited = set()
    mst = []
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        # vertice visitado, ignorado
        if u in visited:
            continue

        # vertice visistado
        visited.add(u)
        total_cost += weight

        # se não é aresta inicial adiciona
        if weight != 0:
            mst.append((prev_vertex, u, weight))

        # adc aresta vertice atual
        for next_weight, v in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (next_weight, v))
                prev_vertex = u  # armazena vertice anterior para a aresta

    return mst, total_cost

# medir tempo prim
def measure_time_prim(n, edges):
    start_time = time.time()
    prim(n, edges)
    end_time = time.time()
    return end_time - start_time

# grafos com número vértices arestas
def generate_graph(num_vertices, num_edges):
    edges = []
    for _ in range(num_edges):
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        weight = random.randint(1, 10)
        if u != v:
            edges.append((u, v, weight))
    return edges

test_cases = [
    (10, 14),       # 10 vértices e 14 arestas
    (100, 140),     # 100 vértices e 140 arestas
    (1000, 1400),   # 1000 vértices e 1400 arestas
    (10000, 14000)  # 10000 vértices e 14000 arestas
]

# impressão dos tempos
for vertices, edges in test_cases:
    edges_list = generate_graph(vertices, edges)
    time_taken = measure_time_prim(vertices, edges_list)
    print(f"Tempo para grafo com {vertices} vértices e {edges} arestas: {time_taken:.6f} segundos")
