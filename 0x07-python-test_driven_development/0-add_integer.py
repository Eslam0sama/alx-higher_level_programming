#!/usr/bin/python3
"""A module that contain add_integer function.

"""


def add_integer(a, b=98):
    """_summary_

    Args:
        a (int, float): The first number to be added.
        b (int, float): The second number. Defaults to 98.

    Raises:
        TypeError: Raise TypeError is a or b not integers or floats.

    Returns:
        Return the resukt of the addition.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    x = int(a)
    y = int(b)

    return x+y
