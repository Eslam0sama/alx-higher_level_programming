#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    i = 0
    printed = 0
    for i in range(0, x):
        try:
            if i < x:
                print("{:d}".format(my_list[i]), end="")
                i += 1
                printed += 1

        except (ValueError, TypeError):
            continue

    print()
    return printed
