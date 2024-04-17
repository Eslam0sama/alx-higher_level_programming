#!/usr/bin/python3
""" A module that contain the function -> write_file.
    for more information about the function read the documentation of the function below.
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8).

    Args:
        filename (str): The file to write to.
        text (str): The text to be written.

    Returns: the number of characters written.

    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        
    return len(text)
