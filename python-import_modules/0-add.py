#!/usr/bin/python3
"""0-add.py: import add function and print 1 + 2"""

from add_0 import add  # yalnız bir dəfə add_0 istifadə olunur

a = 1
b = 2

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
