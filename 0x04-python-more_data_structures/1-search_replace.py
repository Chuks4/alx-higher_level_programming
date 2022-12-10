#!/usr/bin/python3

# Function that replaces all occurrences of an
# element by another in a new list.
# my_list is the initial list
# search is the element to replace to be replace
# replace is the new element


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    # Checking if my_list is empty
    if len(my_list) == 0:
        return my_list

    # Loop through the list
    else:
        for i in range(len(my_list)):

            # Check if any index of my_list is equal to search
            if my_list[i] == search:

                # Replace index equal to search with replace
                new_list[i] = replace

                # if non is equal to search, return my_list
            else:
                pass

    return new_list
