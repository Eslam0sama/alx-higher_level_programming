#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for elem in my_list:
            try:
                if i < x:
                    print(f"{elem:d}", end="")
                    i += 1
            except:
                continue

    return (i+1)
