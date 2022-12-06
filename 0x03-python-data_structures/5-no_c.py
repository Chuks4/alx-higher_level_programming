#!/usr/bin/python3


def no_c(my_string):
    # Checking if my_string is empty
    if my_string:
        # dict containing the unicode of the characters to be changed
        my_dict = {67: None, 99: None}
        return my_string.translate(my_dict)
    else:
        return my_string
