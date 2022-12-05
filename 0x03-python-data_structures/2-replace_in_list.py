#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    # Replaces an element of a list
    # At a specific positon

    # Checks if idx is a negative integer
    # Or out of range
    if ((idx < 0) or (idx > len(my_list) - 1)):
        return my_list
    else:
        my_list[idx] = element
        return my_list
