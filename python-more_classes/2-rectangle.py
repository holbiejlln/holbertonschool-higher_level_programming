#!/usr/bin/python3
"""
Bu modul, düzbucaqlı (Rectangle) təyin edən bir sinif ehtiva edir.
"""


class Rectangle:
    """
    Düzbucaqlını təyin edən sinif.

    Xüsusiyyətlər:
        - width (en): Düzbucaqlının eni. Mütləq int və >= 0 olmalıdır.
        - height (hündürlük): Düzbucaqlının hündürlüyü. Mütləq int və >= 0 olmalıdır.
    """

    def __init__(self, width=0, height=0):
        """
        Yeni Rectangle obyektini başladır.

        Args:
            width (int, optional): Düzbucaqlının eni. Varsayılan olaraq 0.
            height (int, optional): Düzbucaqlının hündürlüyü. Varsayılan olaraq 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Düzbucaqlının enini (width) alır."""
        return self.__width

    @width.setter
    def width(self, value):
        """Düzbucaqlının enini (width) təyin edir."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Düzbucaqlının hündürlüyünü (height) alır."""
        return self.__height

    @height.setter
    def height(self, value):
        """Düzbucaqlının hündürlüyünü (height) təyin edir."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Düzbucaqlının sahəsini (area) hesablayır və qaytarır.

        Returns:
            int: Düzbucaqlının sahəsi (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Düzbucaqlının perimetrini (perimeter) hesablayır və qaytarır.
        Əgər en və ya hündürlük 0 olarsa, perimetr 0 olur.

        Returns:
            int: Düzbucaqlının perimetri (2 * (width + height)).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
