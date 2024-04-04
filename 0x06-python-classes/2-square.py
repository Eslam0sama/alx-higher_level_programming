#!/usr/bin/python3
  
""" A module that contain square class"""
 

class Square:
    """
    class for Square
    """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
