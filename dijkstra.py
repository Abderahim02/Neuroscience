from typing import List, Tuple, Set

# Définition du type Vertex
class Vertex:
    def __init__(self, s: int):
        self.s = s

# Définition du type Graph
class Graph:
    def __init__(self, mat: List[List[int]], size: int):
        self.mat = mat
        self.size = size

# Définition du type Arc
class Arc:
    def __init__(self, frm: Vertex, to: Vertex, weight: int):
        self.from_vertex = frm
        self.to_vertex = to
        self.weight = weight

# Fonction Astar
def Dijkstra(s: Vertex, t: Vertex, G: Graph) -> Tuple[List[int], List[int]]:
    distances, parents = Initialization(s, G)
    GRIS = set([s])
    NOIR = set()
    b = 1
    while b != 0:
        if len(GRIS) == 0:
            return distances, parents
        x = CalculateDmin(GRIS, distances, G)
        if x == t:
            return distances, parents
        L = GetOutgoingArcs(x, G)
        for i in range(len(L)):
            Relaxer(L[i], G, distances, parents, GRIS, NOIR)
        ColorNodeBlack(x, GRIS, NOIR)
    return distances, parents

# Fonction Relax
def Relaxer(e: Arc, G: Graph, d: List[int], parent: List[int], GRIS: Set[Vertex], NOIR: Set[Vertex]):
    x, y = e.from_vertex, e.to_vertex
    if d[x.s] + e.weight < d[y.s]:
        d[y.s] = d[x.s] + e.weight
        parent[y.s] = x.s
        ColorNodeGray(y, GRIS, NOIR)

# Fonction ColorNodeGray
def ColorNodeGray(y: Vertex, GRIS: Set[Vertex], NOIR: Set[Vertex]):
    if y in NOIR:
        NOIR.remove(y)
        GRIS.add(y)
    elif y not in GRIS:
        GRIS.add(y)

# Fonction ColorNodeBlack
def ColorNodeBlack(x: Vertex, GRIS: Set[Vertex], NOIR: Set[Vertex]):
    NOIR.add(x)
    GRIS.remove(x)

# Fonction Initialization
def Initialization(s: Vertex, G: Graph) -> Tuple[List[int], List[int]]:
    d = [float('inf')] * G.size
    parent = [-1] * G.size
    d[s.s] = 0
    return d, parent

# Fonction CalculateDplusHmin
def CalculateDmin(GRIS: Set[Vertex], d: List[int], G: Graph) -> Vertex:
    x = None
    min_val = float('inf')
    for v in GRIS:
        if d[v.s] + 1 < min_val:
            x = v
            min_val = d[v.s] + 1
    return x

# Fonction GetOutgoingArcs
def GetOutgoingArcs(x: Vertex, G: Graph) -> List[Arc]:
    arcs = []
    for i in range(len(G.mat[x.s])):
        if G.mat[x.s][i] != 0:
            arcs.append(Arc(x, Vertex(i), G.mat[x.s][i]))
    return arcs

# Fonction de test TestAstar
def TestDijkstra():
    # G0
    G0 = Graph(
        mat=[[0, 2, 0, 0, 5],
             [2, 0, 1, 0, 0],
             [0, 1, 0, 4, 0],
             [0, 0, 4, 0, 3],
             [5, 0, 0, 3, 0]],
        size=5
    )
    s0 = Vertex(0)
    t0 = Vertex(4)
    distances0, parents0 = Dijkstra(s0, t0, G0)
    print(distances0)  # output: [0, 2, 3, 7, 5]
    print(parents0)  # output: [-1, 0, 1, 2, 0]

    # G1
    G1 = Graph(
        mat=[[0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 1],
             [0, 0, 0, 0]],
        size=4
    )
    s1 = Vertex(0)
    t1 = Vertex(3)
    distances1, parents1 = Dijkstra(s1, t1, G1)
    print(distances1)
    print(parents1)

    # G2
    G2 = Graph(
        mat=[[0, 1, 1, 0, 0],
             [1, 0, 1, 1, 1],
             [1, 1, 0, 2, 2],
             [0, 1, 2, 0, 1],
             [0, 1, 2, 1, 0]],
        size=5
    )
    s2 = Vertex(0)
    t2 = Vertex(4)
    distances2, parents2 = Dijkstra(s2, t2, G2)
    print(distances2)
    print(parents2)

# Appel de la fonction de test
print(TestDijkstra())
