#!/usr/bin/python3

# Function that prints a dictionary by ordered keys


def print_sorted_dictionary(a_dictionary):

    # Check if a_dictionary is empty
    if a_dictionary == {}:
        return a_dictionary

    else:
        # Loop through the dictionary
        for k in sorted(a_dictionary):
            print(f'{k}: {a_dictionary[k]}')
