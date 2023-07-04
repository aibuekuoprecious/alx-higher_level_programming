#!/usr/bin/python3
"""
Defines the Rectangle class representing a rectangle
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
    - width (int): Width of the rectangle.
    - height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.

        Args:
        - width (int): Width of the rectangle (default: 0).
        - height (int): Height of the rectangle (default: 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
        - int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
        - value (int): Width value to be set.

        Raises:
        - TypeError: If the width is not an integer.
        - ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
        - int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
        - value (int): Height value to be set.

        Raises:
        - TypeError: If the height is not an integer.
        - ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - int: Area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
        - int: Perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        - str: Printable string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))
