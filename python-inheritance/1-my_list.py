#!/usr/bin/python3
"""
This module defines a class that extends the built-in list type
and provides a method to print the list in a sorted order.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list type
    and adds a method for printing the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Print the list's elements in ascending sorted order.

        The original list is not modified. Only a sorted
        representation of the list is displayed.
        """
        print(sorted(self))
