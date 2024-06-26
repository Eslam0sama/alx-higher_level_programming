#!/usr/bin/python3
"""A module that contain the function to_json_string.
"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object (string).

    Args:
        my_obj (_type_): _description_
    """
    string_json = json.dumps(my_obj)
    return string_json
