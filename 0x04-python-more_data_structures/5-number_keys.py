#!/usr/bin/python3

# Function that returns the number of keys in a dictionary

def number_keys(a_dictionary):

    # Checking if dictionary is empty
    if len(a_dictionary) == 0:
        return 0

    else:
        # Returns the number of keys

        return len(a_dictionary.keys())
