#!/usr/bin/python3


# Function that prints a matrix of integers
def print_matrix_integer(matrix=[[]]):
    # Loop through the matrix to get the rows of the matrix
    for r in matrix:
        # Loop through each row to get it's element
        for c in r:
            print("{:d}".format(c), end=" " if c != r[-1] else "")
        print()
