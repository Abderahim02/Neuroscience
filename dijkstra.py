from typing import List, Tuple, Set


# Définition du type Arc
class Arc:
    def __init__(self, sommet_i, sommet_j, weight):
        self.from_vertex = sommet_i
        self.to_vertex = sommet_j
        self.weight = weight

# Fonction Astar
def Dijsktra(sommet_i, sommet_j, matrix):
    distances, parents = Initialization(sommet_i, matrix)
    GRIS = set([sommet_i])
    NOIR = set()
    b = 1
    while b != 0:
        if len(GRIS) == 0:
            return distances, parents
        sommet_i = CalculateDmin(GRIS, distances, matrix)
        if sommet_i == sommet_j:
            return distances, parents
        L = GetOutgoingArcs(sommet_i, matrix)
        for i in range(len(L)):
            Relacher(L[i], matrix, distances, parents, GRIS, NOIR)
        ColorNodeBlack(sommet_i, GRIS, NOIR)
    return distances, parents

# Fonction Relax
def Relacher(arc, matrix, d  , parent  , GRIS, NOIR):
    x, y = arc.from_vertex, arc.to_vertex
    if d[x] + arc.weight < d[y]:
        d[y] = d[x] + arc.weight
        parent[y] = x
        ColorNodeGray(y, GRIS, NOIR)

# Fonction ColorNodeGray
def ColorNodeGray(sommet, GRIS, NOIR):
    if sommet in NOIR:
        NOIR.remove(sommet)
        GRIS.add(sommet)
    elif sommet not in GRIS:
        GRIS.add(sommet)

# Fonction ColorNodeBlack
def ColorNodeBlack(sommet, GRIS, NOIR):
    NOIR.add(sommet)
    GRIS.remove(sommet)

# Fonction Initialization
def Initialization(sommet,  matrix):
    d = [len(matrix)+1000] * len(matrix)
    parent = [-1] * len(matrix)
    d[sommet] = 0
    return d, parent

# Fonction CalculateDplusHmin
def CalculateDmin(GRIS, d, matrix):
    x = None
    min_val = len(matrix)+1000
    for v in GRIS:
        if d[v] + 1 < min_val:
            x = v
            min_val = d[v] + 1
    return x

# Fonction GetOutgoingArcs
def GetOutgoingArcs(sommet,  matrix):
    arcs = []
    for i in range(len(matrix[sommet])):
        if matrix[sommet][i] != 0:
            arcs.append(Arc(sommet, i, matrix[sommet][i]))
    return arcs

# Fonction de test TestAstar
def TestDijkstra():

    mat0=[[0, 2, 0, 0, 5],
             [2, 0, 1, 0, 0],
             [0, 1, 0, 4, 0],
             [0, 0, 4, 0, 3],
             [5, 0, 0, 3, 0]]
    s0 = 0
    t0 = 4
    distances0, parents0 = Dijsktra(s0, t0, mat0)
    print(distances0)  # output: [0, 2, 3, 7, 5]
    print(parents0)  # output: [-1, 0, 1, 2, 0]


    mat1=[[0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 1],
             [0, 0, 0, 0]]
    s1 = 0
    t1 = 3
    distances1, parents1 = Dijsktra(s1, t1, mat1)
    print(distances1)
    print(parents1)

    
    mat2=[[0, 1, 1, 0, 0],
             [1, 0, 1, 1, 1],
             [1, 1, 0, 2, 2],
             [0, 1, 2, 0, 1],
             [0, 1, 2, 1, 0]]
    
    s2 = 0
    t2 = 4
    distances2, parents2 = Dijsktra(s2, t2, mat2)
    print(distances2)
    print(parents2)

# Appel de la fonction de test
print(TestDijkstra())


def betweenness_centrality (matrix , sommet):
    sum = 0
    paths = []
    for i in range( len(matrix)):
        for j in range(i, len(matrix)):
            path = Dijsktra(i, j, matrix)
            paths.append(path)
    
    for path in paths:
        for i in range(len(path )):
            if sommet == path[i]:
                sum += 1
    return sum


def max_betweenness_centrality (matrix):
    all_centralities = []
    for i in range(len(matrix)):
        all_centralities.append( betweenness_centrality (matrix , i))
        max_cent = max(all_centralities)
        res = []
        for j in range(len(all_centralities)):
            if all_centralities[j] == max_cent:
                res.append(j)
    return res



