#!/usr/bin/python3
"""A module that contain the function save_to_json_file.
"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes a python object to txt file using
    JSON representation.

    Args:
        my_obj (_type_): _description_
        filename (str): The file to write to.
    """
    with open(filename, "w", enscoding="utf-8") as file:
        json.dump(my_obj, file)
