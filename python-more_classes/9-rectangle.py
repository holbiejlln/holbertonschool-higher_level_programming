#!/usr/bin/python3
"""
Bu modul, düzbucaqlı (Rectangle) təyin edən bir sinif ehtiva edir.
9-cu task üçün kvadrat yaratmağa imkan verən sinif metodu (classmethod)
əlavə edilmişdir.
"""


class Rectangle:
    """
    Düzbucaqlını təyin edən sinif.
    """

    # Hər yeni instansiya başladılan zaman artırılır, silinən zaman azaldılır.
    number_of_instances = 0
    # Düzbucaqlının vizual təsvirində istifadə edilən simvol.
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Yeni Rectangle obyektini başladır.

        Args:
            width (int, optional): Düzbucaqlının eni.
            height (int, optional): Düzbucaqlının hündürlüyü.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Düzbucaqlının enini (width) alır."""
        return self.__width

    @width.setter
    def width(self, value):
        """Düzbucaqlının enini (width) təyin edir."""
        if not isinstance(value, int):
            raise TypeError(
                "width must be an integer")
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
            raise TypeError(
                "height must be an integer")
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
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Düzbucaqlının vizual təsvirini 'print_symbol' istifadə edərək qaytarır.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        line = symbol * self.__width
        return "\n".join([line for i in range(self.__height)])

    def __repr__(self):
        """
        Obyektin rəsmi simvol təsvirini qaytarır.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        İnstansiya silinərkən çağırılır və instansiya sayını azaldır.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Sahəsinə əsasən iki düzbucaqlıdan ən böyüyünü qaytarır.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        size x size ölçülü yeni Rectangle (kvadrat) instansiyasını qaytarır.

        Args:
            size (int, optional): Kvadratın tərəf uzunluğu. Varsayılan 0.

        Returns:
            Rectangle: Yeni kvadrat instansiyası.
        """
        return cls(size, size)
