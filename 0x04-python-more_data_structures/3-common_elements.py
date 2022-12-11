#!/usr/bin/python3

# Function that return a set of common element in two sets


def common_elements(set_1, set_2):

    # Checking if set_1 or set_2 is empty
    if len(set_1) == 0 or len(set_2) == 0:
        return set()
    # Returning the intercept of set_1 and set_2
    return set_1 & set_2
