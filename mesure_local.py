import random
import numpy as np
import time
import matplotlib.pyplot as plt


"Cette fonction retourne les voisins du sommet"
def array_of_neighbors (matrix , sommet ):
    neighbors = []
    for i in range( matrix.shape[0]):
        if ( matrix[ sommet ] [ i ] != 0):
            neighbors.append(i)
    return neighbors


"Cette fonction retourne l'ensemble des voisins distance k du sommet"
def k_neighbors(matrix, sommet, k):
    distance = 1
    neighbors = array_of_neighbors(matrix, sommet)
    new_neighbors = []

    while(distance < k):
        for neighbor in neighbors:
            new_neighbors += array_of_neighbors (matrix , neighbor)
            new_neighbors = list(set(new_neighbors))
        neighobrs = new_neighbors
        distance += 1
    return neighbors

"cette fonction calcule le chevauchement topologique de deux sommets d’un graphe"
def topological_overlap (matrix ,S1 ,S2 ,k):
    neighbors1 = k_neighbors (matrix ,S1 ,k)
    neighbors2 = k_neighbors (matrix ,S2 ,k)
    intersection= list(set(neighbors1) & set(neighbors2))
    return len(intersection)



def generate_random_matrix(size, min_value=0, max_value=100):
    return np.array([[random.randint(min_value, max_value) for _ in range(size)] for _ in range(size)])


def plot_topological_overlap_time():
    sizes = list(range(100, 600, 10))
    k_values = [1, 2, 5, 10]  # Valeurs de k choisies pour l'exemple
    plt.figure()
    for k in k_values:
        times = []
        for size in sizes:
            matrix = generate_random_matrix(size)
            S1, S2 = 0,1
            start_time = time.time()
            topological_overlap(matrix, S1, S2, k)
            end_time = time.time()
            times.append(end_time - start_time)

        plt.semilogy(sizes, times, label=f'k={k}')
    plt.xlabel('Nmax')
    plt.ylabel('Temps (secondes)')
    plt.legend()
    plt.grid()
    plt.show()

plot_topological_overlap_time()


"Cette fonction renvoie le coefficient de clusetring d'un sommet"
def clusetring_coefficient_of_vertex (matrix ,sommet ):
    neighbors = array_of_neighbors (matrix , sommet)
    count = 0
    for neighbor1 in neighbors :
        for neighbor2 in neighbors :
            if matrix [neighbor1 ][neighbor2] != 0 :
                count += 1
    return count /( len( neighbors ) * (len( neighbors)-1))


"Cette fonction revoie le coefficient de clusetring totale d'un graphe "
def clusetring_coefficient_graph (Mat):
    clustring_total = 0
    for i in range (len(Mat)):
        clustring_total += clusetring_coefficient_of_vertex(Mat, i)
    return clustring_total/ len(Mat)


def nbAreteGraphe(Mat):
    count=0
    n = len(Mat)
    for i in range (n):
        for j in range(n):
            if Mat[i][j] !=0:
                count+=1
    return count

def modularity (matrix , community ):
    "Cette fonction renvoie la m o d u l a r i t de la partition community"
    n = len(matrix)
    result = 0
    for elt1 in community :
        for elt2 in community :
            result += (matrix[elt1 ][ elt2] -
            (sum(matrix[elt1 ])*
            sum(matrix[elt2 ])/(2*nbAreteGraphe (matrix ))))
    return result /(2*nbAreteGraphe (matrix ))