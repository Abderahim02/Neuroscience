
def degre_sortant_weight (sommet, matrix):
    if(sommet > matrix.shape[0]-1):
        return print("ERROR")
    return sum(matrix[sommet][:])


def degre_entrant_weight (sommet, matrix):
    if sommet > matrix.shape[0]-1 :
        return print("ERROR")
    return sum(matrix[:][sommet])


def strength(matrix, sommet):
    return np.abs(degre_sortant_weight (sommet, matrix)-degre_entrant_weight (sommet, matrix))
