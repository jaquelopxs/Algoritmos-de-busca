import matplotlib.pyplot as plt

# função de união e busca (union-find)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):  #encontra representante elemento u, procura quem é a raiz de quem
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v): #definição de cada união
        root_u = self.find(u)
        root_v = self.find(v) #vertice que unirá com u
        if root_u != root_v:
            # união rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# função que realiza o kruskal
def kruskal(n, edges):
    # ordena pelo peso
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        # se u e v n estão no mesmo conj, n forma ciclo
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

# definição grafo (arestas e vertices) com seus pesos
vertices = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
edges = [
    (vertices['A'], vertices['B'], 1),
    (vertices['A'], vertices['C'], 3),
    (vertices['B'], vertices['C'], 3),
    (vertices['B'], vertices['D'], 6),
    (vertices['C'], vertices['D'], 4),
    (vertices['C'], vertices['E'], 2),
    (vertices['D'], vertices['E'], 5)
]

mst, total_cost = kruskal(len(vertices), edges)

positions = {
    'A': (0, 1),
    'B': (1, 2),
    'C': (2, 1),
    'D': (3, 0),
    'E': (2, -1)
}

# Desenho do grafo inicial e da MST
def plot_graph(edges, mst, positions):
    plt.figure(figsize=(8, 6))

    # Desenhando todas as arestas do grafo original
    for u, v, weight in edges:
        u_pos = positions[list(vertices.keys())[u]]
        v_pos = positions[list(vertices.keys())[v]]
        plt.plot([u_pos[0], v_pos[0]], [u_pos[1], v_pos[1]], 'gray', linestyle='--')
        plt.text((u_pos[0] + v_pos[0]) / 2, (u_pos[1] + v_pos[1]) / 2, str(weight), color='black', fontsize=12)

    # Desenhando as arestas da MST em uma cor diferente
    for u, v, weight in mst:
        u_pos = positions[list(vertices.keys())[u]]
        v_pos = positions[list(vertices.keys())[v]]
        plt.plot([u_pos[0], v_pos[0]], [u_pos[1], v_pos[1]], 'b', linewidth=2)

    # Desenhando os vértices
    for vertex, pos in positions.items():
        plt.plot(pos[0], pos[1], 'ro', markersize=10)
        plt.text(pos[0], pos[1] + 0.1, vertex, ha='center', fontsize=12, fontweight='bold')

    plt.title(f"Árvore Geradora Mínima com custo total: {total_cost}")
    plt.axis('off')
    plt.show()

# Chamando a função para plotar o grafo e a MST
plot_graph(edges, mst, positions)


