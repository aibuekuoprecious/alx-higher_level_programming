#!/usr/bin/python3
""" This module returns the peak of the list
"""


def find_peak(list_of_integers):
    """ This  function finds a peak in a list of unsorted integers.
    """
    if (len(list_of_integers) == 0):
        return None

    else:
        peak = list_of_integers[0]
        for i in range(len(list_of_integers)):
            if list_of_integers[i] > peak:
                peak = list_of_integers[i]
        return peak
