#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    # Check if my_list is not empty
    if my_list:
        my_list.reverse()

        # Get each element using for loop
        for ele in range(len(my_list)):
            # print each element in a newline
            print("{:d}".format(my_list[ele]))
