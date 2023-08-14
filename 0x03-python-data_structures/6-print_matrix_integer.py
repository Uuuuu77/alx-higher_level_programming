#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for last in matrix:
        for x in range(len(last)):
            if (x != (len(last)-1)):
                print("{:d} ".format(last[x]), end="")
            else:
                print("{:d}".format(last[x]), end="")
        print()
