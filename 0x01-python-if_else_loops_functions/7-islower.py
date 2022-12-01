#!/usr/bin/python3
def islower(c):
    # this function takes a character checks if it is lower or uppercase
    # if lowercase, prints c is lowercase
    # if uppercase, prints c is uppercase
    num = ord(c)
    if num >= 97 and num <= 122:
        return True
    else:
        return False
