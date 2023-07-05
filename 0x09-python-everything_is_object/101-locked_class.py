#!/usr/bin/python3
"""
Module containing the LockedClass class.
"""


class LockedClass:
     """
    LockedClass: Class that allows only a specific instance attribute.

    Attributes:
        __slots__ (tuple): The allowed instance attribute(s).
    """
    __slots__ = ('first_name')
