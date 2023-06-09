
import numpy as np

# The functions degre_entrant and degre_sortant calculate the number of incoming and outgoing edges f
# or a given vertex in a matrix. The matrix represents a graph, where non-zero values indicate the
# presence of an edge.

def degre_entrant (sommet, matrix):
    if sommet > matrix.shape[0]-1 :
        return print("ERROR")
    vector = matrix [:, sommet]
    count = 0
    for i in range(len( vector )):
        if vector [i] > 0:
            count += 1
    return count

def degre_sortant (sommet, matrix):
    if(sommet > matrix.shape[0]-1):
        return print("ERROR")
    vector = matrix[sommet, :]
    count = 0
    for i in range(len( vector )):
        if vector[i] > 0:
            count += 1
    return count



#he function max_degre finds the vertices with the maximum degree in a matrix.
def max_degre(matrix):
    max_degre=[-1 for i in range(len(matrix))]
    print(len(matrix))
    for i in range(len(matrix)):
        max_degre[i]=degre_sommet(i, matrix)
    L = max(max_degre)
    res=[]
    for i in range(len(max_degre)):
        if(max_degre[i]==L):
            res.append(i)
    return res



# A function that computes the density of a matrix representing a graph
def calcul_densite(Mat):
    nb_arcs = 0
    n = len(Mat)
    for i in range (n):
        for j in range (n):
            if Mat[i][j] != 0 :
                nb_arcs+=1
    nb_arcs/=2
    return nb_arcs/((n * (n-1))/2)


#A function that calculates the rich club coefficient of a graph represented by the matrix G. It first defines an inner function 
def rich_club_coefficient(G, k):
    def construct_graph_induit_order_k(Mat, k):
        T=Mat
        for i in range (len(Mat)):
            if degre_sommet(i, Mat) < k:
                for j in range(len(Mat[i])):
                    Mat[i][j] = 0
        return T 
    return calcul_densite(construct_graph_induit_order_k(G,k))

from visualisation import *




#This function calculates and plots the time taken for computing the degree of a vertex for different matrix sizes.
def plot_calcul_degre_sommet():
    Valeurs1 = []
    Valeurs2 = []
    for i in range (20, 1600, 20):
        start_time = time.time()
        degre_sommet(8, Coactivation_matrix[:i,:i])
        end_time = time.time()
        Valeurs1.append(end_time - start_time)
        start_time = time.time()
        degre_sommet(18, Coactivation_matrix[:i,:i])
        end_time = time.time()
        Valeurs2.append(end_time - start_time)

    x = [20*i for i in range(len(Valeurs1))]
    plt.semilogy( x, Valeurs1, label = 'le sommet 8')
    plt.semilogy( x, Valeurs2, label='le sommet 18 ')
    # plt.plot(x, Valeurs)
    plt.xlabel('Nmax')
    plt.ylabel('Temps de calcul')
    plt.legend()
    plt.show()

#This function calculates and plots the time taken for computing the density of a matrix for different matrix sizes.
def plot_calcul_densite():
    Valeurs = []
    for i in range (20, 1600, 20):
        start_time = time.time()
        calcul_densite(Coactivation_matrix[:i,:i])
        end_time = time.time()
        Valeurs.append(end_time - start_time)

    x = [20*i for i in range(len(Valeurs))]
    plt.semilogy( x, Valeurs)
    # plt.plot(x, Valeurs)
    plt.xlabel('Nmax')
    plt.ylabel('Temps de calcul')
    plt.legend()
    plt.show()


#his function calculates and plots the time taken for computing the rich club coefficient for different matrix sizes
def plot_calcul_rich_club():
    Valeurs1 = []
    Valeurs2 = []
    for i in range (20, 1600, 20):
        start_time = time.time()
        rich_club_coefficient(Coactivation_matrix[:i,:i], 10)
        end_time = time.time()
        Valeurs1.append(end_time - start_time)
        start_time = time.time()
        rich_club_coefficient(Coactivation_matrix[:i,:i], 60)
        end_time = time.time()
        Valeurs2.append(end_time - start_time)

    x = [20*i for i in range(len(Valeurs1))]
    plt.semilogy( x, Valeurs1, label="k=10")
    plt.semilogy( x, Valeurs2, label="k=60")

    # plt.plot(x, Valeurs)
    plt.xlabel('Nmax')
    plt.ylabel('Temps de calcul')
    plt.legend()
    plt.show()


#All tests
if __name__=='__main__' :
    plot_calcul_degre_sommet()
    plot_calcul_densite()
    plot_calcul_rich_club()
    print(clusetring_coefficient_graph(Coactivation_matrix))
    print(modularity(Coactivation_matrix, [3, 20, 7, 500]))
    print("Ok all_functions")