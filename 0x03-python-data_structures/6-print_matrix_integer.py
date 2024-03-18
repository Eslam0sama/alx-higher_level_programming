#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for integer in list:
            if integer == list[len(list)-1]:
                print("{:d}".format(integer), end="")
            else:
                print("{:d}".format(integer), end=" ")
        print()
