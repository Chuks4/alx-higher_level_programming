#!/usr/bin/python3


# Function that adds all unique intergers in a list,
# (only once for each integer)

def uniq_add(my_list=[]):

    # Remove all duplicates in the list
    my_set = set(my_list[:])

    # Checking if list is empty
    if len(my_set) == 0:
        return 0

    # Store the additions here
    num_sum = sum(my_set)

    # Return sum
    return num_sum
