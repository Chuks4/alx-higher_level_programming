#!/usr/bin/python3


# Computes the square value of all integer of a matrix

def square_matrix_simple(matrix=[]):
    # Creating the new_matrix
    new = []

    # Checking if matrix is empty
    if len(matrix) == 0:
        return matrix

    # Looping through the rows and columns of matrix
    new = [[c**2 for c in r] for r in matrix]
    return new
