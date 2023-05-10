import random
import numpy as np
import time
import matplotlib.pyplot as plt
import networkx as nx


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

"Cette fonction renvoie la modularité de la partition community"
def modularity (matrix , community ):
    n = len(matrix)
    result = 0
    for elt1 in community :
        for elt2 in community :
            result += (matrix[elt1 ][ elt2] - (sum(matrix[elt1 ])*
            sum(matrix[elt2 ])/(2*nbAreteGraphe (matrix ))))
    return result /(2*nbAreteGraphe (matrix ))



# Création d'un graphe de réseau cérébral normal
G_normal = nx.watts_strogatz_graph(50, 10, 0.1)

# Création d'un graphe de réseau cérébral chez les individus atteints de troubles du spectre autistique
G_autism = nx.watts_strogatz_graph(50, 10, 0.02)

# Modification des attributs du graphe chez les individus atteints de troubles du spectre autistique
nx.set_node_attributes(G_autism, {n: {'modularity': 0.7, 'clustering': 0.3, 'local_efficiency': 0.5, 'global_efficiency': 0.8} for n in G_autism.nodes})

# Création de la figure avec deux sous-graphes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Affichage du graphe de réseau cérébral normal
pos = nx.circular_layout(G_normal)
nx.draw_networkx(G_normal, pos, ax=ax1, with_labels=False, node_size=100)
ax1.set_title('Graphe de réseau cérébral normal')

# Affichage du graphe de réseau cérébral chez les individus atteints de troubles du spectre autistique
pos = nx.circular_layout(G_autism)
node_colors = [G_autism.nodes[n]['modularity'] for n in G_autism.nodes]
nx.draw_networkx(G_autism, pos, ax=ax2, with_labels=False, node_size=100, node_color=node_colors, cmap='coolwarm')
ax2.set_title('Graphe de réseau cérébral chez les individus atteints de TSA')

# Ajustement des espacements entre les sous-graphes
plt.tight_layout()

# Affichage de la figure
#plt.show()

# Création d'un graphe de réseau cérébral normal
G_normal = nx.watts_strogatz_graph(100, 10, 0.1)

# Création d'un graphe de réseau cérébral chez les patients atteints de sclérose en plaques
G_ms = nx.watts_strogatz_graph(100, 10, 0.1)

# Modification des attributs du graphe chez les patients atteints de sclérose en plaques
nx.set_node_attributes(G_ms, {n: {'modularity': 0.5, 'memory_performance': 0.7} for n in G_ms.nodes})

# Création de la figure avec deux sous-graphes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Affichage du graphe de réseau cérébral normal
pos = nx.circular_layout(G_normal)
nx.draw_networkx(G_normal, pos, ax=ax1, with_labels=False, node_size=100)
ax1.set_title('Graphe de réseau cérébral normal')

# Affichage du graphe de réseau cérébral chez les patients atteints de sclérose en plaques
pos = nx.circular_layout(G_ms)
node_colors = [G_ms.nodes[n]['modularity'] for n in G_ms.nodes]
nx.draw_networkx(G_ms, pos, ax=ax2, with_labels=False, node_size=100, node_color=node_colors, cmap='coolwarm')
ax2.set_title('Graphe de réseau cérébral chez les patients atteints de sclérose en plaques')

# Ajout d'une barre de couleur pour représenter l'attribut modularity
sm = plt.cm.ScalarMappable(cmap='coolwarm')
sm.set_array(node_colors)
cbar = plt.colorbar(sm, ax=[ax1, ax2], orientation='vertical', pad=0.05)
cbar.set_label('Modularity')

# Ajustement des espacements entre les sous-graphes
plt.tight_layout()

# Affichage de la figure
#plt.show()



