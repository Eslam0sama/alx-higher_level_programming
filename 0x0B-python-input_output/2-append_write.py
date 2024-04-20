#!/usr/bin/python3
"""A module that contain the function append_write.
"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file.

    Args:
        filename (str): The file to write to.
        text (str): The text to be written.
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
