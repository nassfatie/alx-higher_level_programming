#!/usr/bin/python3

def no_c(my_string):
    updated_str = ''
    for l in my_string:
        if l != 'c' and l != 'C':
            updated_str += l
    return (updated_str)
