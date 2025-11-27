#!/usr/bin/python3
"""
Bu modul, düzbucaqlı (Rectangle) təyin edən bir sinif ehtiva edir.
3-cü task üçün düzbucaqlının # simvolu ilə vizual təsvirini qaytaran
__str__ metodu tətbiq edilmişdir.
"""


class Rectangle:
    """
    Düzbucaqlını təyin edən sinif.

    Xüsusiyyətlər:
        - width (en): Düzbucaqlının eni.
        - height (hündürlük): Düzbucaqlının hündürlüyü.
    """

    def __init__(self, width=0, height=0):
        """
        Yeni Rectangle obyektini başladır.

        Args:
            width (int, optional): Düzbucaqlının eni. Varsayılan olaraq 0.
            height (int, optional): Düzbucaqlının hündürsayılan olaraq 0.
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
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Düzbucaqlının perimetrini (perimeter) hesablayır və qaytarır.
        Əgər en və ya hündürlük 0 olarsa, perimetr 0 olur.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Düzbucaqlının vizual təsvirini # simvolu ilə qaytarır.
        Əgər en və ya hündürlük 0 olarsa, boş sətir qaytarır.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        # Hər bir sətirdə 'width' qədər # simvolu
        line = "#" * self.__width
        # Hündürlük qədər sətiri birləşdiririk, hər sətirdən sonra yeni sətir
        # simvolu (\n) qoyulur, sonda son \n kəsilir
        return "\n".join([line for i in range(self.__height)])
