#!/usr/bin/python3
""" Test script """

from models.rectangle import Rectangle
from models.square import Square

# Testing Rectangle class
rectangle = Rectangle(10, 5)
print(rectangle)  # Output: [Rectangle] (1) 0/0 - 10/5

rectangle.update(1, 2, 3, 4, 5)
print(rectangle)  # Output: [Rectangle] (1) 4/5 - 2/3

rectangle_dict = rectangle.to_dictionary()
print(rectangle_dict)  # Output: {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}

# Testing Square class
square = Square(6)
print(square)  # Output: [Square] (1) 0/0 - 6

square.update(1, 2, 3, 4)
print(square)  # Output: [Square] (1) 4/3 - 2

square_dict = square.to_dictionary()
print(square_dict)  # Output: {'id': 1, 'size': 2, 'x': 4, 'y': 3}

