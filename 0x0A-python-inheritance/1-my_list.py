#!/usr/bin/python3
"""
The MyList class inherits from list
"""


class MyList(list):
    """MyList class inheriting from list"""
    def __init__(self):
        """To initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
