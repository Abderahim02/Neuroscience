def vertex_neighbors(s, Mat) :
    T=[]
    for i in range(len(Mat)):
        if Mat[s][i] != 0:
            T.append(i)
    return T 

def test_vertex_neighbors():
    print(vertex_neighbors(6, Coactivation_matrix1))
# test_vertex_neighbors()


def Kth_neighbor (Mat ,sommet ,k):
    "Cette fonction retourne l ' ensemble des voisins distance k du sommet"
    count = 1
    result_set = vertex_neighbors(sommet, Mat)
    result1 = []
    while(count < k ): #count est la profondeur du parcours
        for elt in result: 
            result1 += vertex_neighbors (elt, Mat) #les voisins des voisins
            result1 = list(set(result1 )) #on supprime les doublons
        result_set = result1 #on rassemble les sommets visités
        count += 1 #on descend 
    return result_set

def topological_overlap (Mat ,s1 ,s2 ,k):
    list1 = Kth_neighbor (Mat ,s1 ,k)
    list2 = Kth_neighbor (Mat ,s2 ,k)
    return list(set(list1) & set(list2 )) # n retourne l'intersection des deux ensembles sous forme de liste


def clusetring_coefficient_vertex (Mat ,sommet ):
    "Cette fonction renvoie le coefficient de clusetring d ' un sommet"
    neighbors = vertex_neighbors (sommet, Mat)
    count = 0
    for elt1 in neighbors :
        for elt2 in neighbors :
             if Mat[elt1][elt2] != 0:
                count+=1
    return count /(len( neighbors ) * (len( neighbors)-1))

def clusetring_coefficient_graph (Mat):
    clustring_total = 0
    for i in range (len(Mat)):
        clustring_total += clusetring_coefficient_vertex(Mat, i)
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

import networkx as nx
import matplotlib.pyplot as plt

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

# # Ajout d'une barre de couleur pour représenter l'attribut modularity
# sm = plt.cm.ScalarMappable(cmap='coolwarm')
# sm.set_array(node_colors)
# cbar = plt.colorbar(sm, ax=[ax1, ax2], orientation='vertical', pad=0.05)
# cbar.set_label('Modularity')

# Ajustement des espacements entre les sous-graphes
plt.tight_layout()

# Affichage de la figure
plt.show()



