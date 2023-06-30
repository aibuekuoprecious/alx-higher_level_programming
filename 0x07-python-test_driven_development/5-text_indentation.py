#!/usr/bin/python3
"""
    5-text_indentation Module
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after each of this characters
        '.', '?', ':'

        Args:
            text: inital string to work on
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in ['.', '?', ':']:
        text = text.replace(char, char + '\n\n')
    print('\n'.join([line.strip() for line in text.split('\n')]), end='')
