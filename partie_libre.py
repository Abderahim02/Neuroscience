

# A function that calculates the sum of weights of outgoing edges from a given vertex in a matrix
def degre_sortant_weight(sommet, matrix):
    # Check if the given vertex is within the matrix range
    if sommet > matrix.shape[0] - 1:
        return print("ERROR")
    
    # Calculate the sum of the weights of outgoing edges from the vertex
    return sum(matrix[sommet][:])


#A function that calculates the sum of weights of incoming edges to a given vertex in the matrix
def degre_entrant_weight(sommet, matrix):
    # Check if the given vertex is within the matrix range
    if sommet > matrix.shape[0] - 1:
        return print("ERROR")
    
    # Calculate the sum of the weights of incoming edges to the vertex
    return sum(matrix[:][sommet])


#A function that calculate the strength of a node
def strength(matrix, sommet):
    # Calculate the addition between the sum of outgoing and incoming edge weights for a vertex
    return degre_sortant_weight(sommet, matrix) + degre_entrant_weight(sommet, matrix)

