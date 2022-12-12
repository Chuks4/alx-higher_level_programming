#!/usr/bin/python3

# Function that prints a dictionary by ordered keys


def print_sorted_dictionary(a_dictionary):

    # Check if a_dictionary is empty
    if len(a_dictionary) == 0:
        return a_dictionary

    else:
        # Loop through the dictionary
        for k, v in sorted(a_dictionary.items()):
            print(f'{k}: {v}')
