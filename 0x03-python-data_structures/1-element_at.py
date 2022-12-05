#!/usr/bin/python3


def element_at(my_list, idx):
    # Retrieves an element of a list

    # Checks if List index is a negative number
    if idx < 0:
        return None

    # Checks if it's out of range
    elif idx > len(my_list):
        return None

    # Prints element at index idx
    else:
        return "{}".format(my_list[idx])
