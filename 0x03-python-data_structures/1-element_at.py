#!/usr/bin/python3


def element_at(my_list, idx):
    # Retrieves an element of a list

    # Checks if List index is a negative number
    # Or out of range
    if idx < 0 or idx > len(my_list) - 1:
        return None

    # Prints element at index idx
    else:
        return my_list[idx]
