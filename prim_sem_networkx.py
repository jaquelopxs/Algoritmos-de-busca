import matplotlib.pyplot as plt
import heapq

def prim(n, edges):
    # lista adjacente para grafo
    graph = {i: [] for i in range(n)}
    for u, v, weight in edges:
        graph[u].append((weight, v))  # (peso, vertice)
        graph[v].append((weight, u))  # grafo não direcionado

    # inicia min_heap
    min_heap = [(0, 0)]  # (peso, vertice inicial)
    visited = set()
    mst = []
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        # se vertice visitado, ignorado
        if u in visited:
            continue

        # marca vertice visitado
        visited.add(u)
        total_cost += weight

        # se n é aresta inicial adicona
        if weight != 0:
            mst.append((prev_vertex, u, weight))

        # adiciona aresta vertice atual
        for next_weight, v in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (next_weight, v))
                prev_vertex = u  # armazena vertice anterior

    return mst, total_cost

# grado com arestas e peso
edges = [
    (0, 1, 1),  # A -- B
    (0, 2, 3),  # A -- C
    (1, 2, 3),  # B -- C
    (1, 3, 6),  # B -- D
    (2, 3, 4),  # C -- D
    (2, 4, 2),  # C -- E
    (3, 4, 5)   # D -- E
]

# chama prim
mst, total_cost = prim(5, edges)

# coodenadas
positions = {
    0: (0, 1),  # A
    1: (1, 2),  # B
    2: (2, 1),  # C
    3: (3, 0),  # D
    4: (2, -1)  # E
}

# nome vetices
vertex_names = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

def plot_graph(edges, mst, positions, vertex_names):
    plt.figure(figsize=(8, 6))

    # desenhando todas as arestas do grafo original
    for u, v, weight in edges:
        if u in positions and v in positions:  # verifica se u e v estão no dicionário positions
            u_pos = positions[u]
            v_pos = positions[v]
            plt.plot([u_pos[0], v_pos[0]], [u_pos[1], v_pos[1]], 'gray', linestyle='--')
            plt.text((u_pos[0] + v_pos[0]) / 2, (u_pos[1] + v_pos[1]) / 2, str(weight), color='black', fontsize=12)

    # dando cor
    for u, v, weight in mst:
        if u in positions and v in positions:
            u_pos = positions[u]
            v_pos = positions[v]
            plt.plot([u_pos[0], v_pos[0]], [u_pos[1], v_pos[1]], 'b', linewidth=2)

    for vertex, pos in positions.items():
        plt.plot(pos[0], pos[1], 'ro', markersize=10)
        plt.text(pos[0], pos[1] + 0.1, vertex_names[vertex], ha='center', fontsize=12, fontweight='bold')

    plt.title(f"Árvore Geradora Mínima com custo total: {total_cost}")
    plt.axis('off')
    plt.show()

# chamando função p/ plotar grafo e a MST
plot_graph(edges, mst, positions, vertex_names)
