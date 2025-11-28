#!/usr/bin/python3
"""
This moule dethe built-in list type
and provrint the list in a sorted order.
"""


class MyList(list):
    """
    A custom list class t-in list type
    and adds a metd in ascending order.
    """

    def print_sorted(self):
        """
        Print the list's elements in ascending sorted order.

        The oOnly a sorted
        resentati the list is displayed.
        """
        print(sorted(self))
