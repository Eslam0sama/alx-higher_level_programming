#!/usr/bin/python3
""" A module that contain the function -> read file.
    for more information about the function read the documentation of the function below.
"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The file to read from.
    """
    with open("test.txt", 'r', encoding='utf-8') as f:

        content = f.read()
        print(content)    
