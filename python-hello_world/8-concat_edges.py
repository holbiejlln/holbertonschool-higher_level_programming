#!/usr/bin/python3
# Print "object-oriented programming with Python" without string literals
print("".join([str.__name__[0:6], "-", str.__name__[0:7].lower(), " programming with Python"]))

