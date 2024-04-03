#!/usr/bin/python3

def safe_print_integer(value):

    try:
        print("{:d}".format(value), end="")
	print()
        if isinstance(value, int):
            return (True)
        else:
            return (False)
    except ValueError:
        pass
