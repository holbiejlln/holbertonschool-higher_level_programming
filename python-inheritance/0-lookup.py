#!/usr/bin/python3
"""
This module provides a function that returns the list of attributes
and methods available for a given object.
"""


def lookup(obj):
    """
    Return a list containing all attributes and methods of the object.

    Arguments:
        obj: The object whose properties will be inspected.

    Returns:
        A list containing all available attributes and methods.
    """
    return dir(obj)
