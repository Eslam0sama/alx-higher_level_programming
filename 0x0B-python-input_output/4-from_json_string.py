#!/usr/bin/python3
"""A module that contain the function from_json_string.
"""
import json


def from_json_string(my_obj):
    """A function that returns an object represented by a JSON string.

    Args:
        my_obj (_type_): _description_
    """
    obj_python = json.loads(my_obj)
    return obj_python
