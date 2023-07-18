#!/usr/bin/python3
"""
This class will be the "base" of all other classes.
"""


class Base:
    """
    Declaring the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Defining the class constructor
        """
        if cond is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
