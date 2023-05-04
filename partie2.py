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