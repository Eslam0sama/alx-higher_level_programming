#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    for elem in my_list:
        try:
            if i < x:
                print("{:d}".format(elem), end="")
                i += 1
        except ValueError:
            continue

    print()
    return (i+1)
