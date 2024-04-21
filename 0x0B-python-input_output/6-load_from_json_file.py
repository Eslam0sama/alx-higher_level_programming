#!/usr/bin/python3
"""A module that contain the function load_from_json_file.
"""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”.

    Args:
        my_obj (_type_): _description_
        filename (str): The file to load from.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.load(file)
