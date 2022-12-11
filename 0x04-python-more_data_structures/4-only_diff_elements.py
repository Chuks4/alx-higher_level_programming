#!/usr/bin/python3

# Function that returns a set of all elements
# present in only one set


def only_diff_elements(set_1, set_2):

    # Checking if set_1 or set_2 is empty
    if len(set_1) == 0 or len(set_2) == 0:
        return set()

    else:
        # Returns elements in set_1 or set_2, but not in both
        return set_1 ^ set_2
