#!/usr/bin/python3
"""
The lookup function
"""


def lookup(obj):
    """
    Args:
        obj: initial object
        Returns: a list of available attributes and
                 methods of an object
    """
    return dir(obj)
