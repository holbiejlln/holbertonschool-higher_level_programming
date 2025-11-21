#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for char in my_string:
        if char !='c' and char !='C':
            newstr = newstr + char
    return newstr
