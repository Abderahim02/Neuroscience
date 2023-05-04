from visualisation import *

def degre_sommet(sommet, matrix):
    count=0
    for i in range(len(matrix)):
        if(matrix[sommet][i]!=0):
            count += 1
    return count

print(degre_sommet(3, Coactivation_matrix))


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

print(max_degre(Coactivation_matrix))


def calcul_densite(Mat):
    nb_arcs = 0
    n = len(Mat)
    for i in range (n):
        for j in range (n):
            if Mat[i][j] != 0 :
                nb_arcs+=1
    nb_arcs/=2
    return nb_arcs/(n**2)

def rich_club_coefficient(G, k):
    def construct_graph_induit_order_k(Mat, k):
        T=Mat
        for i in range (len(Mat)):
            if degre_sommet(i, Mat) > k:
                for j in range(len(Mat[i])):
                    Mat[i][j] = 0
        return T 
    return calcul_densite(construct_graph_induit_order_k(G,k))

def test_calcul_densite():
    print("La densite du graphe 1 est ",calcul_densite(Coactivation_matrix1))
    print("La densite du graphe 2 est ",calcul_densite(Coactivation_matrix2))
    print("Le rich club coeef du graphe 1 est ",rich_club_coefficient(Coactivation_matrix1, 5))
    print("Le rich club du coeiff graphe 2 est ",rich_club_coefficient(Coactivation_matrix2, 5))
test_calcul_densite()